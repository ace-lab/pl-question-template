# server.py

import random

def generate(data):
    # Generate random parameters for the question and store them in the data["params"] dict:
    data["params"]["x"] = random.randint(5, 10)
    data["params"]["operation"] = random.choice(["double", "triple"])

    # Also compute the correct answer (if there is one) and store in the data["correct_answers"] dict:
    if data["params"]["operation"] == "double":
        data["correct_answers"]["y"] = 2 * data["params"]["x"]
    else:
        data["correct_answers"]["y"] = 3 * data["params"]["x"]

def prepare(data):
    # This function will run after all elements have run `generate()`.
    # We can alter any of the element data here, but this is rarely needed.
    pass

def parse(data):
    # data["raw_submitted_answer"][NAME] is the exact raw answer submitted by the student.
    # data["submitted_answer"][NAME] is the answer parsed by elements (e.g., strings converted to numbers).
    # data["format_errors"][NAME] is the answer format error (if any) from elements.
    # We can modify or delete format errors if we have custom logic (rarely needed).
    # If there are format errors then the submission is "invalid" and is not graded.

    # As an example, we will reject negative numbers for "y":
    if "y" not in data["format_errors"]: # check we don't already have a format error
        if data["submitted_answers"]["y"] < 0:
            data["format_errors"]["y"] = "Negative numbers are not allowed"

def grade(data):
    # All elements will have already graded their answers (if any) before this point.
    # data["partial_scores"][NAME] is the individual element scores (0 to 1).
    # data["score"] is the total score for the question (0 to 1).
    # We can modify or delete any of these if we have a custom grading method.
    # This function only runs if `parse()` did not produce format errors, so we can assume all data is valid.

    # grade() can also set `data['format_errors'][NAME]` if there is any reason to mark the question
    # invalid during grading time.  This will cause the question to not use up one of the student's attempts' on exams.

    # As an example, we will give half points for incorrect answers larger than "x":
    if data["score"] == 0: # only if not already correct
        if data["submitted_answers"]["y"] > data["params"]["x"]:
            data["partial_scores"]["y"] = 0.5
            data["score"] = 0.5
