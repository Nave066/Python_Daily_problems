
def common_str(str1, str2):
    res = []
    for i in str1:
        for j in str2:
            if i == j:
                res.append(i)
    return res


if __name__ == "__main__":
    string1 = input("Enter First string")
    string2 = input("Enter Second string")
    print(common_str(string1, string2))