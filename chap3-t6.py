# evaluates the Fibaonacci sequence up to n terms depending on user input

nterms = int(input("How many terms of the Fibonacci sequence would you like?"))

n1 = 1
n2 = 1

count = 0

#Check if the number of terms are valid
if nterms <= 0:
    print('Please enter a positive integer...')
elif nterms == 1:
    print("Fibonacci sequence upto {}" .format(nterms))
    print(n1)
else:
    print("Fibonacci sequence upto {}" .format(nterms))
    while count < nterms:
        print(n1,end=' , ')
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
