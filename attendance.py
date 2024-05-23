import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('attendance.csv')

# Convert percentage strings to float values
months = ['Jan', 'Feb', 'March', 'Apr', 'May']
for month in months:
    data[month] = data[month].str.rstrip('%').astype('float') / 100

# Calculate monthly average percentages
data['Avg'] = (data[months].mean(axis=1))*100

# Print monthly average percentages
print("Monthly Average Percentages:")
print(data[['SAP ID','ROLL ID', 'NAME', 'Avg']])
#Storing data into new csv file
data[['SAP ID', 'ROLL ID', 'NAME', 'Avg']].to_csv('attendance_avg.csv', index=False)
 
# Data visualization (bar graph)
avg_percentage = data[months].mean()
plt.figure(figsize=(10, 6))
plt.bar(months, avg_percentage, color='skyblue')
plt.title('Monthly Performance Average')
plt.xlabel('Month')
plt.ylabel('Average Percentage')
plt.ylim(0,1)  # Set y-axis limit to be percentage (0 to 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Check if any student's average is below 75%
for index, row in data.iterrows():
    if row['Avg'] < 75:
        print(row['SAP ID'], row['ROLL ID'], row['NAME'], row['Avg'], "will not be able to sit in the examination")
    else:
        print("All the Best for Your Examination")
