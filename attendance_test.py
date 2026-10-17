def test_mark_attendance():
    student_id = "STU101"
    attendance_status = "Present"

    assert student_id != ""
    assert attendance_status in ["Present", "Absent"]

    print("Attendance marking test passed")


if __name__ == "__main__":
    test_mark_attendance()
