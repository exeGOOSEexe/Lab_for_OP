import os
fi = (os.listdir())
files1 = fi
"""files = [f for f in f if ".txt" in f]
"""
"""i = 0
for files in files:
    i += 1
print(i)"""
if "input.txt" in files1:
    f = open("input.txt",'r')
    h = open("output.txt",'a')
    g = f.readline()
    l = 0; p = 1
    with open("output.txt", "w", encoding="utf-8") as y:
        y.write("Число: {}".format(g))
        y.write("\nКоличество цифр: {}".format(len(g)))
        while int(g) > 0:
            digit = int(g) % 10
            l += digit
            p = p * digit
            g = int(g) // 10
        y.write("\nСумма цифр: {}".format(l))
        y.write("\nПроизведение цифр: {}".format(p))
    f.closed
elif "input.txt" not in files1:
    print("Файл с входными данными не обнаружен")