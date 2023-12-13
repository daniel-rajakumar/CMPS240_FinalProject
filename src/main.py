import pandas as pd
import matplotlib.pyplot as plt

# load data from remote csv
url = "https://raw.githubusercontent.com/daniel-rajakumar/CMPS240_FinalProject/main/res/iPhone.csv"
sales_data = pd.read_csv(url)

# Calculate growth rates for each region
regions = sales_data.columns[1:]  # remove Year
growth_data = pd.DataFrame()  
for region in regions:
    growth_data[region] = sales_data[region].pct_change() * 100

# set 'Year' column as index
sales_data.set_index('Year', inplace=True)

# Bar chart for sales data
plt.subplot(1, 2, 1)  # relocate the chart
sales_data[regions].plot(kind='bar', ax=plt.gca())
plt.title('iPhone Sales in Different Regions Over 5 Years')
plt.xlabel('Year')
plt.ylabel('Sales (mm)')

# add avg sale (%) for each region on bottom of sale graph
note_text = "Average Growth Rate for Each Region:"
for region, sales_rate in sales_data.items():
    note_text += f"\n{region}: {sales_rate.mean():.4}%"
plt.annotate(note_text, xy=(0.5, -0.3), xycoords='axes fraction', ha='center', fontsize=10, color='gray', wrap=True)

# Bar chart for growth rates
plt.subplot(1, 2, 2)  # relocate the chart
growth_data.plot(kind='bar', ax=plt.gca())
plt.title('iPhone Sales Growth Rate in Different Regions Over 5 Years')
plt.xlabel('Year')
plt.ylabel('Growth Rate (%)')

# add avg growth rate (%) for each region on bottom of growth graph
note_text = "Average Growth Rate for Each Region:"
for region, sales_rate in growth_data.items():
    note_text += f"\n{region.replace(' ', ' ')}: {sales_rate.mean():.3}%"
plt.annotate(note_text, xy=(0.5, -0.3), xycoords='axes fraction', ha='center', fontsize=10, color='gray', wrap=True)


# Show plot
plt.tight_layout()  # Adjust layout
plt.show()
