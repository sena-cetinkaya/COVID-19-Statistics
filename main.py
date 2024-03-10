import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from shapely.geometry import Point

# Read the data
data = pd.read_csv("/kaggle/input/covid-19-global-statistics-dataset/COVID-19 Global Statistics Dataset.csv")

#  Display the first few rows of the data
print(data.head())

#  Learning columns
print(data.columns)

# Learning the size of the dataset
print(data.shape)

# Data types of columns
print(data.dtypes)

# Check for missing values
print(data.isnull().sum())

# Summary statistics
print(data.describe())

# DATA VISUALIZATION

# Bar plot for "Total Cases"

# Convert 'Total Cases' to numeric.
data['Total Cases'] = pd.to_numeric(data['Total Cases'], errors='coerce')

# Drop rows with missing 'Total Cases' values.
data.dropna(subset=['Total Cases'], inplace=True)

# Sort the dataframe by 'Total Cases' and select top 10 countries
top_ten_countries = data.sort_values(by='Total Cases', ascending=False).head(10)
print(top_ten_countries)

# Create a bar plot of total cases by country
plt.figure(figsize=(12, 6))
sns.barplot(x='Total Cases', y='Country', data=top_ten_countries)
plt.title('Top 10 Countries by Total Cases')
plt.xlabel('Total Cases')
plt.ylabel('Country')
plt.show()

# Pie chart for "Total Deaths"

# Convert 'Total Deaths' to numeric
data['Total Deaths'] = pd.to_numeric(data['Total Deaths'], errors='coerce')

# Drop rows with missing 'Total Deaths' values
data.dropna(subset=['Total Deaths'], inplace=True)

# Sort the dataframe by 'Total Deaths' and select top 10 countries
top_ten_countries_deaths = data.sort_values(by='Total Deaths', ascending=False).head(10)

# Create a pie chart to show the distribution of COVID-19 deaths among the top countries
plt.figure(figsize=(8, 8))
plt.pie(top_ten_countries_deaths['Total Deaths'], labels=top_ten_countries_deaths['Country'], autopct='%1.1f%%', startangle=140)
plt.title('Distribution of COVID-19 Deaths Among Top 10 Countries')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# World Map for COVID-19 global statistics

# Load world map data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Load your CSV data
data = pd.read_csv("/kaggle/input/covid-19-global-statistics-dataset/COVID-19 Global Statistics Dataset.csv")

# Merge the world map with your CSV data
merged_data = world.merge(data, how='left', left_on='name', right_on='Country')

# Plot the merged data
merged_data.plot(column='Total Cases', cmap='OrRd', linewidth=0.8, edgecolor='0.8', legend=True)
plt.title('Total COVID-19 Cases by Country')
plt.show()
