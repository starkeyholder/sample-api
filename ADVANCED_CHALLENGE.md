# Advanced Challenge: Event Publishing & Metrics

**For candidates with data pipeline & automation experience**

If you have experience with event-driven systems, Kafka, or observability platforms, this optional challenge demonstrates those skills while learning pytest.

---

## 🎯 Challenge Overview

**Add event publishing and metrics to the User API using the provided `events.py` module.**

We've created a `py/events.py` module with two classes:
- `EventPublisher` - Publishes events (in-memory for this assessment)
- `MetricsCollector` - Collects application metrics

Your task:
1. **Integrate event publishing** into the existing API endpoints
2. **Add metrics collection** for user operations
3. **Create a metrics endpoint** to expose the collected data
4. **Write pytest tests** for the new functionality

**Key focus: Separation of concerns** - Keep business logic separate from event/metrics logic.

---

## 📋 Part 1: Integrate Event Publishing (30 min)

### Task
Modify `py/main.py` to publish events when users are created/updated/deleted.

### Event Types
- `user.created` - When a user is created
- `user.updated` - When a user is updated
- `user.deleted` - When a user is soft deleted

### Example Integration

```python
from py.events import event_publisher

@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate):
    # ... existing user creation logic ...

    # Publish event AFTER successful creation
    event_publisher.publish(
        event_type="user.created",
        user_id=user_id,
        data={
            "username": user["username"],
            "email": user["email"]
        }
    )

    return user
```

### Requirements
✅ Publish events for create, update, and delete operations
✅ Only publish events AFTER successful operations (not on errors)
✅ Event publishing failure should NOT break the API
✅ Keep event logic separate from business logic

---

## 📋 Part 2: Add Metrics Collection (20 min)

### Task
Track these metrics using the `MetricsCollector`:

```python
from py.events import metrics_collector

# In your endpoints
metrics_collector.increment("users.created")
metrics_collector.increment("users.updated")
metrics_collector.increment("users.deleted")
```

### Metrics to Track
- `users.created` - Count of users created
- `users.updated` - Count of users updated
- `users.deleted` - Count of users deleted
- `events.published` - Count of events successfully published
- `events.failed` - Count of failed event publishes

---

## 📋 Part 3: Create Metrics Endpoint (15 min)

### Task
Add `GET /metrics` endpoint that returns current metrics:

```json
{
  "total_users": 42,
  "active_users": 38,
  "deleted_users": 4,
  "events": {
    "users.created": 42,
    "users.updated": 110,
    "users.deleted": 4,
    "events.published": 156,
    "events.failed": 0
  },
  "uptime_seconds": 3600
}
```

### Implementation Hint
```python
@app.get("/metrics")
async def get_metrics():
    metrics = metrics_collector.get_metrics()
    counters = metrics["counters"]

    return {
        "total_users": len(users_db),
        "active_users": sum(1 for u in users_db.values() if u["is_active"]),
        "deleted_users": sum(1 for u in users_db.values() if not u["is_active"]),
        "events": counters,
        "uptime_seconds": metrics["uptime_seconds"]
    }
```

---

## 📋 Part 4: Write pytest Tests (60-90 min)

### Required Tests

**Event Publishing Tests:**
```python
def test_create_user_publishes_event(client, reset_db):
    """Test that creating a user publishes user.created event"""
    from py.events import event_publisher
    event_publisher.clear()

    response = client.post("/users", json={
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User"
    })

    assert response.status_code == 201
    events = event_publisher.get_events()
    assert len(events) == 1
    assert events[0]["event_type"] == "user.created"
    assert events[0]["data"]["username"] == "testuser"
```

**Metrics Tests:**
```python
def test_metrics_endpoint_returns_user_counts(client, reset_db):
    """Test that /metrics returns accurate user counts"""
    # Create some users
    # ...

    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    assert data["total_users"] == 2
    assert data["active_users"] == 2
```

**Error Handling Tests:**
```python
def test_api_works_when_event_publishing_disabled(client, reset_db):
    """Test graceful degradation when events can't be published"""
    from py.events import event_publisher
    event_publisher.disable()

    # API should still work
    response = client.post("/users", json={...})
    assert response.status_code == 201

    event_publisher.enable()
```

### Test Checklist

✅ Test event publishing for create/update/delete
✅ Test event payload contains correct data
✅ Test metrics endpoint accuracy
✅ Test metrics update after operations
✅ Test graceful degradation (events disabled)
✅ Test that failed event publishing doesn't break API
✅ Use fixtures to reset event/metrics state between tests

---

## 🎓 What We're Evaluating

### 1. Separation of Concerns (25 points)
- ✅ Events/metrics logic separate from business logic
- ✅ Clean integration without coupling
- ✅ Easy to test each component independently

### 2. Event Publishing Integration (25 points)
- ✅ Events published at correct times
- ✅ Event payloads contain appropriate data
- ✅ Error handling (doesn't break API if publishing fails)

### 3. Testing Strategy (30 points)
- ✅ Tests cover event publishing
- ✅ Tests verify metrics accuracy
- ✅ Tests handle error cases
- ✅ Good use of fixtures for setup/cleanup

### 4. Code Quality (20 points)
- ✅ Clean, readable code
- ✅ Good naming and organization
- ✅ Proper use of the provided modules

---

## ⏱️ Time Expectation

**Approximately 2-3 hours total:**
- Part 1 (Events): 30 minutes
- Part 2 (Metrics): 20 minutes
- Part 3 (Endpoint): 15 minutes
- Part 4 (Tests): 60-90 minutes

---

## 💡 Tips

1. **Start with one endpoint** - Get event publishing working for POST /users first
2. **Test as you go** - Write a test for each feature as you add it
3. **Use the provided fixtures** - The existing `reset_db` fixture is helpful
4. **Add an event/metrics reset fixture** - Similar pattern to reset_db
5. **Think about production** - What would break? How would you monitor it?

### Example Fixture for Events/Metrics

```python
@pytest.fixture(autouse=True)
def reset_events_and_metrics():
    """Reset events and metrics before each test"""
    from py.events import event_publisher, metrics_collector
    event_publisher.clear()
    event_publisher.enable()
    metrics_collector.reset()
    yield
    event_publisher.clear()
    metrics_collector.reset()
```

---

## 📤 Submission

When complete, include:

1. **Modified `py/main.py`** - With event/metrics integration
2. **New test file** - `tests/test_events_metrics.py` with comprehensive tests
3. **Test output** - Screenshot/paste showing all tests passing
4. **Brief explanation** - A few sentences about your approach and design decisions

---

## ❓ Questions to Consider

As you work on this (we may discuss in interview):
- Where would event publishing fit in a production system?
- How would you handle event publishing failures?
- What other metrics would be useful to track?
- How would you test this with real Kafka instead of in-memory?
- What happens if the metrics endpoint gets called 1000 times/second?

---

## 🚀 Why This Matters

This challenge reflects real production scenarios:

✅ **Event-Driven Architecture** - Microservices communicate via events
✅ **Observability** - Metrics are critical for monitoring
✅ **Separation of Concerns** - Keep business logic clean
✅ **Graceful Degradation** - Systems should handle failures elegantly
✅ **Testing Distributed Systems** - Mock external dependencies effectively

---

**This is optional but highly recommended** if you have experience with data pipelines, event systems, or observability platforms.

Good luck! 🚀
