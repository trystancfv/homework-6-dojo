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

def _mask_email(email):
    """
    Returns a privacy-maintaining version of an email address.
    If the value is deemed an invalid-looking email, it is returned unchanged.
    """
    if '@' not in email:
        return email
    
    address, domain = email.split('@', 1)
    if not address: 
        return email
    
    if len(address) == 1 or len(address) == 2:
        masked_address = address[0] + '*'
    else:
        masked_address = address[0] + '***' + address[-1]
    
    return f"{masked_address}@{domain}"

def _shorten_token_id(token):
    """
    Returns a shortened identifier for a token for secure logging.
    """
    if not token:
        return '<none>'
    if len(token) <= 8:
        return token
    return token[:8] + '...'
        

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
        "Login attempt: username=%s, ip=%s",
        username,
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
            "Login failed: incorrect password for user=%s, attempts=%s, ip=%s",
            username,
            user['failed_attempts'],
            ip_address
        )
        if user['failed_attempts'] >= 3:
            user['is_locked'] = True
            system_logger.error(
                "Account locked: too many failures for user=%s, ip=%s",
                username,
                ip_address
            )
        return None
    
    user['failed_attempts'] = 0
    new_session_id = _generate_session_id()

    system_logger.info(
        "Login success: successfully logged in user=%s, session_id=%s, ip=%s",
        username,
        _shorten_token_id(new_session_id),
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

    masked_email = _mask_email(email)
    system_logger.info("Password reset requested for email=%s", masked_email)

    if user is None:
        system_logger.warning("Password reset email not found in system: email=%s", masked_email)
        return None
    
    new_reset_token = _generate_reset_token()
    # Saves new reset token to in-memory "database"
    RESET_TOKENS[new_reset_token] = {
        'username': user['username'],
        'created_at': datetime.now(timezone.utc)
    }

    system_logger.info(
        "Generated password reset token=%s for email=%s (user=%s)",
        _shorten_token_id(new_reset_token),
        masked_email,
        user['username']
    )

    return new_reset_token

def reset_password(token, new_password):
    """
    Resets a user's password in-memory using a reset token.
    Returns True on success, False on failure.
    """
    token_data = RESET_TOKENS.get(token)

    system_logger.info(
        "Password reset attempt with token=%s",
        _shorten_token_id(token)
    )

    if token_data is None:
        system_logger.warning(
            "Password reset failed: invalid token=%s",
            _shorten_token_id(token)
        )
        return False
    
    # Checks if token has expired (each token is valid for 30 minutes)
    created_at = token_data['created_at']
    if datetime.now(timezone.utc) - created_at > timedelta(minutes=30):
        system_logger.warning(
            "Password reset failed: expired token=%s, created_at=%s",
            _shorten_token_id(token),
            created_at.isoformat()
        )
        # Removes from in-memory "database" as now invalid token
        RESET_TOKENS.pop(token, None)
        return False
    
    username = token_data['username']
    user = find_user_by_username(username)
    if user is None:
        system_logger.error(
            "Password reset failed: token=%s references nonexistent user=%s",
            _shorten_token_id(token),
            username
        )
        # Removes from in-memory "database" as now invalid token
        RESET_TOKENS.pop(token, None)
        return False
    
    user['password'] = new_password

    system_logger.info(
        "Password reset success for user=%s, token=%s",
        username,
        _shorten_token_id(token)
    )

    # Removes from in-memory "database" after use
    RESET_TOKENS.pop(token, None)
    return True