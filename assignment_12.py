import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample customer churn dataset
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Age': [25, 35, 45, np.nan, 30, 50, 40, 28],
    'MonthlyCharges': [500, 700, 800, 600, np.nan, 900, 750, 550],
    'Tenure': [2, 12, 24, 6, 18, 36, 10, 4],
    'Churn': ['Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

# Display the dataset
print("Original Dataset:")
print(df)

# 1. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 2. Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(
    df['MonthlyCharges'].mean()
)

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Generate summary statistics
print("\nSummary Statistics:")
print(df.describe())

# 5. Analyze churn
print("\nChurn Count:")
print(df['Churn'].value_counts())

# 6. Calculate average monthly charges using NumPy
charges = df['MonthlyCharges'].to_numpy()
print("\nAverage Monthly Charges:", np.mean(charges))
print("Maximum Monthly Charges:", np.max(charges))
print("Minimum Monthly Charges:", np.min(charges))

# 7. Visualize customer churn
df['Churn'].value_counts().plot(kind='bar')
plt.title('Customer Churn Analysis')
plt.xlabel('Churn')
plt.ylabel('Number of Customers')
plt.show()

# 8. Visualize monthly charges
plt.hist(df['MonthlyCharges'], bins=5)
plt.title('Monthly Charges Distribution')
plt.xlabel('Monthly Charges')
plt.ylabel('Number of Customers')
plt.show()

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df)
