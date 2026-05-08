from module5_mod import NumberList

if __name__ == "__main__":
    n = int(input("Enter total numbers N: "))
    number_list = NumberList(n)

    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        number_list.add_number(num)
    
    x = int(input("Enter number X to find: "))
    print(number_list.find_number(x))
