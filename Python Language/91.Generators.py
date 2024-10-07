# What are the benefits of using generators in Python?

# Memory Efficiency: Generators generate values on the fly, reducing memory usage compared to storing the entire sequence in memory.
# Lazy Evaluation: Values are computed only when needed, which can lead to performance improvements, especially with large datasets.
# Maintain State: Generators automatically maintain their state between yield statements, making them suitable for iterative processes.
# Convenience: Generators simplify code for iterating over large datasets or streams of data without needing to manage state explicitly.

# Python Generator functions return a generator object that is iterable, i.e., can be used as an Iterator. Generator objects are used either by calling the next method of the generator object or using the generator object in a “for in” loop.


def my_generator():
    for i in range(15):
        yield i


gen = my_generator()

for j in gen:
    print(j)

# -------------------------------------------------------------------------------------------
# Creating Fibonacci series
def fib(limit):
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b
        
# Create a generator object
x = fib(200)

# Iterate over the generator object and print each value
for i in x:
    print(i)


# ---------------------------------------------------------------------------------------------
# generator expression
generator_exp = (i * 5 for i in range(5) if i%2==0)

for i in generator_exp:
    print(i)

# ----------------------------------------------------------------------------------------------------------------------
# State Management: Generators maintain their state between yields automatically. You can also pass data into the generator using the send() method.

def stateful_generator():
    value = yield  # Receive a value from outside
    while True:
        value = yield value * 2

gen = stateful_generator()
next(gen)          # Start the generator
print(gen.send(10))  # Outputs: 20

# ----------------------------------------------------------------------------------------------------------

# Exception Handling: You can handle exceptions within a generator using standard try-except blocks.

def error_handling_generator():
    try:
        yield 1
        yield 2
        raise ValueError("An error occurred")
        yield 3
    except ValueError as e:
        print(e)

gen = error_handling_generator()
print(next(gen))
print(next(gen))
print(next(gen))  # This will trigger the exception


# To handle exceptions outside the generator, use generator.throw().

def gen_with_error():
    yield 1
    raise ValueError("Error inside generator")

g = gen_with_error()
print(next(g))
try:
    g.throw(ValueError, "Error thrown")
except ValueError as e:
    print(e)