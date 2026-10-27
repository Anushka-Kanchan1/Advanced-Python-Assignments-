import numpy as np
import pandas as pd

# Create a NumPy array of product prices
prices = np.array([50, 100, 200, 150, 80])

# Calculate statistics
print("Mean Price:", np.mean(prices))
print("Median Price:", np.median(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))

# Create a Pandas DataFrame
data = {
    'Item': ['Rice', 'Sugar', 'Oil', 'Wheat', 'Milk'],
    'Price': prices,
    'Quantity': [5, 15, 8, 20, 6]
}

df = pd.DataFrame(data)

print("\nGrocery Store Data:")
print(df)

# Display items having quantity less than 10
print("\nItems with Quantity Less Than 10:")
print(df[df['Quantity'] < 10])
