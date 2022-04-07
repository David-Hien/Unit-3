# 0.1 + 0.2 == 0.3 is False

## Explanation
When using float values to represent numbers, it's stored in base 2. In the case of decimal numbers, most of the times, the decimal fractions cannot be represented as binary fractions. For that reason, the statement 0.1 + 0.2 == 0.3 is false.

## Code
``` python
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)

```

## Run
```
0.30000000000000004
False

```

## Possible solution
To tackle the issue, I decided to use getcontext().prec from the inbuilt decimal module to change the significant figures of the decimal value so as to prevent it from taking the incorrect digits into account. In the example below, I set the number of significant figures to 6, instead of the default value of 28.

## Code
``` python
from decimal import Decimal, getcontext

getcontext().prec = 6
print(Decimal("0.1") + Decimal("0.2"))
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

```

## Run
```
0.3
True

```

## Citation
GeeksforGeeks. “Why 0.3 - 0.2 Is Not Equal to 0.1 in Python?” GeeksforGeeks, 26 Nov. 2020, www.geeksforgeeks.org/why-0-3-0-2-is-not-equal-to-0-1-in-python.
