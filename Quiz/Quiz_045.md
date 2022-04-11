## Code
```python
class Students:
    """ This class represents the students"""
    def __init__(self, students_lst):
        self.students_lst = students_lst

    # This function calculates the average score of all the students
    def get_average(self):
        avg = 0
        for student in self.students_lst:
            avg += (student["score"]/len(self.students_lst))

        return avg


# Input list of students and their names, scores
list_students = [{"name": "bob", "score": 40},
                 {"name": "alice", "score": 56},
                 {"name": "dice", "score": 35}]

# Call class with the input
students = Students(list_students)

# Print the average
print(students.get_average())

```

## Run
```
/Users/hientrinh/Quiz/venv/bin/python /Users/hientrinh/Quiz/Quiz_045.py
43.666666666666664

Process finished with exit code 0
```
