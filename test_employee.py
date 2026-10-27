from employee import employee_details

def test_employee_details():
    result = employee_details(
        "Rahul",
        "101",
        "CSE",
        50000
    )

    expected = (
        "Name: Rahul\n"
        "Employee ID: 101\n"
        "Department: CSE\n"
        "Salary: 50000"
    )

    assert result == expected
    