import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Titanic dataset
data = pd.read_csv("Titanic-Dataset.csv")

# Task 1
# User input for column containing numeric values
numeric_column = input("Enter the column name containing numeric values: ")

# Find the maximum and minimum values
max_value = data[numeric_column].max()
min_value = data[numeric_column].min()

print("Maximum value:", max_value)
print("Minimum value:", min_value)

# Calculate the average value
average_value = data[numeric_column].mean()
print("Average value:", average_value)

# Calculate the percentage difference
percentage_difference = ((max_value - average_value) / average_value) * 100
print("Percentage difference between average and maximum value:", percentage_difference)

# Calculate normalized column
normalized_column = ((data[numeric_column] - min_value) / (max_value - min_value)).round(4)

# Update the original DataFrame with the normalized column
data[numeric_column] = normalized_column

# Save the updated DataFrame back to the CSV file
data.to_csv("Titanic-Dataset.csv", index=False)

# Find numeric columns for correlation calculation
numeric_columns = data.select_dtypes(include=[np.number]).columns

# Calculate correlation matrix
correlation_matrix = data[numeric_columns].corr()

# Find columns with maximum positive and negative correlation
# Skripta računa koeficijente korelacije za sve parove numeričkih kolona u skupu podataka. Na kraju vraća kolone između kojih postoji najveće pozitivno i negativno poklapanje vrijednosti
max_positive_corr = correlation_matrix[numeric_column].nlargest(2).index[1]
max_negative_corr = correlation_matrix[numeric_column].nsmallest(1).index[0]

print("Column with maximum positive correlation:", max_positive_corr)
print("Column with maximum negative correlation:", max_negative_corr)

# Calculate standard deviation and plot distribution
std_dev = data[numeric_column].std()
print("Standard deviation:", std_dev)

plt.hist(data[numeric_column], bins=20, color='skyblue', edgecolor='black')
plt.xlabel(numeric_column)
plt.ylabel('Frequency')
plt.title('Distribution of ' + numeric_column)
plt.show()
