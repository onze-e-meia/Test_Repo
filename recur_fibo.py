def recur_fibo(n):  
   if n <= 2:  
       return 1  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))


    
def fibo(n):
    if n <= 2:
        return 1
    i = 3
    f1 = 1
    f2 = 1
    while i <= n:
        fn = f1 + f2
        f2 = f1
        f1 = fn
        i += 1
    return fn
