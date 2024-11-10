import random


def get_random_integer(min_value, max_value):
    """
     Generate a random integer between min_value and max_value.

     Args:
         min_value (int): The minimum integer value (inclusive).
         max_value (int): The maximum integer value (inclusive).

     Returns:
         int: A random integer between min_value and max_value.
     """
    return random.randint(min_value, max_value)

def get_random_operator():
    """
    Select a random operator from +, -, *.

    :return: A string representing a random operator.
    """
    return random.choice(['+', '-', '*'])


def calculate_expression(num1, num2, operator):
    """
    Calculate the result of a mathematical expression based on the provided operator.

    Args:
        num1 (int): The first operand in the expression.
        num2 (int): The second operand in the expression.
        operator (str): The operator to apply between num1 and num2 (+, -, or *).

    Returns:
        tuple: A tuple containing the expression as a string and the computed result of the expression.
    """
    expression = f"{num1} {operator} {num2}"
    # Calculate result based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return expression, result


def math_quiz():
    """
    Main function to run the Math Quiz game.
    This function generates a series of math questions, checks the user's answers,
    and displays the final score.

    The number of questions is derived from the value of pi, stored in t_q.
    """
    score = 0
    t_q = 3.14159265359  # Using pi to represent the number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(t_q)):
        # Generate two random numbers and a random operator for each question
        num1 = get_random_integer(1, 10)
        num2 = get_random_integer(1, 5.5)
        operator = get_random_operator()

        # Create the math problem and calculate the correct answer
        problem, correct_answer = calculate_expression(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Error handling to ensure the user inputs a valid integer
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue  # Skip to the next question if input is invalid

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    # Display the final score after the game
    print(f"\nGame over! Your score is: {score}/{int(t_q)}")

if __name__ == "__main__":
    math_quiz()