from itertools import repeat


def inp():
    user = ""
    array = []
    while True:
        try:
            user = input("Enter the array: ")
            user = user.split()
            for el in user:
                array.append(int(el))
            return array
        except:
            print("Incorrect data, try again.")


def moda(array):
    max_element, element = 'no', 0
    max_repeat, repeat_counter = 0, 0
    for el in array:
        if el == element:
            repeat_counter += 1
        else:
            if repeat_counter > max_repeat:
                max_repeat = repeat_counter
                max_element = element
            elif repeat_counter == max_repeat:
                max_element = 'no'
            element = el
            repeat_counter = 1
    if repeat_counter > max_repeat:
        max_repeat = repeat_counter
        max_element = element
    elif repeat_counter == max_repeat:
        max_element = 'no'
    return max_element


print("Moda of this array is", moda(sorted(inp())))
