# WAP fib series 

a = 0
b = 1 

x = int (input("Sequence till where you want to follow the fibbonaci series: "))

for i in range (0 , x) :
    print (a) 
    result = a + b
    a=b
    b=result