def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return round((n1 / n2),2)

math_operators = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

carry_over = "n"
number1 = 0
continue_working = True

while continue_working:

    if carry_over == "n":
        number1 = int(input("Enter a number: "))
        choose_operator = input("Choose an operator: ")
        number2 = int(input("Enter another number: "))

        if choose_operator in math_operators:
            carry_over = input(f"Result is {math_operators[choose_operator](number1, number2)}. Type 'y' to continue. with same result. Type 'n' to start again. ")
            number1 = math_operators[choose_operator](number1, number2)

    if carry_over == "y":
        first_time = 1
        choose_operator = input("Choose an operator: ")
        number2 = int(input("Enter another number: "))
        carry_over = input(f"Result is {math_operators[choose_operator](number1, number2)}. Type 'y' to continue. with same result. Type 'n' to start again. ")
