
n = int(input("Enter any value : "))
start = 2
while start<n:
    if n%start == 0:
        print(f"The number {n} is not prime")
        break
    start += 1
else:
    print(f"Number {n} is prime")
