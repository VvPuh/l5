line_1 = set(input('Enter first line: '))
line_2 = set(input('Enter second line: '))
print("Unic symbols: ", end='')
for el in (line_1 - line_2):
    print("'", el, "' ", sep='', end='')
