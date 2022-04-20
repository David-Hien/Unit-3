## Code
``` python
class quiz_048:
    """ This class represents Quiz 48"""
    def __init__(self, lst):
        self.lst = lst

    # This method locates the flat land (where two consecutive points have the same y-value),
    # and find the point in the middle
    def get_land(self):
        for i in range(len(self.lst) - 1):
            # Check if y-value is the same
            if self.lst[i][1] == self.lst[i + 1][1]:
                return (self.lst[i][0] + self.lst[i + 1][0]) / 2, self.lst[i][1]


# Test
test1 = quiz_048([(0, 100), (1000, 500), (1500, 1500), (3000, 1000), (4000, 150), (5500, 150), (6999, 800)])
test2 = quiz_048([(0, 1000), (300, 1500), (350, 1400), (500, 2000), (800, 1800), (1000, 2500), (1200, 2100),
                  (1500, 2400), (2000, 1000), (2200, 500), (2500, 100), (2900, 800), (3000, 500), (3200, 1000),
                  (3500, 2000), (3800, 800), (4000, 200), (5000, 200), (5500, 1500), (6999, 2800)])

print(test1.get_land())
print(test2.get_land())

```

## Run
```
/Users/hientrinh/Quiz/venv/bin/python /Users/hientrinh/Quiz/Quiz_048.py
(4750.0, 150)
(4500.0, 200)

Process finished with exit code 0
```
