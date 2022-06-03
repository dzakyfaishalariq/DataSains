# alphabet rangoli
def print_rangoli(size):
    # your code goes here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(size):
        print("-".join(alphabet[i:size]).center(size*4-3, "-"))
    for i in range(size-1, 0, -1):
        print("-".join(alphabet[i:size]).center(size*4-3, "-"))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
