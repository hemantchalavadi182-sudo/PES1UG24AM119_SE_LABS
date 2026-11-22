import pytest
import math

from hypothesis import given, strategies as st

from visa_application import (
    parse_application,
    processing_average,
    payable_fee
)


# ==========================================
# 1. PARSE APPLICATION FUZZ TESTING
# ==========================================

@given(st.one_of(st.text(), st.none()))
def test_parse_application_no_crash(s):
    try:
        result = parse_application(s)
        assert isinstance(result, tuple)
        assert isinstance(result[0], str)
        assert isinstance(result[1], int)
    except ValueError:
        pass

@given(
    st.text(
        alphabet=st.characters(
            blacklist_categories=("Cc", "Cs"),
            blacklist_characters=":"
        ),
        min_size=1
    ).filter(lambda x: bool(x.strip())),
    st.integers(min_value=0, max_value=10000)
)
def test_parse_application_valid(visa, entries):
    result = parse_application(f"{visa}:{entries}")

    assert result[0] == visa.strip().title()
    assert result[1] == entries

# ==========================================
# 2. PROCESSING AVERAGE FUZZ TESTING
# ==========================================

@given(st.one_of(st.text(), st.none()))
def test_processing_average_no_crash(s):
    try:
        result = processing_average(s)
        assert isinstance(result, int)
    except ValueError:
        pass


@given(
    st.lists(
        st.integers(min_value=0, max_value=10000),
        min_size=1,
        max_size=100
    )
)
def test_processing_average_valid(values):
    csv_data = ",".join(map(str, values))

    result = processing_average(csv_data)

    assert result == sum(values) // len(values)


# ==========================================
# 3. PAYABLE FEE FUZZ TESTING
# ==========================================

@given(st.one_of(st.text(), st.none()))
def test_payable_fee_no_crash(s):
    try:
        result = payable_fee(s)
        assert isinstance(result, (int, float))
        assert math.isfinite(result)
        assert result >= 0
    except ValueError:
        pass


@given(
    st.floats(
        min_value=0,
        max_value=100000,
        allow_nan=False,
        allow_infinity=False
    ),
    st.floats(
        min_value=0,
        max_value=100000,
        allow_nan=False,
        allow_infinity=False
    )
)
def test_payable_fee_valid(fee, discount):
    result = payable_fee(f"{fee}|{discount}")

    expected = max(fee * 1.18 - discount, 0)

    assert result == pytest.approx(expected)


# ==========================================
# 4. EDGE CASE TESTING
# ==========================================

def test_empty_application():
    with pytest.raises(ValueError):
        parse_application("")


def test_invalid_entries():
    with pytest.raises(ValueError):
        parse_application("tourist:abc")


def test_negative_entries():
    with pytest.raises(ValueError):
        parse_application("tourist:-2")


def test_empty_processing_days():
    with pytest.raises(ValueError):
        processing_average("")


def test_invalid_processing_days():
    with pytest.raises(ValueError):
        processing_average("5,abc,10")


def test_negative_processing_days():
    with pytest.raises(ValueError):
        processing_average("5,-10,15")


def test_invalid_fee():
    with pytest.raises(ValueError):
        payable_fee("abc|500")


def test_negative_fee():
    with pytest.raises(ValueError):
        payable_fee("-1000|100")


def test_discount_greater_than_fee():
    assert payable_fee("100|500") == 0
