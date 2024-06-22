def lower_triangular(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()

def upper_triangular(n):
    for i in range(n):
        for j in range(i, n):
            print("*", end=" ")
        print()

def pyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        print()

print("Lower Triangle:")
lower_triangular(5)
print("Upper Triangle:")
upper_triangular(5)
print("Pyramid:")
pyramid(5)

