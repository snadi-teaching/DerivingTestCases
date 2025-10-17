import pytest
from patient.categorize_patient import categorize_patient


@pytest.mark.parametrize(
    "case_id, gender, age, expected",
    [
        ("TC1", "F", -10, "Invalid Age"),
        ("TC2", "U", 5, "Invalid Gender"),
        ("TC3", "F", 10, "Child"),
        ("TC4", "F", 20, "Young Adult (F)"),
        ("TC5", "F", 35, "Adult (F)"),
        ("TC6", "F", 66, "Senior (F)"),
        ("TC7", "M", 20, "Young Adult (M)"),
        ("TC8", "M", 35, "Adult (M)"),
        ("TC9", "M", 66, "Senior (M)"),
    ],
    ids=lambda x: x,
)
def test_patients(case_id, gender, age, expected):
    assert categorize_patient(gender, age) == expected
