import pandas as pd


def get_dataset():
    """get dataset in different formats csv,json"""
    marks = pd.read_csv("Exercise2/dataset/marks.csv")
    engagement = pd.read_json("Exercise2/dataset/engagement.json")
    bio = pd.read_excel("Exercise2/dataset/bio.xlsx", sheet_name="Sheet1").astype(
        {"id": "int"}
    )
    return marks, engagement, bio


def main():
    """Calculate overall scenarios"""
    marks, engagement, bio = get_dataset()

    # Merge data from different dataset
    student_data = bio.merge(marks, how="left", on="id")
    student_data = student_data.merge(engagement, how="left", on="id")

    # Generate height information based on gender
    height_by_gender = student_data.groupby("Gender").aggregate(
        {"Height": ["min", "mean", "max"]}
    )
    print("Height Information based on Gender")
    print(height_by_gender)

    # Generate Weight Information based on Gender
    weight_by_gender = student_data.groupby("Gender").aggregate(
        {"Weight": ["min", "mean", "max"]}
    )
    print("Weight Information based on Gender")
    print(weight_by_gender)

    # Generate People count based on Gender
    gender_count = student_data.groupby(["Gender"])["Gender"].count()
    print("People count based on Gender")
    print(gender_count)

    # Generate Mean Marks Information based on Department
    avg_marks_by_dept = student_data.groupby("Department")[
        ["AI", "Math", "English"]
    ].aggregate("mean")
    print("Mean Marks Information based on Department")
    print(avg_marks_by_dept)

    # Generate People count based on sports involvement
    sports_status = student_data.groupby(["Sports"])["Sports"].count()
    print("People count based on sports Status")
    print(sports_status)

    # Generate People count based on sports involvement
    academic_level = student_data.groupby(["Education", "Communication"])[
        ["Gender"]
    ].count()
    print("People count based on academic and communication involvement")
    print(academic_level)


if __name__ == "__main__":
    main()
