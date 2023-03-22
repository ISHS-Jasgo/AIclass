start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

# find all prime number between start and end
for number in range(start, end + 1):
    is_prime = True
    # check if number is prime
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    # prime numbers are greater than 1
    if number <= 1:
        is_prime = False
    # print result
    if is_prime:
        print(number)
