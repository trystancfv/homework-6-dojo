## Scenario
In this challenge, you are a junior backend engineer at **TripleZotID**, a mid-sized company that builds authentication and account management tools for other SaaS products. Your team maintains a small authentication service responsible for user logins and password resets. 

During a recent internal audit, the security team discovered that your service is **over-sharing in its logs**. In particular, it logs:
* full email addresses
* raw passwords
* password reset tokens
* complete session identifiers

These logs are  shipped to a centralized logging platform and retained long-term, because they extremely helpful for debugging. However, that also makes them valuable targets. If an attacker ever gained access to the logging storage or if logs were accidentally exposed, the sensitive data included could potentially be used to hijack accounts or impersonate users. 

In response to this, you've been asked to refactor the logging behavior of the service before it’s rolled out fully or reused in any customer products. 

Within `auth_service.py` you will see a handful of functions (`login`, `request_password_reset`, `reset_password`, etc.) with intensive logging throughout. Your task is to **redesign the logging system so it preserves useful information for debugging and monitoring, without exposing any sensitive data that could be used maliciously.** Remember, good logs capture events and context, not secrets.

## Tasks
1. Modify the logging system in `auth_service.py` so that **sensitive data is never written to logs**. This includes, but is not limited to: full email addresses, raw passwords, password reset tokens, and full session identifiers.
2. Implement safer logging patterns, such as masking or partially restricting fields (e.g. a***@example.com), while still logging non-sensitive identifiers so engineers can correlate events.
3. Maintain the original behavior of the authentication flows. Your modifications **must not change**: public function interfaces, return values, as well as successful/failed login and reset behavior. In line with this, all existing authentication functionality in `auth_service.py` should continue to work as before for legitimate requests.

You do not need to add or modify any of the test cases in `checker`. You may write helper functions in `auth_service.py` (for example, a helper to mask emails or centralize logging behavior). You must modify `auth_service.py` in the `/challenge` directory, but there is a non-writable copy in `/challenge/backup` in case you need to restore the original and start over.

All of the test cases in `checker` must pass for the Python executable to give you the flag. In this challenge, you are unable to read the checker script.

Make sure to run the checker script by executing the following in the `/challenge` directory:

```bash
$ ./checker
```

For demonstration of the authentication functionality and usage as an intermediate sanity check, a script called `auth_demo.py` is also available. This file is NOT required by automated tests. It exists purely as a helper. To run the script, execute the following in the `/challenge` directory:

```bash
$ python3 ./auth_demo.py
```
