def categorize_patient(gender, age):
    if age < 0:
        return "Invalid Age"

    if gender in {"f", "female", "woman"}:
        gender = "F"
    elif gender in {"m", "male", "man"}:
        gender = "M"

    if gender not in {"F", "M"}:
        return "Invalid Gender"

    if age < 18:
        return "Child"

    if gender == "F":
        if 18 <= age <= 25:
            return "Young Adult (F)"
        elif 26 <= age <= 65:
            return "Adult (F)"
        else:
            return "Senior (F)"
    else:
        if 18 <= age <= 30:
            return "Young Adult (M)"
        elif 31 <= age <= 59:
            return "Adult (M)"
        else:
            return "Senior (M)"
