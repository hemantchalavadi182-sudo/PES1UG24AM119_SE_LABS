# Lab 6: Code and Branch Coverage Analysis

## Objective

* Understand code coverage and branch coverage.
* Measure test coverage using Coverage.py.
* Identify untested statements and decision branches.
* Improve test cases to achieve maximum coverage.

## Project Description

This project implements a Visa Application system with three main functionalities:

1. Visa fee calculation.
2. Document completeness verification.
3. Application status determination.

## Files

| File                     | Description                  |
| ------------------------ | ---------------------------- |
| visa_application.py      | Main application source code |
| test_visa_application.py | Pytest test cases            |
| htmlcov/                 | HTML coverage report         |

## Tools Used

* Python 3.12
* Pytest
* Coverage.py

## Testing

Command:

`coverage run --branch -m pytest`

All 25 test cases passed successfully.

## Coverage Results

| Metric             | Result |
| ------------------ | -----: |
| Total test cases   |     25 |
| Passed             |     25 |
| Failed             |      0 |
| Statement coverage |   100% |
| Branch coverage    |   100% |
| Missing statements |      0 |
| Partial branches   |      0 |

## Coverage Report

Generate the HTML report using:

`coverage html`

Open:

`htmlcov/index.html`

## Conclusion

Successfully achieved 100% statement coverage and 100% branch coverage.

All 25 test cases passed, and all 26 decision branches were covered. No statements or branches remain untested.

