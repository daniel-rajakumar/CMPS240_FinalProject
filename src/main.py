import pandas as pd
import matplotlib.pyplot as plt

# get data from url
data_url = "https://raw.githubusercontent.com/daniel-rajakumar/CMPS240_FinalProject/main/res/iPhone.csv"
sales_data = pd.read_csv(data_url)

# make year as Y-axis
sales_data.set_index('Year', inplace=True)

# growth rate
sales_data_growth = sales_data.pct_change() * 100  # Calculate percentage change

#######################
###### Plotting ######
######################

fig, ax1 = plt.subplots(figsize=(10, 6))  # Create a figure and axes
ax2 = ax1.twinx()  # Create a second y-axis sharing the same x-axis

# set up plot for sale
for column in sales_data.columns:
    ax1.plot(sales_data.index, sales_data[column], label=f'{column} Sales', linestyle='-', marker='o')

# set up plot for growth rage
for column in sales_data_growth.columns:
    ax2.plot(sales_data_growth.index, sales_data_growth[column], label=f'{column} Growth Rate', linestyle='--', marker='x')

# Set labels and title for the plot
ax1.set_xlabel('Year')
ax1.set_ylabel('iPhone Sales')
ax2.set_ylabel('Growth Rate (%)')
ax1.set_title('iPhone Sales and Growth Rate in Different Regions Over Time')

# Show legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

note_text = "Average Growth Rate for Each Region:"
for region, growth_rate in sales_data_growth.items():
    note_text += f"\n{region}: {growth_rate.mean():.2}%"

plt.annotate(note_text, xy=(0.5, -0.3), xycoords='axes fraction', ha='center', fontsize=10, color='gray', wrap=True)


# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show()

