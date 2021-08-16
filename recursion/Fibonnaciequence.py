#Recursive Solution
# def fibonacci(n):

#     if (n ==1 or n==0):
#         return n
    
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

#ITERATIVE SOLUTION
def fibonacci(n):

    a = 0
    b = 1

    for i in range(n):
        a,b = b,a+b
        print("a -> " + str(a))
        print("b -> " + str(b))

    return a

#Memorization

#Cache
# n = 10
# cache = [None]*(n+1)
# def fibonacci(n):

#     #Base Case
#     if n == 0 or n == 1:
#         return n

#     #check cache

#     if cache[n] != None:
#         return cache[n]

#     #keep setting cache
#     cache[n] = fibonacci(n-1) + fibonacci(n-2)

#     return cache[n]

print(fibonacci(10))