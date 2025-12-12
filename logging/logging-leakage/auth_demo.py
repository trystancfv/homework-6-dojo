"""
    Simple demo script for Logging Leakage challenge.

    This script imports the insecure authentication functionality from auth_service.py
    and runs a few example flows so learners (and instructors) can see the logging behavior.

    This file is NOT required by automated tests. It exists purely as a helper.

    To run the demo script, navigate to the challenge directory and run: python3 ./auth_demo.py
"""


from auth_service import (
    initialize_data,
    USERS,
    login,
    request_password_reset,
    reset_password
)


DEMO_USERS = [
    {
        'username': 'alex',
        'email': 'alex@example.com',
        'password': 'alex123'
    },
    {
        'username': 'bob',
        'email': 'bob@example.com',
        'password': 'b0b_secure'
    },
    {
        'username': "charlie",
        'email': 'charlie@example.com',
        'password': 'charlie_pw',
    }
]


def run_demo():
    initialize_data(DEMO_USERS)

    print("== Demo: Logging Leakage auth_service ==")
    print("Available demo users:")
    for u in USERS.values():
        print(f" - {u['username']} / {u['email']} (password={u['password']})")

    print("\nAttempting login with wrong password...")
    login('alex', 'wrong_password', ip_address='203.0.113.10')

    print("\nAttempting login with correct password...")
    session = login('alex', 'alex123', ip_address='203.0.113.10')
    print("Session:", session)

    print("\nRequesting password reset for bob@example.com...")
    token = request_password_reset('bob@example.com')
    print("Reset token:", token)

    print("\nResetting password using token...")
    if token:
        success = reset_password(token, 'new_bob_password')
        print("Password reset success:", success)

    print("\nAll done. Check the logs above for details.")


if __name__ == "__main__":
    run_demo()