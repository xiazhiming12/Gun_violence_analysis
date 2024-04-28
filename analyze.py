# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 02:18:46 2024

@author: 夏之茗
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Victims.csv")

df['DATE'] = pd.to_datetime(df['DATE'])
df['YEAR'] = df['DATE'].dt.year
df['MONTH'] = df['DATE'].dt.month
df['DAY'] = df['DATE'].dt.day
grouped_by_year = df.groupby('YEAR').size().reset_index(name='incident_count')
plt.figure(figsize=(10, 6))
plt.bar(grouped_by_year['YEAR'], grouped_by_year['incident_count'], color='skyblue')
plt.xlabel('Year')
plt.ylabel('Incident Count')
plt.title('Incidents by Year')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

grouped_by_year_incident = df.groupby(['YEAR', 'VICTIMIZATION_PRIMARY']).size().unstack(fill_value=0)
grouped_by_year_incident['TOTAL'] = grouped_by_year_incident.sum(axis=1)
grouped_by_year_incident['HOMICIDE_PROPORTION'] = grouped_by_year_incident['HOMICIDE'] / grouped_by_year_incident['TOTAL']
grouped_by_year_incident['BATTERY_PROPORTION'] = grouped_by_year_incident['BATTERY'] / grouped_by_year_incident['TOTAL']
plt.figure(figsize=(10, 6))
plt.plot(grouped_by_year_incident.index, grouped_by_year_incident['HOMICIDE_PROPORTION'], marker='o', label='Homicide')
plt.plot(grouped_by_year_incident.index, grouped_by_year_incident['BATTERY_PROPORTION'], marker='o', label='Battery')
plt.xlabel('Year')
plt.ylabel('Proportion')
plt.title('Proportion of Homicide and Battery Incidents by Year')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(grouped_by_year_incident.index, rotation=45)
plt.tight_layout()
plt.show()

df = df[df['YEAR'] >= 2010]

print(df.info())

plt.hist(df['AGE'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Victims'' Ages')
plt.show()

grouped_data = df.groupby(['SEX', 'RACE', 'AGE']).size().reset_index(name='incident_count')
pivot_table = grouped_data.pivot_table(index='AGE', columns=['SEX', 'RACE'], values='incident_count', aggfunc='sum')
plt.figure(figsize=(14, 10))
sns.heatmap(pivot_table, cmap='viridis', linecolor='white', linewidth=1)
plt.xlabel('Sex & Race')
plt.ylabel('Age')
plt.title('Incidents Count by Sex, Race, and Age')
plt.tight_layout()
plt.show()