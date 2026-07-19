import matplotlib.pyplot as plt
languages = ["Python", "Java", "C++", "C"]
students = [40, 30, 20, 10]
plt.pie(students, labels=languages, autopct="%1.1f%%")
plt.title("Programming Languages")
plt.show()