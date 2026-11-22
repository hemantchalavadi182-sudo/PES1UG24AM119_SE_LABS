# Lab 7: Fuzz Testing

## Objective

* Understand fuzz testing.
* Generate automatic test inputs using Hypothesis.
* Identify unexpected inputs and edge cases.
* Validate application functions using property-based testing.

## Project Description

The Visa Application system contains three main functions:

1. parse_application() – Parses visa type and entry information.
2. processing_average() – Calculates average processing days.
3. payable_fee() – Calculates payable fees after tax and discount.

## Tools Used

* Python 3.12
* Pytest
* Hypothesis

## Testing Approach

Hypothesis generates multiple random inputs to test application behaviour.

Testing includes:

* Valid inputs
* Invalid inputs
* Empty inputs
* Negative values
* Unexpected characters
* Boundary conditions
* Random numerical values

## Test Execution

Run:

`pytest -v`

Run with Hypothesis statistics:

`pytest -v --hypothesis-show-statistics`

## Conclusion

Fuzz testing was implemented using Hypothesis and Pytest.

The application functions were tested with automatically generated inputs and additional edge cases to identify unexpected behaviour and improve input validation.

