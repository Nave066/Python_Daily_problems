def maximum_in_subarray(inp, length):
    """
    :param inp: Input string From main method
    :param length: Length of sub string given by the user
    :return: Nothing returns, printed in method itself
    """
    for i in range(0, len(inp)-length+1):  # For loop for iterating through the array
        maximum_value = inp[i]
        sub_array = []
        for j in range(i, i+length-1):  # For loop for iterating through sub arrays
            sub_array.append(inp[j])
            if maximum_value < inp[j+1]:  # Finding maximum among sub array
                maximum_value = inp[j+1]
        sub_array.append(inp[i+length-1])
        print("Maximum in {} is {}".format(sub_array, maximum_value))


if __name__ == '__main__':
    input_array = [4, 6, 7, 1, 13, 3, 9, 10, 34]
    subarray_length = int(input("Enter the length"))
    maximum_in_subarray(input_array, subarray_length)
