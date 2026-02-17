import difflib


def detect_bug_line(incorrect_code: str, correct_code: str) -> int:
    incorrect_lines = incorrect_code.split("\n")
    correct_lines = correct_code.split("\n")

    diff = list(difflib.ndiff(incorrect_lines, correct_lines))

    line_number = 0
    for d in diff:
        if d.startswith("  "):
            line_number += 1
        elif d.startswith("- "):
            return line_number + 1

    return -1
