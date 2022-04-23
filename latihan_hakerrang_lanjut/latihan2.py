def count_substring(string, sub_string):
    nilai = string.find(sub_string)
    return nilai


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
