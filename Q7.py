# Quesion 7
three_digit_num = int(input("Please enter a three digit integer: "))
if three_digit_num % 10 == 0:
    print("Invalid input. Rightmost digit must be non-zero.")
else:
    reversed_num = 0
    while three_digit_num > 0:
        digit = three_digit_num % 10
        reversed_num = reversed_num * 10 + digit
        three_digit_num //= 10

    print(f"You entered: {three_digit_num}")
    print(f"{three_digit_num} reversed is {reversed_num}.")
