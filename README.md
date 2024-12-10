# pandas-challenge
Summary Overview
This project performs a detailed analysis of school performance based on data from two CSV files (schools_complete.csv and students_complete.csv)
# Ensure the CSV files are correctly located in these paths before running the script.
/Users/christinaland/Downloads/pandachallenge.py/PyCitySchools/Resources/schools_complete.csv
/Users/christinaland/Downloads/pandachallenge.py/PyCitySchools/Resources/students_complete.csv
# Loading Data into pd.read_csv
file1 = pd.read_csv('/Users/christinaland/Downloads/pandachallenge.py/PyCitySchools/Resources/schools_complete.csv')
file2 = pd.read_csv('/Users/christinaland/Downloads/pandachallenge.py/PyCitySchools/Resources/students_complete.csv')

#   Display Datafram .head() function from loaded data
print(file1.head())
print(file.2head())
# create variables for data set merging
Schooldataset and studentdataset for merging
# merge the dataframe pd.merge() function
dataframemerged = pd.merge(schoolsdataset,studentdataset, how="left", on=" school_name")dataframemerged.head())

# Count unique names under ['School_name'] with .nunique() function
total_unique_schools = schoolsdataset['School_name'].niunque()
# f format string 
print(f"Total number of unique schools:{total_unique_schools}")
# count student name with .count() fuctionv- counting all that are not blank
total_budget = dataframemerged['student_name'].count() 
print()
#display total budget with .sum() under the budget column
total_budget = schooldataset[student_name].sum()
print()

#dispaly mean of math score 
mean_math_score = dataframemerged[math_score].mean()
print()
# mean for readinf .mean()
mean_reading_score = dataframemerged['reading_score'].mean()
print()

# average number of students passing math 
# sort the number of student with a 70 or above and return the value to perform an average of the number of students who passed the class
passing_read_percentage = dataframemerged[math_score]>=70)].count['Student_name'] 
passing_read_count/(total_students) x 100

# do the same for the math count 
# Passing Percentages for Math, Reading, and Overall (students passing both math and reading with a score ≥ 70).
passing_math_count = dataframemerged[
    (dataframemerged["math_score"] >= 70) & (dataframemerged["reading_score"] >= 70)
].count()["student_name"]
overall_passing_rate = passing_math_count /  float(total_students) * 100
overall_passing_rate

# group the data by school type (e.g., District, Charter) to compare metrics
school_types = schoolsdataset.set_index(["school_name"])["type"]

# compute the per-student budget and analyze how it correlates with performance metrics

per_capita_spending = per_school_budget / total_students

# generate a summary DataFrame that includes all the key metrics for the district and each school.
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


