nb = int(input("Enter a number: "))

cond = False

if nb > 1:
    for i in range(2, nb):
        if (nb % i) == 0:
            cond = True
            break

if cond:
    print(nb, "is not a prime number!")
else:
    print(nb, "is a prime number!")
