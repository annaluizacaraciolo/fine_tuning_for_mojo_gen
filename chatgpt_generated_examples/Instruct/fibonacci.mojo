# Generated by ChatGPT (GPT-4) based on 6 examples provided of Mojo code
@always_inline
fn fibonacci(n: Int) -> Int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
