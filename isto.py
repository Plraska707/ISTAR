import pandas as pd
import matplotlib.pyplot as plt


file='Ethiopia_1997-2023_May26.xlsx'

df = pd.read_excel(file)

df=df[df.YEAR>=2018]

df=df[df.ADMIN2=='Mekelle Tigray']

grouped_counts = df.groupby(['YEAR', 'NOTES']).size().unstack()

# Plot the grouped counts
grouped_counts.plot(kind='bar', stacked=True)

# Set axis labels
plt.xlabel('Year')
plt.ylabel('Count')

# Set legend
plt.legend(title='Notes')

# Display the plot
plt.show()