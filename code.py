import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel(r'C:\Users\naman\Contacts\Desktop\code\Internship\Python Intern\sales data\sales_data.xlsx')

# Group by Region and sum the Sale_amt
sales_by_region = df.groupby('Region')['Sale_amt'].sum()

# Print the grouped sales sum
print(sales_by_region)

# Plot total sales by region
sales_by_region.plot(kind='bar', title='Total Sales Amount by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales Amount')
plt.show()
