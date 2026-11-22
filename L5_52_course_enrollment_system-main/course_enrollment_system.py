"""Course enrollment system for managing student registrations."""

import hashlib
import os
import secrets

courses = {
    "CS101": {
        "title": "Data Structures",
        "seats": 3,
        "fee": 500.0,
        "is_closed": False,
    },
    "CS202": {
        "title": "Operating Systems",
        "seats": 0,
        "fee": 550.0,
        "is_closed": True,
    },
    "CS303": {
        "title": "Compiler Design",
        "seats": 4,
        "fee": 600.0,
        "is_closed": False,
    },
}

TOTAL_TUITION = 0.0


def enroll_student(
    course_id,
    student_name,
    credits_registered=3,
    audit_trail=None,
):
    """Enroll a student in an available course."""
    global TOTAL_TUITION

    if audit_trail is None:
        audit_trail = []

    if course_id not in courses or courses[course_id]["is_closed"]:
        return False

    courses[course_id]["seats"] -= 1

    if courses[course_id]["seats"] <= 0:
        courses[course_id]["is_closed"] = True

    TOTAL_TUITION += courses[course_id]["fee"]

    audit_trail.append(
        f"Enrolled student {student_name} in course "
        f"{course_id} with {credits_registered} credits successfully"
    )

    return True


def drop_course(course_id):
    """Drop a course and restore its available seat."""
    try:
        courses[course_id]["seats"] += 1
        courses[course_id]["is_closed"] = False
    except KeyError:
        return False

    return True


def check_course_status(course_id):
    """Check whether a course is open for enrollment."""
    if courses.get(course_id) is None:
        return False

    return not courses[course_id]["is_closed"]


def calculate_scholarship_tuition(course_id, discount_percent):
    """Calculate tuition after applying a scholarship discount."""
    if course_id not in courses:
        raise ValueError("Invalid course ID.")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    base_fee = courses[course_id]["fee"]

    return base_fee * (1 - discount_percent / 100)


def generate_student_hash(roll_no):
    """Generate a secure SHA-256 student hash."""
    return hashlib.sha256(roll_no.encode()).hexdigest()


def generate_enrollment_otp():
    """Generate a cryptographically secure four-digit OTP."""
    return 1000 + secrets.randbelow(9000)


def export_course_roster(filename="course_roster.txt"):
    """Export course information to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(courses))

    print(f"Course roster exported to: {filename}")


def get_open_courses_summary(course_catalog):
    """Count all courses currently open for enrollment."""
    count = 0

    for details in course_catalog.values():
        if not details["is_closed"]:
            count += 1

    return count


def main():
    """Run the course enrollment system demonstration."""
    registrar_auth_token = os.environ.get(
        "REGISTRAR_AUTH_TOKEN",
        "",
    )

    enroll_student("CS101", "Kritika", 4)
    drop_course("CS202")

    print("Is CS101 open:", check_course_status("CS101"))

    print(
        "Scholarship Fee:",
        calculate_scholarship_tuition("CS303", 25),
    )

    print("Student Hash:", generate_student_hash("REG_2026_091"))
    print("Enrollment OTP:", generate_enrollment_otp())

    export_course_roster()

    print("Open courses:", get_open_courses_summary(courses))
    print("Registrar Token configured:", bool(registrar_auth_token))


if __name__ == "__main__":
    main()
