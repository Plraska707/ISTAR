import pandas as pd
import matplotlib.pyplot as plt


file='Ethiopia_1997-2023_May26.xlsx'

df = pd.read_excel(file)


df=df[df.YEAR>=2018]
#colonne=[df.columns]

df=df[df.ADMIN2=='Mekelle Tigray']
#print(df.head())
#print(colonne)
#df['DISORDER_TYPE'].value_counts().plot.barh()
grouped_sum = df.groupby('YEAR')['FATALITIES'].count()

# Plot the grouped sums
grouped_sum.plot(kind='line')

#plt.plot(x=YEAR, y=event_count)
# Set axis labels
plt.xlabel('Year')
plt.ylabel('Number of Disorder events')

# Set legend
#plt.legend(title='FATALITIES')
plt.legend()

# Display the plot
plt.show()

#grouped_counts = df.groupby('DISORDER_TYPE')['YEAR']

#events_by_year = df.groupby(df.YEAR)[df.DISORDER_TYPE].value_counts
#events_by_year.plot.bar()

# Create a bar plot
#events_by_year.plot.bar()

#df.plot(x="YEAR", y=grouped_counts)
#plt.title("DISORDER_TYPE")
#plt.ylabel("Billions of $")
#plt.gca().invert_xaxis()

#plt.show()