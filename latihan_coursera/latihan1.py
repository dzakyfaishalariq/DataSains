import array as arr
a = arr.array('i', [-3, -1, 0, 1, 3])
# uji kebenaran array a
print(a)
if a.buffer_info()[0] == a.buffer_info()[1]:
    print("array a is contiguous")
else:
    print("array a is not contiguous")

