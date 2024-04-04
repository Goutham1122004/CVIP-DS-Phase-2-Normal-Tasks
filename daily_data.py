import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('D:/Internship_Tasks/Coders_Cave_Task/Phase 2/Climate data Analysis - Task 1/dataset/daily_data.csv')  

data['DATE'] = pd.to_datetime(data['DATE'])
data.dropna(inplace=True)
data['DailyPrecipitation'] = pd.to_numeric(data['DailyPrecipitation'], errors='coerce')
data.dropna(subset=['DailyPrecipitation'], inplace=True) 
print(data.describe())

plt.figure(figsize=(12, 6))
sns.lineplot(x='DATE', y='DailyAverageDryBulbTemperature', data=data)
plt.title('Temperature Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.xticks(rotation=45)
plt.show()

data['Month'] = data['DATE'].dt.month
monthly_precipitation = data.groupby('Month')['DailyPrecipitation'].sum()

plt.figure(figsize=(10, 6))
monthly_precipitation.plot(kind='bar', color='blue')
plt.title('Monthly Precipitation Analysis')
plt.xlabel('Month')
plt.ylabel('Total Precipitation (inches)')
plt.xticks(rotation=0)
plt.show()

