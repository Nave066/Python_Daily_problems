def max_num(number):
    if 1 <= number <= 5:
        my_list = [6, 3, 12, 8, 1]

        my_list.sort()
        print(my_list)
        maxi = my_list[-number]
        return print("Your Maximum number is: " + str(maxi))
    else:
        print("Invalid")


if __name__ == "__main__":
    input_from_user = int(input("Enter number: "))
    max_num(input_from_user)

