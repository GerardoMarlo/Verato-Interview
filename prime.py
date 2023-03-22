def number(n):
    counter=0
    #prime number its only divisible by itself or 1

    
    for i in range (2, int(n**.5)+1): #Modified range to go from 2 to the square root of n
        if (n % i == 0):
            counter+=1


    if counter >= 1:
        print(n,"is NOT prime")  
    else:    
        print(n,"is prime")
           




number(5)
number(4)
number(15)
number(9)
number(7)
number(223)
    