def get_input():
    answer = input("When was the known use of the word 'quiz'? ")

    if answer == "1781":
        print("Correct!")
    else:
        print(f"The answer is '1781', not {answer!r}")

    answer = input("What Language was this program built in? ")

    if answer == "Python":
        print("Correct")
    else:
        print(f"This Program was built in 'Python', not {answer!r}")

    answer = input("When was Travis Born?")

    if answer == "2002":
        print("Correct!")
    else:
        print(f"Travis was born in '2002', not in {answer!r}")


if __name__ == '__main__':
    get_input()