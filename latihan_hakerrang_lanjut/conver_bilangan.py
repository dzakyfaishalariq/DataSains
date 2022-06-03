import os
os.system('cls')


def print_formatted(number):
    # your code goes here

    for i in range(1, number+1):
        oktal = oct(i).replace('0o', '').rjust(len(oct(number)))
        heksa = hex(i).replace('0x', '').upper().rjust(len(hex(number)))
        biner = bin(i).replace('0b', '').rjust(len(bin(number)))
        # mencetak string formating
        print("{} {} {} {}".format(i, oktal, heksa, biner))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
