```
#import necessary packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

```
# Read the CSV file
df = pd.read_csv("Titanic.csv")

#print the data
print(df)
```

```
                                               Name PClass    Age     Sex  Survived
0                      Allen, Miss Elisabeth Walton    1st  29.00  female         1
1                       Allison, Miss Helen Loraine    1st   2.00  female         0
2               Allison, Mr Hudson Joshua Creighton    1st  30.00    male         0
3     Allison, Mrs Hudson JC (Bessie Waldo Daniels)    1st  25.00  female         0
4                     Allison, Master Hudson Trevor    1st   0.92    male         1
...                                             ...    ...    ...     ...       ...
1308                             Zakarian, Mr Artun    3rd  27.00    male         0
1309                         Zakarian, Mr Maprieder    3rd  26.00    male         0
1310                               Zenni, Mr Philip    3rd  22.00    male         0
1311                               Lievens, Mr Rene    3rd  24.00    male         0
1312                                 Zimmerman, Leo    3rd  29.00    male         0

[1313 rows x 5 columns]
```

```
# Display the first few rows of the dataset
print(df.head())
```
```
                                            Name PClass    Age     Sex  Survived
0                   Allen, Miss Elisabeth Walton    1st  29.00  female         1
1                    Allison, Miss Helen Loraine    1st   2.00  female         0
2            Allison, Mr Hudson Joshua Creighton    1st  30.00    male         0
3  Allison, Mrs Hudson JC (Bessie Waldo Daniels)    1st  25.00  female         0
4                  Allison, Master Hudson Trevor    1st   0.92    male         1
```

```
# Summary statistics
print(df.describe())
```
```
              Age     Survived
count  756.000000  1313.000000
mean    30.397989     0.342727
std     14.259049     0.474802
min      0.170000     0.000000
25%     21.000000     0.000000
50%     28.000000     0.000000
75%     39.000000     1.000000
max     71.000000     1.000000
```

```
# Check for missing values
print(df.isnull().sum())
```
```
Name          0
PClass        1
Age         557
Sex           0
Survived      0
dtype: int64
```

```
# Distribution of survival
sns.countplot(x='Survived', data=df)
plt.title('Survival Distribution')
plt.show()
```
![survival distribution](https://github.com/Rajkumar062003/Titanic_Dataset/blob/main/Output/1.Distribution_of_survival.jpeg)

```
# Survival by passenger class
sns.countplot(x='PClass', hue='Survived', data=df)
plt.title('Survival by Passenger Class')
plt.show()
```
![survival by passenger class](https://github.com/Rajkumar062003/Titanic_Dataset/blob/main/Output/2.Survival_by_passenger_class.jpeg)

```
# Survival by gender
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival by Gender')
plt.show()
```
![Survival by gender](https://github.com/Rajkumar062003/Titanic_Dataset/blob/main/Output/3.Survival_by_gender.jpeg)

```
# Age distribution
sns.histplot(df['Age'].dropna(), bins=20, kde=True)
plt.title('Age Distribution')
plt.show()
```
![age Distribution](https://github.com/Rajkumar062003/Titanic_Dataset/blob/main/Output/4.Age_distribution.jpeg)