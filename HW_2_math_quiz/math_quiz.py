import random


def get_random_integer(minimum_value: int, maximum_value: int) -> int:
    """
    Get a random integer between the given values - [minimum_value, maximum_value].
    The value is returned from a discrete uniform distribution.

    Args:
        minimum_value (int): Minimum random value that could be returned - value inclusive
        maximum_value (int): Maximum random value that could be returned - value inclusive

    Returns:
        int: Random integer between [minimum_value, maximum_value]

    Rises:
        ValueError: If "minimum_value" >= "maximum_value".

    Examples:
        >>> random.seed(42)  #  Setting random seed for reproducibility - not necessary during actual usage
        >>> get_random_integer(0, 100)
        81
    """
    if minimum_value >= maximum_value:
        raise ValueError("minimum_value must be smaller than maximum_value")
    return random.randint(minimum_value, maximum_value)


def get_random_operator() -> str:
    """
    Get a random mathematical operator from the choice ['+', '-', '*'].

    Args: -

    Returns:
        str: Random mathematical operator

    Rises: -

    Examples:
        >>> random.seed(42)  #  Setting random seed for reproducibility - not necessary during actual usage
        >>> get_random_operator()
        '*'
    """
    return random.choice(['+', '-', '*'])


def process_numbers(number_1: int, number_2: int, operator: str) -> [str, int]:
    """
    Process the 2 input numbers using the given operator

    Args:
        number_1 (int): First number to be processed
        number_2 (int): Second number to be processed
        operator (str): Operator to be used to process the numbers

    Returns:
        str: The numbers and the operations recieved for processing
        int: the resultant from the operation

    Rises:
        ValueError: If "operator" not one of ['+', '-', '*']

    Examples:
        >>> process_numbers(12, 3, "+")
        ('12 + 3', 15)
        >>> process_numbers(12, 3, "-")
        ('12 - 3', 9)
        >>> process_numbers(12, 3, "*")
        ('12 * 3', 36)
    """
    problem_statement = f"{number_1} {operator} {number_2}"
    if operator == '+':
        problem_answer = number_1 + number_2
    elif operator == '-':
        problem_answer = number_1 - number_2
    else:
        problem_answer = number_1 * number_2
    return problem_statement, problem_answer

def get_total_number_of_questions() -> int:
    """
    Get the total number of questions that the user wants to answer

    Args: -

    Returns:
        int: The number of questions that the user wants to answer

    Rises:
        ValueError: If the user doesn't provide a natural number
    """
    while True:
        # Keep asking the user how many questions they want to answer - repeat the question if the answer is not a natural number
        try:
            no_questions = int(input("How many questions do you want to answer in total?\n"))
            if no_questions > 0:
                return no_questions
            else:
                print("That's not a natural number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a natural number.")


def math_quiz():
    """
    A math quiz where a user could choose the  number of questions to answer and gets a score based on the number of
    right answers.

    Args: -

    Returns: -

    Rises: -
    """
    score = 0
    total_questions = get_total_number_of_questions()

    print("Welcome to the Math Quiz Game!")
    print(f"You will be presented with {total_questions} math problems, and you have to provide the correct answers.")

    for _ in range(total_questions):
        number_1 = get_random_integer(1, 10)
        number_2 = get_random_integer(1, 5)
        operator = get_random_operator()

        problem, answer = process_numbers(number_1, number_2, operator)
        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
