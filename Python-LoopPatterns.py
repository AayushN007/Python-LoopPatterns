#1. generate numbers from 1 to n in reverse order.

n = int(input("Enter the value of n"))
for i in range(n, 0, -1):
    print(i, end=" ")
print()



#2.generate the 1st n euler numbers: 1, 8m 27, 64

n = int(input("Enter the value of n"))
print("the 1st ",n," euler numbers are:")
for i in range(1, n+1):
    print(i**3, end=" ")

#3. Generate the first n powers of 3: 1 ,3, 7, 81

n = int(input("Enter the value of n"))
print("the 1st ",n," powers of 3 are:")
for i in range(n):
    print(3**i, end=" ")

#4. Generate the sequence 1, -2, 3, -4, 5, -6.

n = int(input("Enter the value of n"))
print("the 1st ",n," numbers in the sequence are:")
for i in range(1, n+1):
    if i % 2 == 0:
        print(-i, end=" ")
    else:
        print(i, end=" ")

#5. Generate all the numbers from 1 to n that are divisible by both 3 and 5. 

n = int(input("Enter the value of n"))
print("the numbers from 1 to ",n," that are divisible by both 3 and 5 are:")
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
        
#6. generate the numbers from 1 ,3 ,6 ,10, 15, 21.....

n = int(input("Enter the value of n"))
print("the 1st ",n," numbers in the sequence are:")
sum = 0
for i in range(1, n+1):
    sum += i
    print(sum, end=" ")