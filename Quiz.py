from string import ascii_lowercase
import random

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
        "When was the known use of the word 'quiz'": ["1781", "1771", "1871", "1881"],
        "What Language was this program built in": ["Python", "Java", "C", "GoLang"],
        "When was Travis Born": ["2002", "2003", "1999", "2000"],
        "How old is the White House": ["39", "69", "92", "145"],
        "What's the official name of the := operator": ["Assignment expression", "Named expression", "Walrus operator",
                                                        "Colon equals operator",
                                                        ]
    }


def get_answer(question, options):
    print(f"{question}")
    labelled_options = dict(zip(ascii_lowercase, random.sample(options, k=len(options))))
    for label, option in labelled_options.items():
        print(f" {label}) {option}")

    while (answer_label := input("\nChoice? ")) not in labelled_options:
        print(f"Please answer one of {', '.join(labelled_options)}")

    return labelled_options[answer_label]


def ask_question(question, options):
    correct_answer = options[0]
    ordered_options = random.sample(options, k=len(options))

    answer = get_answer(question, ordered_options)
    if answer == correct_answer:
        print("⭐️Correct⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0


def do_quiz():
    questions = prepare_questions(QUESTIONS, NUM_QUESTIONS_PER_QUIZ)

    number_of_correct = 0
    for number, (question, options) in enumerate(questions, start=1):
        print(f"\nQuestion {number}:")
        number_of_correct += ask_question(question, options)

    print(f"You got {number_of_correct} correct out of {number} questions")


def prepare_questions(questions, number_of_questions):
    number_of_questions = min(number_of_questions, len(questions))
    return random.sample(list(QUESTIONS.items()), k=number_of_questions)


if __name__ == '__main__':
    do_quiz()
