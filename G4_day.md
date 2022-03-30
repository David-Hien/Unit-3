## Code
``` python
# Import the random library
import random


class RandomGrouping:
    """ This class is used for generating random groups with predetermined size from any list """

    # This function declares attributes
    def __init__(self, lst, group_size, seed):
        self.lst = lst
        self.group_size = group_size
        self.seed = seed

    # This function sets the seed for random, so that other systems with the same seed will give the same random value
    def set_seed(self):
        random.seed(self.seed)

    # This function randomly shuffles the list
    def shuffle(self):
        # Creates a new list for the shuffled value
        new_lst = []

        # This loop insert random values from the old list into the new list
        for i in range(len(self.lst)):
            # Create a random value of iteration
            rand = random.randint(0, len(self.lst) - 1)

            # Add the value of the random iteration of the list
            new_lst.append(self.lst[rand])

            # Remove that value from the old list so it won't duplicate
            self.lst.remove(self.lst[rand])

        self.lst = new_lst
        return self.lst

    # This function separates a list into groups of a predetermined size
    def grouping(self):
        # Creates a new list for the list of groups
        grouping_list = []

        # This loop runs from the first iteration to the last while skipping the value of the 'group_size'
        for i in range(0, len(self.lst), self.group_size):
            # Appends a list with the group members
            grouping_list.append(self.lst[i: i + self.group_size])

        # This loop prints the group number and its members
        for group_num in range(len(grouping_list)):
            # Prints the group number and the names inside the list seperated by a comma
            print(f"Group {group_num + 1}:", ', '.join(grouping_list[group_num]))


# List of students in G11
student_list = ["Danish", "Marika", "Minato", "Aup", "Mitsuki Baba", "Shinebayar", "Fabi", "Soraya", "Zoopash", "Julia",
                "Taichi", "Yurika", "Beatrice", "Elia", "Kyoka", "Ryu", "Leo", "Mitsuki Kyota", "Ming", "Marian",
                "Kamilla", "Kojiro", "Jun", "Ji Yang", "Reiji", "Minori", "Shimba", "Vanni", "Nagisa", "Boss", "Nina",
                "Hana", "David", "Asahi", "Michael", "Yuki", "Janet", "Anju", "Andy"]

# Declare values for class
G4_random_group = RandomGrouping(lst=student_list, group_size=5, seed=2022)

# Set seed for random
G4_random_group.set_seed()

# Shuffles the names around
G4_random_group.shuffle()

# Prints the list of groups
G4_random_group.grouping()

```

## Run
```
/Users/hientrinh/exampleApp/venv/bin/python /Users/hientrinh/exampleApp/random_group_generator.py
Group 1: Michael, Ming, Boss, Anju, Kamilla
Group 2: Aup, Nina, Ji Yang, Hana, Danish
Group 3: Janet, David, Ryu, Yurika, Vanni
Group 4: Nagisa, Marian, Minori, Reiji, Yuki
Group 5: Minato, Beatrice, Mitsuki Baba, Kojiro, Zoopash
Group 6: Elia, Shinebayar, Leo, Taichi, Shimba
Group 7: Soraya, Marika, Fabi, Kyoka, Asahi
Group 8: Andy, Julia, Mitsuki Kyota, Jun

Process finished with exit code 0
```
