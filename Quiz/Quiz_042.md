## Code
``` python
class Quiz042:
    """This class is quiz 42"""
    def __init__(self, n):
        self.n = n

    # This function produces a list of list of numbers in ascending order with ascending number of values starting from 1
    def mapper(self) -> list:
        result = []
        for i in range(self.n):
            sub_lst = []
            for j in range(i + 1):
                sub_lst.append(j + 1)

            result.append(sub_lst)

        return result


print(Quiz042(4).mapper())

```

## Run
```
/Users/hientrinh/Quiz/venv/bin/python /Users/hientrinh/Quiz/Quiz_042.py
[[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]

Process finished with exit code 0

```
