class NumberList:
    def __init__(self, n):
        """
        Initialize the NumberList class with the total numbers N.
        """
        self.n = n
        self.numbers = []

    def add_number(self, num):
        """
        Add a number to the list.
        """
        self.numbers.append(num)

    def find_number(self, num):
        """
        Find the position of a number in the list.
        """
        if num in self.numbers:
            return self.numbers.index(num) + 1
        else:
            return -1