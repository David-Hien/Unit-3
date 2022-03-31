## Code
``` python
# 1.State the four properties of the OOP programming paradigm
#   - Inheritance
#   - Encapsulation
#   - Polymorphism
#   - Data abstraction

# 2.Identify the components of a UML diagram for Classes.
#   - Top section: Name of class
#   - Middle section: Attributes
#   - Bottom section: Methods

# 3.A UML diagram is shown below for a score calculation. Create an object and obtain the average.
class Scores:
    """ This class collects scores and finds its average """
    def __init__(self, results: list):
        self.results = results

    # Methods
    # This method finds the average of the values in the list
    def getAverage(self) -> int:
        average = 0
        for score in self.results:
            average += (score / len(self.results))

        return int(average)


david = Scores([6, 6, 5, 7, 6, 7])
print(david.getAverage())

```

## Run
```
/Users/hientrinh/Quiz/venv/bin/python /Users/hientrinh/Quiz/Quiz_036.py
6

Process finished with exit code 0

```
