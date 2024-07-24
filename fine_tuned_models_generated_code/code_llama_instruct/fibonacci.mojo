fn fib[n: Int]() -> Int:
    if n < 2:
        return 1
    else:
        return fib[n - 1]() + fib[n - 2]()

# The code above does not work 
# Some modifications were done in order to test it

# 1. The first modification done in order to try to run this mojo program was to remove square
#    brackets and define the argument of the function inside parentheses.

# fn fib(n: Int) -> Int:
#     if n < 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# def main():
#     print(fib(6))

# 2. The code is runnable, but it does not give the correct answer for the 6th fibonacci number;
#    In order to correct the result, here's is the proposed modification:

fn fib(n: Int) -> Int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    print(fib(6))
