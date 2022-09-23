def get_input():

    QUESTIONS = [
        ("When was the known use of the word 'quiz'", "1781"),
        ("What Language was this program built in", "Python"),
        ("When was Travis Born", "2002")
    ]

    for question, correct_answer in QUESTIONS:
        answer = input(f"{question}? ")

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")


if __name__ == '__main__':
    get_input()
