import pandas as pd
import matplotlib.pyplot as plt


file='Ethiopia_1997-2023_May26.xlsx'

df = pd.read_excel(file)

df=df[df.YEAR>=2018]

df=df[df.ADMIN2=='Mekelle Tigray']

grouped_percentages = df.groupby(['YEAR', 'EVENT_TYPE']).size() / df.groupby('YEAR').size() * 100

# Plot the grouped percentages as a pie chart
grouped_percentages.unstack().plot(kind='pie', subplots=True, layout=(2,3), figsize=(16, 8), autopct='%1.1f%%')

# Set aspect ratio to be equal so that pie is drawn as a circle
plt.axis('equal')

# Set legend
plt.legend(title='Disorder Type')

# Display the plot
plt.show()