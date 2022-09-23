from string import ascii_lowercase

def get_input():

    QUESTIONS = {
        "When was the known use of the word 'quiz'": ["1781", "1771", "1871", "1881"],
        "What Language was this program built in": ["Python", "Java", "C", "GoLang"],
        "When was Travis Born": ["2002", "2003", "1999", "2000"],
        "How old is the White House": ["39", "69", "92", "145"]
    }

    num_of_correct_answers = 0
    for number, (question, options) in enumerate(QUESTIONS.items(), start=1):
        print(f"\nQuestion {number}:")
        print(f"{question}")
        correct_answer = options[0]
        labelled_options = dict(zip(ascii_lowercase, sorted(options)))
        for label, option in labelled_options.items():
            print(f" {label}) {option}")

        answer_label = input("\nChoice? ")
        answer = labelled_options.get(answer_label)
        if answer == correct_answer:
            num_of_correct_answers +=1
            print("⭐️Correct⭐")
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")

    print(f"\nYou got {num_of_correct_answers} correct out of {number} questions")


if __name__ == '__main__':
    get_input()







