N = input("Min value: ")
M = input("Max value: ")
count = 0
while True:
    if N.isdigit():
        if M.isdigit():
            N = int(N)
            M = int(M)
            if N >= 100000 and N <= 999999:
                if M >= 100000 and M <= 999999:
                    if M>=N:
                        break;
                    else:
                        print("Incorrect max value (correct max>=min)")
                else:
                    print("Incorrect max value (correct in [100000,999999])")
            else:
                print("Incorrect min value (correct in [100000,999999])")
        else:
            print("Incorrect max value (not in N)")
    else:
        print("Incorrect min value (not in N)")
    N = input("Min value: ")
    M = input("Max value: ")

for x in range(N, M + 1):
    a5 = x % 10
    a4 = (x % 100 - a5) // 10
    a3 = ((x % 1000 - a5) // 10 - a4)
    a0 = x // 100000
    a1 = x // 10000 - a0 * 10
    a2 = x // 1000 - a0 * 100 - a1 * 10
    if a0 + a1 + a2 == a3 + a4 + a5:
        count += 1
print(count)