import employee_info as employ

def test_employee_age():

    inputrangelower = 20
    inputrangeupper = 30

    result = employ.get_employees_by_age_range(inputrangelower, inputrangeupper)

    assert (len(result) == 2)

def test_avg_salary():

    result = employ.calculate_average_salary()

    assert (result == 361000 / 6)

def test_employees_dept():

    inputdept = "Sales"

    result = employ.get_employees_by_dept(inputdept)

    assert (len(result) == 2)