fn fibonacci(n: Int) -> Int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        var a: Int = 0
        var b: Int = 1
        for i in 2:n+1:
            var c: Int = a + b
            a = b
            b = c
        return b

# Example usage
print(fibonacci(10))  # Output: 55
