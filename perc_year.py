import pandas as pd
import matplotlib.pyplot as plt


file='Ethiopia_1997-2023_May26.xlsx'

df = pd.read_excel(file)

df=df[df.YEAR==2023]

df=df[df.ADMIN2=='Mekelle Tigray']

grouped_percentages = df['EVENT_TYPE'].value_counts() / len(df) * 100

# Plot the pie chart
grouped_percentages.plot(kind='pie', autopct='%1.1f%%')

# Set title
plt.title('Event Types in 2023')

# Display the plot
plt.show()