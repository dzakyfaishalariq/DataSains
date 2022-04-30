# fungsi untuk mengubah tulisan kecil kebesar maupun sebaliknya
def swap_case(s):
    string_baru = ''
    for i in s:
        if i.isupper():
            string_baru += i.lower()
        else:
            string_baru += i.upper()
    return string_baru


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
