## Code
``` python
class NarcissisticNumber:
    """
    This class represents Narcissistic Numbers

    Narcissistic Numbers are numbers that the sum of each digits to the power of the total number of digits 
    equals to number
    """
    def __init__(self, m, n):
        self.m = m
        self.n = n

    # This method gets a list of Narcissistic numbers between integer m and n (m, n not included)
    def get_number(self):
        result = []
        for num in range(self.m + 1, self.n):
            narc = 0
            for digits in str(num):
                narc += int(digits) ** len(str(num))

            if narc == num:
                result.append(num)

        return result


# Print test results
test1 = NarcissisticNumber(m=0, n=10)
test2 = NarcissisticNumber(m=10, n=200)
test3 = NarcissisticNumber(m=200, n=400)
print(test1.get_number())
print(test2.get_number())
print(test3.get_number())

```

## Run
```
/Users/hientrinh/Quiz/venv/bin/python /Users/hientrinh/Quiz/Quiz_046.py
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[153]
[370, 371]

Process finished with exit code 0
```
