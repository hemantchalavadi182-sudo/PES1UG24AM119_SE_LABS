INCLUDED_ENTRIES = {"tourist": 1, "business": 3, "student": 2}


def visa_fee(visa_type, entries, speed, nationality_group):
    if visa_type not in INCLUDED_ENTRIES:
        raise ValueError("unknown visa type")
    if entries < 0:
        raise ValueError("invalid entries")
    included = INCLUDED_ENTRIES[visa_type]
    if nationality_group == "A" and visa_type != "student":
        included += 1
    extra = entries - included
    if extra <= 0:
        return 0
    if speed == "express":
        rate = 100
    else:
        rate = 40
    if extra > 5:
        rate = rate + 20
        if speed == "express":
            rate += 10
    return extra * rate


def documents_complete(forms_filed, photos, is_renewal):
    if is_renewal:
        return forms_filed >= 1
    if photos < 2:
        return False
    return forms_filed >= 3


def application_status(days_left, is_express, is_peak_season):
    if is_express:
        cutoff = 10
    else:
        cutoff = 30
    if is_peak_season:
        cutoff += 15
    if days_left >= cutoff:
        return "open"
    elif days_left >= cutoff - 15:
        return "closing"
    return "closed"
