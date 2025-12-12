import logging
import uuid
from datetime import datetime, timezone, timedelta


"""
    Basic configurations for logging. Please see the following documentation for more information:
    https://docs.python.org/3/library/logging.html
"""
system_logger = logging.getLogger("auth_logger")
if not system_logger.handlers:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s : %(message)s"
    )


"""
    The following represents an in-memory "database" of users and reset tokens.
    To emphasize the challenge, the "database" has been abstracted as two dictionaries.
"""
USERS = {}
RESET_TOKENS = {}


"""
    Helper functions, used as part of the demo.
"""
def initialize_data(user_data):
    """
    Initializes the in-memory USERS store with accounts based on the information given.
    """
    if USERS:
        return
    
    for user in user_data:
        USERS[user['username']] = {
            'username': user['username'],
            'email': user['email'],
            'password': user['password'],
            'failed_attempts': 0,
            'is_locked': False
        }


"""
    Helper functions, used as part of the authentication flows.
"""
def find_user_by_username(username):
    """Returns a user dict by username, or None if unable to be found."""
    return USERS.get(username)

def find_user_by_email(email):
    """Returns a user dict by email, or None if unable to be found."""
    for user in USERS.values():
        if user['email'] == email:
            return user
    return None

# See the following for more information on Universal Unique Identifiers (UUIDs):
# https://docs.python.org/3/library/uuid.html

def _generate_session_id():
    """Generates a random session ID."""
    return str(uuid.uuid4())

def _generate_reset_token():
    """Generate a random password reset token."""
    return str(uuid.uuid4())


"""
    Core authentication flows. You will make a majority of changes here.
"""
def login(username, password, ip_address=None):
    """
        Attempts to log in a user.
        Returns dict on success, or None on failure.
    """
    user = find_user_by_username(username)


    system_logger.info(
        "Login attempt: username=%s, password=%s, ip=%s",
        username,
        password,
        ip_address        
    )

    if user is None:
        system_logger.warning("Login failed: unknown user=%s, ip=%s", username, ip_address)
        return None
    
    if user['is_locked']:
        system_logger.warning("Login failed: locked account user=%s, ip=%s", username, ip_address)
        return None 
    
    if user['password'] != password:
        user['failed_attempts'] += 1
        system_logger.warning(
            "Login failed: incorrect password for user=%s, attempts=%s, last_password=%s, ip=%s",
            username,
            user['failed_attempts'],
            password,
            ip_address
        )
        if user['failed_attempts'] >= 3:
            user['is_locked'] = True
            system_logger.error(
                "Account locked: too many failures for user=%s, last_password=%s, ip=%s",
                username,
                password,
                ip_address
            )
        return None
    
    user['failed_attempts'] = 0
    new_session_id = _generate_session_id()

    system_logger.info(
        "Login success: successfully logged in user=%s, session_id=%s, password_used=%s, ip=%s",
        username,
        new_session_id,
        password,
        ip_address
    )

    return {
        'username': username,
        'session_id': new_session_id
    }

def request_password_reset(email):
    """
    Requests a password reset link.

    Returns a reset token str on success, or None on failure.
    """
    user = find_user_by_email(email)

    system_logger.info("Password reset requested for email=%s", email)

    if user is None:
        system_logger.warning("Password reset email not found in system: email=%s", email)
        return None
    
    new_reset_token = _generate_reset_token()
    # Saves new reset token to in-memory "database"
    RESET_TOKENS[new_reset_token] = {
        'username': user['username'],
        'created_at': datetime.now(timezone.utc)
    }

    system_logger.info(
        "Generated password reset token=%s for email=%s (user=%s)",
        new_reset_token,
        email,
        user["username"]
    )

    return new_reset_token

def reset_password(token, new_password):
    """
    Resets a user's password in-memory using a reset token.
    Returns True on success, False on failure.
    """
    token_data = RESET_TOKENS.get(token)

    system_logger.info(
        "Password reset attempt with token=%s, new_password=%s",
        token,
        new_password
    )

    if token_data is None:
        system_logger.warning(
            "Password reset failed: invalid token=%s, new_password=%s",
            token,
            new_password
        )
        return False
    
    # Checks if token has expired (each token is valid for 30 minutes)
    created_at = token_data['created_at']
    if datetime.now(timezone.utc) - created_at > timedelta(minutes=30):
        system_logger.warning(
            "Password reset failed: expired token=%s, new_password=%s, created_at=%s",
            token,
            new_password,
            created_at.isoformat()
        )
        # Removes from in-memory "database" as now invalid token
        RESET_TOKENS.pop(token, None)
        return False
    
    username = token_data['username']
    user = find_user_by_username(username)
    if user is None:
        system_logger.error(
            "Password reset failed: token=%s references nonexistent user=%s, new_password=%s",
            token,
            username,
            new_password
        )
        # Removes from in-memory "database" as now invalid token
        RESET_TOKENS.pop(token, None)
        return False
    
    old_password = user['password']
    user['password'] = new_password

    system_logger.info(
        "Password reset success for user=%s, token=%s, old_password=%s, new_password=%s",
        username,
        token,
        old_password,
        new_password
    )

    # Removes from in-memory "database" after use
    RESET_TOKENS.pop(token, None)
    return True