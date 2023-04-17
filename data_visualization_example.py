#Import Pandas and Matplotlib
import pandas as pd
import matplotlib.pyplot as plt

#Read the data from "employee_performance.csv"
data = pd.read_csv("C:/Users/hamit.koculu/Desktop/employee_performance.csv")

#Check the dataset
'''print(data.head())'''

#Use the .value_counts() function to determine the number of people in the different categories
educational_level = data["Education"].value_counts()

#Display the result
'''print(educational_level)'''

#Create a pie chart with the labels "Collage", "High School", "University"
'''plt.pie(educational_level, labels = educational_level.index)'''

#Display the result
'''plt.show()'''

#Create a bar chart with the names on the x-axis and the revenue values on the y-axis
'''plt.bar(data["Name"], data["Revenue"])'''

#Display the result
'''plt.show()'''

#Create a bar chart with the data "Revenue" and "Number of Calls"
plt.bar(data["Name"], data["Revenue"], label = "Revenues")
plt.bar(data["Name"], data["Number of Calls"], label = "Number of calls")

#Add a legend
plt.legend()

#Add grid lines 
plt.grid()

#Display the result
plt.show()