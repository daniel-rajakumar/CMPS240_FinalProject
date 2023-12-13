# import pandas as pd
# import matplotlib.pyplot as plt

# # Creating DataFrame from the cvs data
# sales_data = pd.read_csv("https://raw.githubusercontent.com/daniel-rajakumar/CMPS240_FinalProject/main/res/iPhone.csv")

# # Set 'Year' column as the index of the DataFrame
# sales_data.set_index('Year', inplace=True)

# # Plot for each region
# for column in sales_data.columns:
#     plt.plot(sales_data.index, sales_data[column], label=column)

#   # Calculate growth rate for each region
# growth_data = sales_data.pct_change() * 100  # Calculate percentage change as growth rate


# # Set plot labels and title
# plt.xlabel('Year')
# plt.ylabel('iPhone Sales')
# plt.title('iPhone Sales in Different Regions Over 5 Years')
# plt.legend()  # Show legend

# # Show plot
# plt.grid(True)  # Add gridlines
# plt.tight_layout()  # Adjust layout
# plt.show()




import pandas as pd
import matplotlib.pyplot as plt

# Creating sample sales data (Replace this with your actual data)
data = {
    'Year': [2019, 2020, 2021, 2022, 2023],
    'Region_A': [5000, 6000, 7000, 8000, 7500],
    'Region_B': [4500, 5500, 6500, 7500, 7000],
    'Region_C': [4000, 5000, 6000, 7000, 6500]
}

# Creating DataFrame from the data
# sales_data = pd.DataFrame(data)

sales_data = pd.read_csv("https://raw.githubusercontent.com/daniel-rajakumar/CMPS240_FinalProject/main/res/iPhone.csv")

# Set 'Year' column as the index of the DataFrame
sales_data.set_index('Year', inplace=True)

# Calculate growth rate for each region
growth_data = sales_data.pct_change() * 100  # Calculate percentage change as growth rate

# Plotting the data and growth rate
fig, ax1 = plt.subplots(figsize=(10, 6))  # Set the figure size

# Plot for each region
for column in sales_data.columns:
    ax1.plot(sales_data.index, sales_data[column], label=f'{column} Sales')

ax2 = ax1.twinx()  # Create a second y-axis for growth rate
for column in growth_data.columns:
    ax2.plot(growth_data.index, growth_data[column], linestyle='--', label=f'{column} Growth Rate')

# Set plot labels and title
ax1.set_xlabel('Year')
ax1.set_ylabel('iPhone Sales')
ax2.set_ylabel('Growth Rate (%)')
plt.title('iPhone Sales and Growth Rate in Different Regions Over 5 Years')
fig.tight_layout()

# Combine legends from both axes
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax2.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper right')

# Show plot
plt.grid(True)  # Add gridlines
plt.show()

