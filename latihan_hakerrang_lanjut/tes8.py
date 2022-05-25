# mencetak berapa kali substring muncul dari string yang diberikan.

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        # DIGUNAKAN UNTUK MENGECEK SUBSTRING
        if string[i:].startswith(sub_string):
            count += 1
    return count


def main():
    string = input()
    sub_string = input()
    count = count_substring(string, sub_string)
    print(count)


main()
