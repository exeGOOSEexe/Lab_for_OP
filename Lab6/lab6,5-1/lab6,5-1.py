import os

def PrintRectangle(a, b, file):
    f = open(file, 'a')
    a = int(a); b = int(b)
    f.write(a * "*")
    if b < 1 :
        exit
    else:
        for i in range(1, b - 1):
            f.write("\n*" + (a - 2) * " " + "*" )
    f.write( "\n" + a * "*")
def PrintSquare(a, file):
    f = open(file, 'a')
    a = int(a)
    f.write(a * "*")
    if a < 1:
        exit
    else:
        for i in range(1, a - 1):
            f.write("\n*" + (a - 2) * " " + "*")
    f.write('\n' + a * "*")

files = (os.listdir())

if "input.txt" in files:
    with open("input.txt","r")as y:
        firth = y.readline()
        two = y.readline()
        firth_one = firth[0]; firth_two = firth[2]
        if firth_two == " ":
            PrintSquare(firth_one, two)
        elif firth_two != " ":
            PrintRectangle(firth_one,firth_two,two)
else:
    print("file not found")