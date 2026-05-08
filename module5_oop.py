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


if __name__ == "__main__":
    n = int(input("Enter total numbers N: "))
    number_list = NumberList(n)
    
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        number_list.add_number(num)
    
    x = int(input("Enter number X to find: "))
    print(number_list.find_number(x))

