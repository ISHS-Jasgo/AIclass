# week04 prime_number v1.0
# add function

def is_prime(number) -> bool:
    """
    prime number check function
    :param number: integer number
    :return: True if number is prime number or False if number is not prime number
    """
    # check if number is prime
    for i in range(2, number):
        if number % i == 0:
            return False

    # prime numbers are greater than 1
    if number <= 1:
        return False
    return True


# get start and end value with one line using split and map
start, end = map(int, input("Enter start and end number: ").split())

# find all prime number between start and end
for n in range(start, end + 1):
    if is_prime(n):
        print(n)
