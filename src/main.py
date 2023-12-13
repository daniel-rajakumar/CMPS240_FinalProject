import pandas as pd
import matplotlib.pyplot as plt

# Creating DataFrame from the data
sales_data = pd.read_csv("https://raw.githubusercontent.com/daniel-rajakumar/CMPS240_FinalProject/main/iPhone.csv")

# Set 'Year' column as the index of the DataFrame
sales_data.set_index('Year', inplace=True)

# Plotting the data
# plt.figure(figsize=(1, 1))  # Set the figure size

# Plot for each region
for column in sales_data.columns:
    plt.plot(sales_data.index, sales_data[column], label=column)

# Set plot labels and title
plt.xlabel('Year')
plt.ylabel('iPhone Sales')
plt.title('iPhone Sales in Different Regions Over 5 Years')
plt.legend()  # Show legend

# Show plot
plt.grid(True)  # Add gridlines
plt.tight_layout()  # Adjust layout
plt.show()
