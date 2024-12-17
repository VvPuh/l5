def inp():
    while True:
        try:
            line_inp = input('Enter line of int: ')
            line_inp = line_inp.split()
            line_inp = set(line_inp)
            for element in line_inp:
                line_inp.remove(element)
                line_inp.add(int(element))
            return line_inp
        except:
            print("Not int in line, try again.")


print("First line.")
line_1 = inp()
print("Second line.")
line_2 = inp()
print("Int in both lines: ")
for el in (line_1 & line_2):
    print(el, end=' ')
