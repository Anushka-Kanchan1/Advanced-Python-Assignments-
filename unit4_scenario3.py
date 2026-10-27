import numpy as np
import pandas as pd

# Create a NumPy array of mobile prices
prices = np.array([15000, 25000, 35000, 45000, 20000, 55000, 30000])

# Calculate statistics
print("Mean Price:", np.mean(prices))
print("Median Price:", np.median(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))

# Create a Pandas DataFrame
data = {
    'Mobile': ['Samsung', 'Vivo', 'iPhone', 'OnePlus',
               'Oppo', 'Google Pixel', 'Realme'],
    'Price': prices
}

df = pd.DataFrame(data)

print("\nMobile Price DataFrame:")
print(df)

# Display mobiles costing more than Rs. 30,000
print("\nMobiles costing more than Rs. 30,000:")
print(df[df['Price'] > 30000])
