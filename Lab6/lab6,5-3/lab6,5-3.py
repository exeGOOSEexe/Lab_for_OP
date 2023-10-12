import os
fi = (os.listdir())
files = fi
if "input.txt" in files:
    f = open("input.txt",'r')
    h = open("output.txt",'a')
    w = f.readline()
    w = int(w)
    for i in range(1,w + 1):
        if i > 1:
            for c in range(2,i):
                if (i % c ) == 0:
                    break
            else:
                h.writelines(str(i) + ' ')
elif "input.txt" not in files:
    print("Файл с входными данными не обнаружен")