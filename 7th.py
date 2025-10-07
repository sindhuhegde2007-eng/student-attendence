def calculate_attendance_percentage(classes_held, classes_attended):
    if classes_held == 0:
        return 0.0
    return (classes_attended / classes_held) * 100

def main():
    try:
        classes_held = int(input("Enter the total number of classes held: "))
        classes_attended = int(input("Enter the number of classes attended: "))

        if classes_held < 0 or classes_attended < 0:
            print("Error: Number of classes cannot be negative.")
        elif classes_attended > classes_held:
            print("Error: Attended classes cannot exceed total classes held.")
        else:
            percentage = calculate_attendance_percentage(classes_held, classes_attended)
            print(f"\n📊 Attendance Summary:")
            print(f"   Classes Held     : {classes_held}")
            print(f"   Classes Attended : {classes_attended}")
            print(f"   Attendance       : {percentage:.2f}%")

            if percentage < 75:
                print("⚠️ Warning: Attendance below 75%. You may not be eligible for exams.")
            else:
                print("✅ Good job! Your attendance meets the requirement.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()
