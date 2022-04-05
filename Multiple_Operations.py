first = input("Enter the First Value")
second = input("Enter the Second Value")


def multiple_operation(first_value, second_value):
    operation = input("Enter the Operation to perform (+,-,*,/)")
    if operation == "+":
        add = int(first_value) + int(second_value)
        return print(add)
    elif operation == "-":
        sub = int(first_value) - int(second_value)
        return print(sub)
    elif operation == "*":
        mul = int(first_value) * int(second_value)
        return print(mul)
    elif operation == "/":
        div = float(first_value) / float(second_value)
        return print(div)
    else:
        return print("Invalid")


multiple_operation(first, second)
