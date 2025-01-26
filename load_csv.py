import pandas as pd  # Import Pandas library
import matplotlib.pyplot as plt


# File path
file_path = r"C:\Users\Priya\Documents\CODEXINTERN Internship Works\student.csv"

# Load the CSV file
try:
    data = pd.read_csv(file_path)  # Load the CSV into a DataFrame
    print("File loaded successfully!")
    print(data.head())  # Display the first few rows of the data
except FileNotFoundError:
    print("The file was not found. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")

# Calculate the average of the "Score" column
average_score = data["Score"].mean()
print(f"The average score is: {average_score}")

# Create a bar chart for scores
plt.bar(data["Name"], data["Score"], color='skyblue')
plt.title("Scores of Students")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()

# Create a scatter plot for Age vs. Score
plt.scatter(data["Age"], data["Score"], color='green', marker='o')
plt.title("Age vs. Score")
plt.xlabel("Age")
plt.ylabel("Score")
plt.show()

# Create a heatmap for correlation between columns
numeric_data = data.select_dtypes(include=[float, int])  # Select only numeric columns
correlation = numeric_data.corr()  # Compute the correlation matrix

plt.imshow(correlation, cmap="coolwarm", interpolation="none")
plt.colorbar()  # Add a color bar
plt.xticks(range(len(correlation)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation)), correlation.columns)
plt.title("Correlation Heatmap")
plt.show()
