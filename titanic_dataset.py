import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("Titanic.csv")

#print the data
print(df)

# Display the first few rows of the dataset
print(df.head())

# Summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Distribution of survival
sns.countplot(x='Survived', data=df)
plt.title('Survival Distribution')
plt.show()

# Survival by passenger class
sns.countplot(x='PClass', hue='Survived', data=df)
plt.title('Survival by Passenger Class')
plt.show()

# Survival by gender
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival by Gender')
plt.show()

# Age distribution
sns.histplot(df['Age'].dropna(), bins=20, kde=True)
plt.title('Age Distribution')
plt.show()