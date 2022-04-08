## Code
``` python
class Order:
    """ This class represents the sort algorithms in ascending order"""
    def __init__(self, num_list):
        self.num_list = num_list
    
    # This function sorts the list using selection method
    def selection(self):
        # Creates a duplicate of the main list and an empty list
        cur_list = self.num_list
        new_list = []
        
        # Go through the whole list
        for i in range(len(cur_list)):
            n = cur_list[0]
            for j in cur_list:
                # Checks for the smallest value in the list
                if n > j:
                    n = j

            # Adds the smallest value to the new list and removing that value from the old list
            new_list.append(n)
            cur_list.remove(n)

        return new_list
    
    # This function sorts the list using bubble method
    def bubble(self):
        # Creates a duplicate of the main list and an empty list
        new_list = self.num_list
        
        # Go through the whole list
        for i in range(len(new_list)):
            for j in range(0, len(new_list) - i - 1):
                if new_list[j] > new_list[j + 1]:
                    # Change the places of the two values if the former is larger than the later
                    new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]

        return new_list


# These commands runs the code on several examples
test1 = Order([6, 7, 8, 5, 4, 3])
print(test1.selection())
test1 = Order([6, 7, 8, 5, 4, 3])
print(test1.bubble())
test2 = Order([9, 8, 7, 6, 5, 4])
print(test2.selection())
test2 = Order([9, 8, 7, 6, 5, 4])
print(test2.bubble())
test3 = Order([1, 3, 4, 1, -1, 2])
print(test3.selection())
test3 = Order([1, 3, 4, 1, -1, 2])
print(test3.bubble())

```

## Run
```
/Users/hientrinh/Quiz/venv/bin/python /Users/hientrinh/Quiz/Quiz_044.py
[3, 4, 5, 6, 7, 8]
[3, 4, 5, 6, 7, 8]
[4, 5, 6, 7, 8, 9]
[4, 5, 6, 7, 8, 9]
[-1, 1, 1, 2, 3, 4]
[-1, 1, 1, 2, 3, 4]

Process finished with exit code 0
```
