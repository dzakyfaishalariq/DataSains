import pandas as pd
import numpy as np
import os 
os.system('cls')

def main():
    print('hallo semuanya')

data = {
    'nama':'Dzaky faishalariq',
    'kelas':'informatika A',
    'info':'saya Dzaky Faishalariq'
}

print(data)

for i in data:
    print('|{:<10}|{:<30}|'.format(i,data[i]))

main()
