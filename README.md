# pytest Assessment - User Management API

Welcome to the pytest technical assessment! This is a practical exercise designed to evaluate your ability to learn and apply pytest for API testing.

## 🎯 Assessment Goals

This assessment will help us understand:
1. Your ability to learn pytest quickly (documentation and examples provided)
2. How you approach API testing
3. Your Python code quality and testing patterns
4. Your problem-solving approach when learning new tools

## 📋 What You're Testing

A simple FastAPI User Management API with these endpoints:

- `GET /health` - Health check
- `POST /users` - Create a new user
- `GET /users` - List all users (with optional `active_only` filter)
- `GET /users/{user_id}` - Get a specific user
- `PUT /users/{user_id}` - Update a user
- `DELETE /users/{user_id}` - Soft delete (sets is_active=False)
- `DELETE /users/{user_id}/permanent` - Permanently delete

## 🚀 Getting Started

### 1. Setup Your Environment

```bash
# Clone this repository (if you haven't already)
git clone <repository-url>
cd sample-api

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Verify the API Works

```bash
# Start the API server (in one terminal)
uvicorn py.main:app --reload --port 8000

# In another terminal, test the health endpoint
curl http://localhost:8000/health
```

You should see: `{"status":"healthy","timestamp":"..."}`

### 3. Run the Example Test

```bash
# Run the one example test we provided
pytest -v

# You should see 1 test pass: test_health_check
```

## 📝 Your Task

**Add comprehensive test coverage for all API endpoints.**

We've provided one example test (`test_health_check`) to show you pytest basics. Your job is to:

1. **Write tests for all endpoints** - Cover success cases and error cases
2. **Use pytest features effectively** - Fixtures, parametrization, assertions
3. **Follow testing best practices** - Clear test names, good organization, readable code

### Minimum Requirements (Must Complete)

✅ **At least 15 tests total** covering:
- User creation (success + validation errors)
- User listing (empty, with data, filtering)
- User retrieval (success + not found)
- User updates (success + conflicts)
- User deletion (both soft and permanent)

✅ **Use pytest fixtures** - For test client, test data, database cleanup

✅ **Test error cases** - 404s, 409 conflicts, validation errors

✅ **All tests must pass** - Run `pytest -v` to verify

### Bonus Points (Optional)

🌟 **Use pytest.mark.parametrize** - Test multiple inputs in one test

🌟 **Add test coverage reporting** - Run `pytest --cov=py --cov-report=term-missing`

🌟 **Create custom fixtures** - For common test data (e.g., sample users)

🌟 **Test edge cases** - Empty strings, very long inputs, special characters

🌟 **Parallel execution** - Get tests running with `pytest -n auto` (pytest-xdist)

🌟 **Advanced Challenge** - See [ADVANCED_CHALLENGE.md](ADVANCED_CHALLENGE.md) for an optional Kafka/event streaming challenge (for candidates with data pipeline experience)

## 📚 pytest Learning Resources

**Official Docs:**
- pytest documentation: https://docs.pytest.org/
- FastAPI testing: https://fastapi.tiangolo.com/tutorial/testing/

**Key Concepts to Learn:**

### Fixtures
```python
@pytest.fixture
def sample_user():
    return {"username": "testuser", "email": "test@example.com", "full_name": "Test User"}
```

### Parametrization
```python
@pytest.mark.parametrize("username,expected", [
    ("abc", 409),  # Too short
    ("validuser", 201),  # Valid
])
def test_create_user_username_validation(client, username, expected):
    # Test multiple inputs
```

### Async Tests (if needed)
```python
@pytest.mark.asyncio
async def test_something_async():
    result = await some_async_function()
    assert result == expected
```

## 🧪 Running Your Tests

```bash
# Run all tests with verbose output
pytest -v

# Run specific test file
pytest tests/test_users.py -v

# Run specific test
pytest tests/test_users.py::test_create_user_success -v

# Run with coverage report
pytest --cov=py --cov-report=term-missing

# Run tests in parallel (optional)
pytest -n auto
```

## 📤 Submission

When you're done:

1. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add comprehensive pytest test coverage"
   git push
   ```

2. **Verify all tests pass**:
   ```bash
   pytest -v
   ```

3. **Send us**:
   - Link to your GitHub repository
   - Test output showing all tests passing
   - Any notes about your approach or challenges

## ⏱️ Time Expectation

**Recommended: 2-4 hours**

This is not a speed test - we value quality over speed. Take your time to:
- Read the pytest documentation
- Understand the API behavior
- Write clean, readable tests

## ❓ Questions?

If you have questions about:
- **The assessment requirements** - Email us
- **How pytest works** - Check the docs first, then ask
- **The API behavior** - Read `py/main.py` or test it manually

## 🎓 What We're Looking For

**Strong candidates will:**
- ✅ Learn pytest quickly from documentation
- ✅ Write clear, well-organized tests
- ✅ Cover both success and error cases
- ✅ Use fixtures effectively
- ✅ Follow Python best practices

**We are NOT expecting:**
- ❌ 100% code coverage
- ❌ Complex mocking or advanced pytest features
- ❌ Performance optimization
- ❌ Prior pytest expertise (you're learning it now!)

## 💡 Tips

1. **Start simple** - Get basic tests working first, then add more
2. **Read the API code** - Understanding `py/main.py` helps you know what to test
3. **Use the example** - The `test_health_check` shows the pattern
4. **Run tests frequently** - Verify each test works before moving on
5. **Ask questions** - If something is unclear, reach out

---

**Good luck! We're excited to see your work.** 🚀

*This assessment mirrors real-world testing practices used in production systems.*
