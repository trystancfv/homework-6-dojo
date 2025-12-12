## Scenario
In this challenge, you are a junior backend engineer at **TripleZotID**, a mid-sized company that builds authentication and account management tools for other SaaS products. Your team manages a small authentication service that primarily handles user logins and password resets. Recently, a security team at your company ran an internal audit and found that your service is **over-sharing in its logs**. In particular, it records full email addresses, session IDs, and even password reset tokens.

These logs are extremely useful for debugging and are eventually shipped to a centralized logging platform so that various engineers and analysts have access. Because of their value, they are also backed up and retained for long periods of time. However, if an attacker were to ever gain access to the logging system or if log files were accidentally shared, the sensitive inputs included could potentially be used to hijack accounts or impersonate users. In response to this, you’ve been asked to fortify the internal behavior of the service before it’s rolled out fully or reused in any customer products. 

Within `auth_service.py` you will see a handful of functions (`login`, `request_password_reset`, `reset_password`, etc.) with intensive logging throughout. As mentioned, the logs are very helpful for debugging, but they clearly contain sensitive information. Your job is to **redesign the logging system so it preserves useful information for debugging and monitoring, without exposing any sensitive data that could be used maliciously.**

## Tasks

1. Modify the logging system in `auth_service.py` so that **sensitive data is never written to logs**. This includes, but is not limited to: emails, raw passwords, password reset tokens, and full session identifiers.
2. Implement safer logging patterns, such as masking or partially restricting fields (for example, masking email addresses) while still logging non-sensitive identifiers so that engineers can still correlate events.
3. Maintain the original behavior of the authentication flows. This would include the public function interfaces, return values, as well as successful/failed login and reset behavior, all of which should remain unchanged. Additionally, all existing functionality in `auth_service.py` should continue to work as before for legitimate requests.
Ensure that all of the test cases in `checker` pass, including tests that verify both:
  * The authentication flows still work correctly.
  * Sensitive values are **no longer present** in the captured log output.
You do not need to add or modify any of the test cases in `checker`. You may write helper functions in `auth_service.py` (for example, a helper to mask emails or centralize logging behavior). You must modify `auth_service.py` in the `/challenge` directory, but there is a non-writable copy in `/challenge/backup` in case you need to restore the original and start over.

All of the test cases in `checker` must pass for the Python executable to give you the flag. In this challenge, you are unable to read the checker script.

Make sure to run the checker script by doing the following in the `/challenge` directory:

```bash
$ ./checker
```
