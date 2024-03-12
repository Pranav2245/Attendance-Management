import pandas as pd
import matplotlib.pyplot as plt

def read_attendance_data(file_path):
    data = pd.read_csv(file_path)
    return data

def analyze_attendance_data(data):
    total_students = len(data)

    present_count = data['Status'].value_counts()['Present']
    absent_count = data['Status'].value_counts()['Absent']

    attendance_percentage = present_count / total_students * 100

    return {
        'total_students': total_students,
        'present_count': present_count,
        'absent_count': absent_count,
        'attendance_percentage': attendance_percentage
    }

def visualize_attendance_data(data):
    data['Status'].value_counts().plot(kind='bar')
    plt.title('Attendance Status')
    plt.xlabel('Status')
    plt.ylabel('Count')
    plt.show()

def write_attendance_data_to_csv(data, file_name):
    data.to_csv(file_name, index=False)

if __name__ == "__main__":
    file_path = input("Enter the path of the attendance CSV file: ")
    attendance_data = read_attendance_data(file_path)

    analysis_results = analyze_attendance_data(attendance_data)
    print("\nAttendance Analysis:")
    print(f"Total Students: {analysis_results['total_students']}")
    print(f"Present: {analysis_results['present_count']}")
    print(f"Absent: {analysis_results['absent_count']}")
    print(f"Attendance Percentage: {analysis_results['attendance_percentage']:.2f}%")

    visualize_attendance_data(attendance_data)

    new_file_name = input("Enter the name of the output CSV file: ")
    write_attendance_data_to_csv(attendance_data, new_file_name)
    print(f"Attendance data has been saved to {new_file_name}")
