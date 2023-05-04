import Lab2.bmi as bmi

def test_bmi_normal_weight():
    height = 1.7
    weight = 57

    result = bmi.calculate_bmi(height, weight)

    assert (result == 0)

def test_bmi_over_weight():
    height = 1.7
    weight = 80

    result = bmi.calculate_bmi(height, weight)

    assert (result == 1)

def test_bmi_under_weight():
    height = 1.7
    weight = 45

    result = bmi.calculate_bmi(height, weight)

    assert (result == -1)