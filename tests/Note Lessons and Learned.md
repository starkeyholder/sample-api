I spent some time at the beginning going back and forth between the basic test_health_check example and the pytest documentation link (that in README page). At first, it wasn’t obvious how everything fit together — especially how fixtures work, how client.get() simulates an HTTP request, and the importance of the client parameter in each test function. I initially didn’t pay enough attention to how client was being injected into each test.
After experimenting and re-reading the examples a few times, things started to click. Once I understood the overall pattern, writing additional tests became much more straightforward and consistent.
I learned early on from pytest error output was that I needed a consistent users_db dictionary set up for the tests. The failures and tracebacks made it clear when the in-memory database wasn’t initialized or was in the wrong state, which led me to explicitly create and reset the users_db data before each test.

This is where I spent most of my time. The tests that were failing were:
	•	test_list_users_with_data
	•	test_list_users_active_only
	•	test_delete_user_soft_delete
Initially, I kept adjusting the tests, assuming I had made a mistake. After stepping back and reviewing the API code more carefully, I realized the issue wasn’t with the tests at all — it was in the application logic.
The check for the active_only flag was inverted, which caused the API to return incorrect results. Once I fixed that condition, all three tests passed immediately without any changes to the test code.
It was a good reminder that when tests fail, it doesn’t always mean the tests are wrong — sometimes they’re doing exactly what they’re supposed to do by exposing a bug in the implementation. At the same time, it reminded me to slow down and double-check my own thinking in the test cases, just to make sure the test logic itself makes sense and is validating the right behavior.