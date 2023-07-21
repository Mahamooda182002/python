import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('dataset.csv')

# Display the first few rows of the dataset
print(data.head())

# Check the dimensions of the dataset
print('Number of rows:', data.shape[0])
print('Number of columns:', data.shape[1])

# Check the data types of each column
print(data.dtypes)

# Check for missing values
print('Missing values:', data.isnull().sum())

# Perform summary statistics
print(data.describe())

# Plot a histogram of a numerical variable
plt.hist(data['numeric_column'])
plt.xlabel('Numeric Column')
plt.ylabel('Frequency')
plt.title('Histogram of Numeric Column')
plt.show()

# Create a scatter plot of two numerical variables
plt.scatter(data['numeric_column1'], data['numeric_column2'])
plt.xlabel('Numeric Column 1')
plt.ylabel('Numeric Column 2')
plt.title('Scatter Plot')
plt.show()

# Create a bar plot of a categorical variable
plt.figure(figsize=(8, 6))
sns.countplot(data['categorical_column'])
plt.xlabel('Categories')
plt.ylabel('Count')
plt.title('Bar Plot of Categorical Column')
plt.xticks(rotation=45)
plt.show()

# Calculate correlations between numerical variables
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
