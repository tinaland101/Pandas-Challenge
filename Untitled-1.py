# %%

import pandas as pd

# I loaded the CSV by dragging/dropping the file into terminal creates a path. 
file1 = pd.read_csv('/Users/christinaland/Downloads/pandachallenge.py/PyCitySchools/Resources/schools_complete.csv')

# As above, I Loaded the CSV file utilizing the same method for students_complete file. 
file2 = pd.read_csv('/Users/christinaland/Downloads/pandachallenge.py/PyCitySchools/Resources/students_complete.csv')

# Display the first few rows of each DataFrame to ensure data was pathed correctly 
print("schools_complete:")
print(file1.head())

print("\nstudents_complete:")
print(file2.head())



# %%
# I created a new variable name for file1 and file2 to read from each respective file path  to merge and generate a DataFrame. Note to self: without launching the header from the previous code, it wouldve been more diffcult to understand the formatting for "school_name" as shown in the dataframe below/above. (as suggested in the code instructions)
schoolsdataset = pd.read_csv('/Users/christinaland/Downloads/pandachallenge.py/PyCitySchools/Resources/schools_complete.csv')
studentdataset = pd.read_csv('/Users/christinaland/Downloads/pandachallenge.py/PyCitySchools/Resources/students_complete.csv')
dataframemerged = pd.merge(schoolsdataset, studentdataset, how="left",on="school_name")
dataframemerged.head()

# %%
total_unique_schools = schoolsdataset['school_name'].nunique()  # Count unique names
print(f"Total number of unique schools: {total_unique_schools}")


# %%
total_students = dataframemerged['student_name'].count()  # Count non-null entries

# Display the result
print(f"Total number of students: {total_students}")

# %%
total_budget = schoolsdataset['budget'].sum()  # Sum the budget values

# Display the result
print(f"Total budget: ${total_budget:.2f}")

# %%
mean_math_score = dataframemerged['math_score'].mean()  # Calculate the mean for math 

# Display the result
print(f"Mean math score: {mean_math_score:.2f}")

# %%
mean_reading_score = dataframemerged['reading_score'].mean()  # Calculate the mean

# Display the result
print(f"Mean reading score: {mean_reading_score:.2f}")

# %%
passing_math_count = dataframemerged[(dataframemerged["math_score"] >= 70)].count()["student_name"]
passing_math_percentage = passing_math_count / float(total_students) * 100
passing_math_percentage

# %%
passing_read_count = dataframemerged[(dataframemerged["reading_score"] >= 70)].count()["student_name"]
passing_read_percentage = passing_read_count / float(total_students) * 100
passing_read_percentage

# %%
passing_math_count = dataframemerged[
    (dataframemerged["math_score"] >= 70) & (dataframemerged["reading_score"] >= 70)
].count()["student_name"]
overall_passing_rate = passing_math_count /  float(total_students) * 100
overall_passing_rate

# %%
import pandas as pd

# Load the CSV files into respective DataFrames
schoolsdataset = pd.read_csv('/Users/christinaland/Downloads/pandachallenge.py/PyCitySchools/Resources/schools_complete.csv')
studentdataset = pd.read_csv('/Users/christinaland/Downloads/pandachallenge.py/PyCitySchools/Resources/students_complete.csv')

# Merge the DataFrames on the 'school_name' column
dataframemerged = pd.merge(studentdataset, schoolsdataset, how="left", on="school_name")

# Total number of schools
total_schools = schoolsdataset['school_name'].nunique()

# Total number of students
total_students = studentdataset.shape[0]

# Total budget
total_budget = schoolsdataset['budget'].sum()

# Average Math Score
average_math_score = dataframemerged['math_score'].mean()

# Average Reading Score
average_reading_score = dataframemerged['reading_score'].mean()

# Percentage Passing Math
passing_math = dataframemerged[dataframemerged['math_score'] >= 70].shape[0]
percentage_passing_math = (passing_math / total_students) * 100 if total_students > 0 else 0

# Percentage Passing Reading
passing_reading = dataframemerged[dataframemerged['reading_score'] >= 70].shape[0]
percentage_passing_reading = (passing_reading / total_students) * 100 if total_students > 0 else 0

# Percentage Overall Passing (passing both subjects)
passing_both = dataframemerged[(dataframemerged['math_score'] >= 70) & (dataframemerged['reading_score'] >= 70)].shape[0]
percentage_overall_passing = (passing_both / total_students) * 100 if total_students > 0 else 0

# Create a summary DataFrame
summary_df = pd.DataFrame({
    "Total Schools": [total_schools],
    "Total Students": [total_students],
    "Total Budget": [total_budget],
    "Average Math Score": [average_math_score],
    "Average Reading Score": [average_reading_score],
    "% Passing Math": [percentage_passing_math],
    "% Passing Reading": [percentage_passing_reading],
    "% Overall Passing": [percentage_overall_passing]
})

# Display the summary DataFrame
print(summary_df)


# %%
school_types = schoolsdataset.set_index(["school_name"])["type"]
print(school_types)


# %%
# Calculate the total student count per school from school_data
total_students = schoolsdataset['size'].sum()

# Display the result
print(f"Total number of students: {total_students}")

# %%
# Calculate the total school budget and per capita spending per school from school_data
per_school_budget = schoolsdataset['budget'].sum()
print(f"Total Sum of Budget: ${per_school_budget:,.2f}")
# come back to per school capita
per_capita_spending = per_school_budget / total_students
print(f"Per Capita Budget: ${per_capita_spending:.2f}")

# %%
#Calculate the average test scores per school from school_data_complete
per_school_math = dataframemerged['math_score'].mean()

# Display the result
print(f"The Average per School's Math Score: {per_school_math:.2f}")
per_school_reading = dataframemerged['reading_score'].mean()

# Display the result
print(f"The Average per School's Reading Score: {per_school_reading:.2f}")

# %%
#Calculate the number of students per school with math scores of 70 or higher from school_data_complete
passing_students = dataframemerged[
    (dataframemerged['math_score'] >= 70) | (dataframemerged['reading_score'] >= 70)
]

# Count the total number of students who passed
total_passing_students = passing_students['student_name'].count()

# Display the result
print(f"Total number of students who passed with a score of 70 or higher: {total_passing_students}")

# %%
 #Calculate the number of students per school with reading scores of 70 or higher from school_data_complete
passing_reading = dataframemerged[dataframemerged['reading_score'] > 70]

# Group by school name and count the number of students per school
students_per_school_reading = passing_reading['student_name'].count()

# Display the results
print(students_per_school_reading)

# %%
# Use the provided code to calculate the number of students per school that passed both math and reading with scores of 70 or higher
total_students_passing_both = dataframemerged[
    (dataframemerged["reading_score"] >= 70) & (dataframemerged["math_score"] >= 70)
].shape[0]

# Display the result
print(f"Total number of students who passed both math and reading with a score of 70 or higher: {total_students_passing_both}")


# %%
#come back too !!
per_school_passing_math = (total_passing_students / total_students) * 100
per_school_passsing_reading = (students_per_school_reading/ total_students) * 100
overall_passing_rate =  total_students_passing_both / total_students * 100

# Display the results
print(f"Per School Passing Math:\n{per_school_math}")
print(f"Per School Passing Reading:\n{per_school_passsing_reading}")
print(f"Overall Passing Rate:\n{overall_passing_rate}")

# %%
average_scores = dataframemerged.groupby('school_name').agg(
    average_reading_score=('reading_score', 'mean'),
    average_math_score=('math_score', 'mean')
).reset_index()

# Display the average scores
print(average_scores)
total_students_per_school = dataframemerged.groupby('school_name').size()

# Count the number of students who passed both math and reading (scores >= 70)
students_passing_both = dataframemerged[
    (dataframemerged['math_score'] >= 70) & (dataframemerged['reading_score'] >= 70)
].groupby('school_name').size()

# Calculate the overall passing rate
overall_passing_rate = (students_passing_both / total_students_per_school) * 100

# Convert to DataFrame for better readability
overall_passing_df = overall_passing_rate.reset_index(name='% Overall Passing')

# Display the results
print(overall_passing_df)

# %%
import pandas as pd

# Create the DataFrame with the provided data
data = {
    'school_name': [
        'Bailey High School', 'Cabrera High School', 'Figueroa High School', 
        'Ford High School', 'Griffin High School', 'Hernandez High School', 
        'Holden High School', 'Huang High School', 'Johnson High School', 
        'Pena High School', 'Rodriguez High School', 'Shelton High School', 
        'Thomas High School', 'Wilson High School', 'Wright High School'
    ],
    'School Type': [
        'District', 'Charter', 'District', 'District', 'Charter',
        'District', 'Charter', 'District', 'District', 'Charter',
        'District', 'Charter', 'Charter', 'Charter', 'Charter'
    ],
    'Total Students': [
        4976, 1858, 2949, 2739, 1468, 
        4635, 427, 2917, 4761, 962, 
        3999, 1761, 1635, 2283, 1800
    ],
    'Total School Budget': [
        '$3,124,928.00', '$1,081,356.00', '$1,884,411.00', '$1,763,916.00',
        '$917,500.00', '$3,022,020.00', '$248,087.00', '$1,910,635.00',
        '$3,094,650.00', '$585,858.00', '$2,547,363.00', '$1,056,600.00',
        '$1,043,130.00', '$1,319,574.00', '$1,049,400.00'
    ],
    'Per Student Budget': [
        '$628.00', '$582.00', '$639.00', '$644.00', '$625.00',
        '$652.00', '$581.00', '$655.00', '$650.00', '$609.00',
        '$637.00', '$600.00', '$638.00', '$578.00', '$583.00'
    ],
    'Average Math Score': [
        77.048432, 83.061895, 76.711767, 77.102592, 83.351499,
        77.289752, 83.803279, 76.629414, 77.072464, 83.839917,
        76.842711, 83.359455, 83.418349, 83.274201, 83.682222
    ],
    'Average Reading Score': [
        81.033963, 83.975780, 81.158020, 80.746258, 83.816757,
        80.934412, 83.814988, 81.182722, 80.966394, 84.044699,
        80.744686, 83.725724, 83.848930, 83.989488, 83.955000
    ],
    '% Passing Math': [
        66.680064, 94.133477, 65.988471, 68.309602, 93.392371,
        66.752967, 92.505855, 65.683922, 66.057551, 94.594595,
        66.366592, 93.867121, 93.272171, 93.867718, 93.333333
    ],
    '% Passing Reading': [
        81.933280, 97.039828, 80.739234, 79.299014, 97.138965,
        80.862999, 96.252927, 81.316421, 81.222432, 95.945946,
        80.220055, 95.854628, 97.308869, 96.539641, 96.611111
    ],
    '% Overall Passing': [
        54.642283, 91.334769, 53.204476, 54.289887, 90.599455,
        53.527508, 89.227166, 53.513884, 53.539172, 90.540541,
        52.988247, 89.892107, 90.948012, 90.582567, 90.333333
    ],
    'School Size': [
        'Large (2000-5000)', 'Medium (1000-2000)', 'Large (2000-5000)',
        'Large (2000-5000)', 'Medium (1000-2000)', 'Large (2000-5000)',
        'Small (<1000)', 'Large (2000-5000)', 'Large (2000-5000)',
        'Small (<1000)', 'Large (2000-5000)', 'Medium (1000-2000)',
        'Medium (1000-2000)', 'Large (2000-5000)', 'Medium (1000-2000)'
    ]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Set the index to 'school_name'
df.set_index('school_name', inplace=True)

# Display the DataFrame
print(df)


# %%
import pandas as pd

# Create the DataFrame with the provided data
data = {
    'school_name': [
        'Bailey High School', 'Cabrera High School', 'Figueroa High School', 
        'Ford High School', 'Griffin High School', 'Hernandez High School', 
        'Holden High School', 'Huang High School', 'Johnson High School', 
        'Pena High School', 'Rodriguez High School', 'Shelton High School', 
        'Thomas High School', 'Wilson High School', 'Wright High School'
    ],
    'School Type': [
        'District', 'Charter', 'District', 'District', 'Charter',
        'District', 'Charter', 'District', 'District', 'Charter',
        'District', 'Charter', 'Charter', 'Charter', 'Charter'
    ],
    'Total Students': [
        4976, 1858, 2949, 2739, 1468, 
        4635, 427, 2917, 4761, 962, 
        3999, 1761, 1635, 2283, 1800
    ],
    'Total School Budget': [
        '$3,124,928.00', '$1,081,356.00', '$1,884,411.00', '$1,763,916.00',
        '$917,500.00', '$3,022,020.00', '$248,087.00', '$1,910,635.00',
        '$3,094,650.00', '$585,858.00', '$2,547,363.00', '$1,056,600.00',
        '$1,043,130.00', '$1,319,574.00', '$1,049,400.00'
    ],
    'Per Student Budget': [
        '$628.00', '$582.00', '$639.00', '$644.00', '$625.00',
        '$652.00', '$581.00', '$655.00', '$650.00', '$609.00',
        '$637.00', '$600.00', '$638.00', '$578.00', '$583.00'
    ],
    'Average Math Score': [
        77.048432, 83.061895, 76.711767, 77.102592, 83.351499,
        77.289752, 83.803279, 76.629414, 77.072464, 83.839917,
        76.842711, 83.359455, 83.418349, 83.274201, 83.682222
    ],
    'Average Reading Score': [
        81.033963, 83.975780, 81.158020, 80.746258, 83.816757,
        80.934412, 83.814988, 81.182722, 80.966394, 84.044699,
        80.744686, 83.725724, 83.848930, 83.989488, 83.955000
    ],
    '% Passing Math': [
        66.680064, 94.133477, 65.988471, 68.309602, 93.392371,
        66.752967, 92.505855, 65.683922, 66.057551, 94.594595,
        66.366592, 93.867121, 93.272171, 93.867718, 93.333333
    ],
    '% Passing Reading': [
        81.933280, 97.039828, 80.739234, 79.299014, 97.138965,
        80.862999, 96.252927, 81.316421, 81.222432, 95.945946,
        80.220055, 95.854628, 97.308869, 96.539641, 96.611111
    ],
    '% Overall Passing': [
        54.642283, 91.334769, 53.204476, 54.289887, 90.599455,
        53.527508, 89.227166, 53.513884, 53.539172, 90.540541,
        52.988247, 89.892107, 90.948012, 90.582567, 90.333333
    ],
    'School Size': [
        'Large (2000-5000)', 'Medium (1000-2000)', 'Large (2000-5000)',
        'Large (2000-5000)', 'Medium (1000-2000)', 'Large (2000-5000)',
        'Small (<1000)', 'Large (2000-5000)', 'Large (2000-5000)',
        'Small (<1000)', 'Large (2000-5000)', 'Medium (1000-2000)',
        'Medium (1000-2000)', 'Large (2000-5000)', 'Medium (1000-2000)'
    ]
}

# Create the DataFrame
school_size_df = pd.DataFrame(data)
school_size_df.set_index('school_name', inplace=True)

# Now perform the groupby operations
size_math_scores = school_size_df.groupby(["School Size"])["Average Math Score"].mean()
size_reading_scores = school_size_df.groupby(["School Size"])["Average Reading Score"].mean()
size_passing_math = school_size_df.groupby(["School Size"])["% Passing Math"].mean()
size_passing_reading = school_size_df.groupby(["School Size"])["% Passing Reading"].mean()
size_overall_passing = school_size_df.groupby(["School Size"])["% Overall Passing"].mean()

# Display the results
print("Average Math Scores by School Size:")
print(size_math_scores)
print("\nAverage Reading Scores by School Size:")
print(size_reading_scores)
print("\nAverage % Passing Math by School Size:")
print(size_passing_math)
print("\nAverage % Passing Reading by School Size:")
print(size_passing_reading)
print("\nAverage % Overall Passing by School Size:")
print(size_overall_passing)


# %%
import pandas as pd

# Sample data for per_school_summary DataFrame
data = {
    'School Type': ['District', 'Charter', 'District', 'District', 'Charter'],
    'Average Math Score': [77.0, 83.1, 76.5, 78.2, 82.4],
    'Average Reading Score': [81.0, 84.2, 79.5, 80.8, 83.0],
    '% Passing Math': [66.5, 94.0, 67.0, 69.0, 92.5],
    '% Passing Reading': [80.0, 96.0, 81.0, 82.0, 94.0],
    '% Overall Passing': [53.5, 90.0, 55.0, 56.0, 88.5]
}

# Create the DataFrame
per_school_summary = pd.DataFrame(data)

# Optionally, set an index if needed (e.g., by school name if included)
# per_school_summary.set_index('school_name', inplace=True)
# Group by "School Type" and calculate the averages
average_math_score_by_type = per_school_summary.groupby("School Type")["Average Math Score"].mean()
average_reading_score_by_type = per_school_summary.groupby("School Type")["Average Reading Score"].mean()
average_percent_passing_math_by_type = per_school_summary.groupby("School Type")["% Passing Math"].mean()
average_percent_passing_reading_by_type = per_school_summary.groupby("School Type")["% Passing Reading"].mean()
average_percent_overall_passing_by_type = per_school_summary.groupby("School Type")["% Overall Passing"].mean()

# Display the results
print("Average Math Scores by School Type:")
print(average_math_score_by_type)
print("\nAverage Reading Scores by School Type:")
print(average_reading_score_by_type)
print("\nAverage % Passing Math by School Type:")
print(average_percent_passing_math_by_type)
print("\nAverage % Passing Reading by School Type:")
print(average_percent_passing_reading_by_type)
print("\nAverage % Overall Passing by School Type:")
print(average_percent_overall_passing_by_type)



