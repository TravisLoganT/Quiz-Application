from string import ascii_lowercase
import random
import pathlib
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"


def get_answer(question, options):
    print(f"{question}")
    labelled_options = dict(zip(ascii_lowercase, random.sample(options, k=len(options))))
    for label, option in labelled_options.items():
        print(f" {label}) {option}")

    while (answer_label := input("\nChoice? ")) not in labelled_options:
        print(f"Please answer one of {', '.join(labelled_options)}")

    return labelled_options[answer_label]


def ask_question(question):
    correct_answer = question["answer"]
    options = [question["answer"]] + question["options"]
    ordered_options = random.sample(options, k=len(options))

    answer = get_answer(question["question"], ordered_options)
    if answer == correct_answer:
        print("⭐️Correct⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0


def do_quiz():
    questions = prepare_questions(QUESTIONS_PATH, NUM_QUESTIONS_PER_QUIZ)

    number_of_correct = 0
    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {number}:")
        number_of_correct += ask_question(question)

    print(f"You got {number_of_correct} correct out of {number} questions")


def prepare_questions(path, number_of_questions):
    questions = tomllib.loads(path.read_text())["questions"]
    number_of_questions = min(number_of_questions, len(questions))
    return random.sample(list(questions), k=number_of_questions)


if __name__ == '__main__':
    do_quiz()
