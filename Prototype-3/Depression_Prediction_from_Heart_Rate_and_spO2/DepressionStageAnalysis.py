import pandas as pd

# Read the CSV file
data = pd.read_csv('depression_stage_data.csv')

# Count the values in the 'Depression Stage' column
stage_counts = data['Depression Stage'].value_counts()

# Extract the counts for each stage (defaulting to 0 if a stage is missing)
count_0 = stage_counts.get(0, 0)
count_1 = stage_counts.get(1, 0)
count_2 = stage_counts.get(2, 0)
count_3 = stage_counts.get(3, 0)

# Print the counts
print(f"Count of 0: {count_0}")
print(f"Count of 1: {count_1}")
print(f"Count of 2: {count_2}")
print(f"Count of 3: {count_3}")

depression_stage_result=""
# Determine the stage with the maximum count
max_count = max(count_0, count_1, count_2, count_3)
if max_count == count_0:
    depression_stage_result="No Depression (Healthy)"
    print("No Depression (Healthy)")
elif max_count == count_1:
    depression_stage_result="Mild Depression"
    print("Mild Depression")
elif max_count == count_2:
    depression_stage_result="Moderate Depression"
    print("Moderate Depression")
elif max_count == count_3:
    depression_stage_result="Severe Depression"
    print("Severe Depression")