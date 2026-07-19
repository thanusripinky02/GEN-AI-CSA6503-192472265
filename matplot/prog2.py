import matplotlib.pyplot as plt
subjects = ["Python", "Java", "C++"]
marks = [90, 80, 85]
plt.bar(subjects, marks)
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()