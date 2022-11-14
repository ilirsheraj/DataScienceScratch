import matplotlib.pyplot as plt


test1_grades = [99, 90, 85, 97, 80]
test2_grades = [100, 85, 60, 90, 70]

plt.scatter(test1_grades, test2_grades)
plt.title("Equal Axis")
plt.xlabel("Grades of Test 1")
plt.ylabel("Grades of Test 2")
plt.axis("equal")
plt.show()
