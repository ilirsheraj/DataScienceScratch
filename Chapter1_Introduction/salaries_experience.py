# The list below contains the salaries for a number of employees and their years as data scientists
from collections import defaultdict, Counter


salaries_and_tenures = [
	(83000, 8.7), (88000, 8.1),
	(48000, 0.7), (76000, 6),
	(69000, 6.5), (76000, 7.5),
	(60000, 2.5), (83000, 10),
	(48000, 1.9), (63000, 4.2)
]

print("Years Salary")
for salary, years in salaries_and_tenures:
	print(years, salary)
print("=" * 30)

# Average salary per tenure: It makes no difference because all tenure years are unique
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
	salary_by_tenure[tenure].append(salary)
print(salary_by_tenure)

average_salary_by_tenure = {
	tenure: sum(salaries) / len(salaries) for tenure, salaries in salary_by_tenure.items()
}

print("=" * 30)

# Group tenure into three categories: less than 2 years, 2 to 5 years and more than 5 years
def tenure_bucket(tenure):
	if tenure < 2:
		return "less than two"
	elif tenure < 5:
		return "between two and five"
	else:
		return "more than five"


# Group the salaries together
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
	bucket = tenure_bucket(tenure)
	print(bucket)
	salary_by_tenure_bucket[bucket].append(salary)
print(salary_by_tenure_bucket)

print("=" * 30)

# Compute average salary per each group
average_salary_by_bucket = {
	tenure_bucket: sum(salaries) / len(salaries) for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
print(average_salary_by_bucket)
