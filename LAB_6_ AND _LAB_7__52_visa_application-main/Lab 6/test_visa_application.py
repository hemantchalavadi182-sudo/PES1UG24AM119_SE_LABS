import pytest

from visa_application import (
    visa_fee,
    documents_complete,
    application_status
)


# ==========================================
# VISA FEE TEST CASES
# ==========================================

def test_unknown_visa_type():
    with pytest.raises(ValueError):
        visa_fee("work", 5, "normal", "A")


def test_negative_entries():
    with pytest.raises(ValueError):
        visa_fee("tourist", -1, "normal", "A")


def test_tourist_included_entries():
    assert visa_fee("tourist", 1, "normal", "B") == 0


def test_business_included_entries():
    assert visa_fee("business", 3, "normal", "B") == 0


def test_student_included_entries():
    assert visa_fee("student", 2, "normal", "B") == 0


def test_nationality_group_a_extra_entry():
    assert visa_fee("tourist", 3, "normal", "A") == 40


def test_student_group_a():
    assert visa_fee("student", 3, "normal", "A") == 40


def test_normal_speed_fee():
    assert visa_fee("tourist", 3, "normal", "B") == 80


def test_express_speed_fee():
    assert visa_fee("tourist", 3, "express", "B") == 200


def test_extra_entries_more_than_five_normal():
    assert visa_fee("tourist", 7, "normal", "B") == 360


def test_extra_entries_more_than_five_express():
    assert visa_fee("tourist", 7, "express", "B") == 780


# ==========================================
# DOCUMENT COMPLETION TEST CASES
# ==========================================

def test_renewal_documents_complete():
    assert documents_complete(1, 0, True) is True


def test_renewal_documents_incomplete():
    assert documents_complete(0, 2, True) is False


def test_new_application_complete():
    assert documents_complete(3, 2, False) is True


def test_insufficient_photos():
    assert documents_complete(3, 1, False) is False


def test_insufficient_forms():
    assert documents_complete(2, 2, False) is False


# ==========================================
# APPLICATION STATUS TEST CASES
# ==========================================

def test_express_open():
    assert application_status(10, True, False) == "open"


def test_express_closing():
    assert application_status(9, True, False) == "closing"

def test_express_closed():
    assert application_status(-6, True, False) == "closed"


def test_normal_open():
    assert application_status(30, False, False) == "open"


def test_normal_closing():
    assert application_status(29, False, False) == "closing"


def test_normal_closed():
    assert application_status(10, False, False) == "closed"


def test_peak_season_express_open():
    assert application_status(25, True, True) == "open"


def test_peak_season_normal_closing():
    assert application_status(35, False, True) == "closing"


def test_peak_season_normal_closed():
    assert application_status(10, False, True) == "closed"
