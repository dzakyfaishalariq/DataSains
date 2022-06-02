import textwrap
# membuat fungsi untuk memisahkan kata sebannyak rang yang kita tentukan


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == "__main__":
    str, max_width = input(), int(input())
    rat = wrap(str, max_width)
    print(rat)
