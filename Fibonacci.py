n = int(input("Enter a number of terms: "))

a = 0
b = 1
count = 0

while count<n:
    print(a, end=' ')
    c=a+b 
    a=b 
    b=c
    count+=1