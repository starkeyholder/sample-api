# pytest Assessment Evaluation Rubric

## Scoring Guide for Candidate Assessment

**Total Points: 100**

Use this rubric to objectively evaluate the candidate's pytest assessment submission. This assessment focuses on **learning ability** and **testing fundamentals** since the candidate has no prior pytest experience.

---

## 1. Test Coverage (30 points)

**Excellent (25-30 points):**
- ✅ 15+ tests covering all endpoints
- ✅ Tests both success and error cases
- ✅ Edge cases considered (validation, conflicts, not found)
- ✅ Logical test organization and naming

**Good (18-24 points):**
- ✅ 12-14 tests covering most endpoints
- ✅ Major success cases covered
- ✅ Some error cases tested
- ⚠️ May miss some edge cases

**Adequate (10-17 points):**
- ✅ 8-11 tests
- ✅ Basic CRUD operations tested
- ⚠️ Missing significant error cases
- ⚠️ Limited edge case testing

**Needs Improvement (0-9 points):**
- ❌ Fewer than 8 tests
- ❌ Only happy paths tested
- ❌ Major endpoints missing

**Score: _____ / 30**

---

## 2. pytest Feature Usage (25 points)

**Excellent (20-25 points):**
- ✅ Fixtures used effectively (client, test data, cleanup)
- ✅ Proper use of pytest assertions
- ✅ Uses parametrize for multiple inputs (bonus feature)
- ✅ Custom fixtures created for common data
- ✅ Demonstrates understanding of pytest concepts

**Good (14-19 points):**
- ✅ Basic fixtures used (client, reset_db)
- ✅ Standard assertions work correctly
- ✅ Shows grasp of pytest basics
- ⚠️ May not use advanced features

**Adequate (7-13 points):**
- ✅ Minimal fixture usage
- ✅ Tests run and pass
- ⚠️ Doesn't leverage pytest features effectively
- ⚠️ Could be more Pythonic

**Needs Improvement (0-6 points):**
- ❌ Doesn't use fixtures properly
- ❌ Poor understanding of pytest patterns
- ❌ Tests are more like scripts than unit tests

**Score: _____ / 25**

---

## 3. Code Quality (20 points)

**Excellent (16-20 points):**
- ✅ Clean, readable test code
- ✅ Good naming conventions (test names describe what they test)
- ✅ Proper Python style (PEP 8)
- ✅ Organized test structure
- ✅ Comments where helpful (not excessive)

**Good (11-15 points):**
- ✅ Readable code
- ✅ Reasonable naming
- ✅ Generally follows Python conventions
- ⚠️ Minor style inconsistencies

**Adequate (6-10 points):**
- ✅ Code works
- ⚠️ Naming could be clearer
- ⚠️ Some style issues
- ⚠️ Could be better organized

**Needs Improvement (0-5 points):**
- ❌ Hard to read or understand
- ❌ Poor naming conventions
- ❌ Inconsistent style
- ❌ Messy organization

**Score: _____ / 20**

---

## 4. API Testing Understanding (15 points)

**Excellent (12-15 points):**
- ✅ Tests verify status codes correctly
- ✅ Validates response body content
- ✅ Tests request validation (400s, 409s, 404s)
- ✅ Understands REST API patterns
- ✅ Tests database state changes

**Good (8-11 points):**
- ✅ Checks status codes
- ✅ Basic response validation
- ✅ Some error testing
- ⚠️ May miss some validation scenarios

**Adequate (4-7 points):**
- ✅ Basic endpoint testing
- ⚠️ Limited response validation
- ⚠️ Minimal error case testing

**Needs Improvement (0-3 points):**
- ❌ Only checks if endpoint responds
- ❌ No validation of responses
- ❌ Doesn't test errors

**Score: _____ / 15**

---

## 5. Learning & Problem-Solving (10 points)

**Excellent (8-10 points):**
- ✅ Clearly learned pytest from documentation
- ✅ Applied concepts correctly without hand-holding
- ✅ Shows initiative (bonus features attempted)
- ✅ Creative solutions to testing challenges

**Good (6-7 points):**
- ✅ Successfully learned pytest basics
- ✅ Applied examples appropriately
- ⚠️ Stayed mostly within provided examples

**Adequate (3-5 points):**
- ✅ Basic understanding achieved
- ⚠️ Limited exploration beyond examples
- ⚠️ May show confusion about concepts

**Needs Improvement (0-2 points):**
- ❌ Didn't demonstrate learning
- ❌ Only copied example without understanding
- ❌ Major conceptual gaps

**Score: _____ / 10**

---

## Bonus Points (Optional, up to +10)

**Award bonus points for:**
- ✅ **Parametrization** (+3): Uses `@pytest.mark.parametrize` effectively
- ✅ **Coverage Report** (+2): Runs and includes `pytest --cov` output
- ✅ **Parallel Execution** (+2): Gets tests working with `pytest -n auto`
- ✅ **Custom Fixtures** (+2): Creates reusable test data fixtures
- ✅ **Documentation** (+1): Adds helpful comments or docstrings

**Bonus Score: _____ / 10**

---

## Total Score Calculation

| Category | Points | Max |
|----------|--------|-----|
| Test Coverage | _____ | 30 |
| pytest Feature Usage | _____ | 25 |
| Code Quality | _____ | 20 |
| API Testing Understanding | _____ | 15 |
| Learning & Problem-Solving | _____ | 10 |
| **Subtotal** | **_____** | **100** |
| Bonus Points | _____ | +10 |
| **TOTAL** | **_____** | **110** |

---

## Interpretation Guide

**90-110 points: STRONG HIRE** 🟢
- Demonstrated excellent learning ability
- Solid understanding of testing fundamentals
- Ready to contribute with minimal ramp-up
- Strong Python skills
- **Recommendation:** Move forward with hire, despite no prior pytest experience

**75-89 points: HIRE WITH RESERVATIONS** 🟡
- Adequate learning ability shown
- Basic testing understanding
- Will need more mentoring/support
- Python skills are decent
- **Recommendation:** Hire if team has mentoring capacity and other qualities are strong

**60-74 points: BORDERLINE** 🟠
- Struggled to learn pytest independently
- Testing fundamentals need work
- Python skills may be weaker than expected
- **Recommendation:** Deep dive in follow-up interview. May need different role or more junior level.

**Below 60 points: NOT RECOMMENDED** 🔴
- Unable to learn pytest from documentation
- Weak testing fundamentals
- Python skills below senior level
- **Recommendation:** Not a fit for Senior Test Automation Engineer role

---

## Key Red Flags to Watch For

🚩 **Fewer than 10 tests** - Didn't meet minimum requirements

🚩 **Only copied examples** - No original work, suggests can't learn independently

🚩 **All tests are identical patterns** - May not understand what's being tested

🚩 **Tests don't pass** - Basic execution issues

🚩 **No fixtures used** - Didn't grasp core pytest concept from docs

🚩 **No error testing** - Doesn't understand API testing fundamentals

---

## Green Flags to Look For

✅ **Exceeded minimum requirements** - Shows initiative

✅ **Used parametrize** - Learned advanced feature independently

✅ **Clean, readable code** - Professional quality

✅ **Thoughtful test names** - Understands testing communication

✅ **Edge cases tested** - Critical thinking applied

✅ **Custom fixtures created** - Shows architectural thinking

---

## Follow-Up Interview Questions (Based on Results)

**If score is high (85+):**
- "Walk me through your approach to learning pytest"
- "What was the most challenging test to write?"
- "How would you approach parallel test execution for a large suite?"

**If score is medium (70-84):**
- "What parts of pytest were confusing?"
- "How comfortable are you with the fixture system?"
- "Let's pair on adding one more test together" (live coding)

**If score is low (<70):**
- "What resources did you use to learn pytest?"
- "How much time did you spend on this?"
- "Show me your Python testing experience before this" (verify resume claims)

---

## Final Hiring Decision Framework

**Hire if:**
- Score ≥ 90, OR
- Score ≥ 75 AND exceptional architecture/systems experience (which Andy has), OR
- Score ≥ 70 AND strong performance in other interview rounds

**Do NOT hire if:**
- Score < 60, OR
- Evidence of not attempting to learn (copy-paste only), OR
- Fundamental Python weaknesses revealed

---

**Remember:** This candidate has 20+ years of automation experience but NO pytest experience. The goal is to assess:
1. **Learning ability** - Can he pick up new tools quickly?
2. **Testing fundamentals** - Does he understand what makes good tests?
3. **Python proficiency** - Is his Python solid enough to learn frameworks quickly?

If he scores well on these dimensions, the specific pytest knowledge gap can be closed quickly on the job.
