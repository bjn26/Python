def collatz(number):
        if(number%2==0):
            print(number//2)
            return number//2
        else:
            n=3*number+1
            print(n)
            return n
number=input("Enter a number:")
while(number!=1):
        number = collatz(int(number))