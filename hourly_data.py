import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('D:/Internship_Tasks/Coders_Cave_Task/Phase 2/Climate data Analysis - Task 1/dataset/hourly_data.csv') 
data.dropna(inplace=True)
print(data.describe())

plt.figure(figsize=(10, 6))
sns.histplot(data['HourlyDryBulbTemperature'].astype(str), bins=20, kde=True) 
plt.title('Hourly Temperature Distribution')
plt.xlabel('Temperature (°F)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data['HourlyPrecipitation'].astype(str), bins=20, kde=True)  
plt.title('Hourly Precipitation Distribution')
plt.xlabel('Precipitation (inches)')
plt.ylabel('Frequency')
plt.show()

correlation_matrix = data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(data['DATE'], data['HourlyDryBulbTemperature'])
plt.title('Hourly Temperature Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.xticks(rotation=45)
plt.show()

