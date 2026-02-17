from server.mcp_server import retriever
import re


def detect_bug_type(buggy_line: str, correct_line: str) -> tuple:
    """
    Detect C++ bug type and return:
    (bug_category, error_type, detailed_reason)
    """

    # Assignment inside condition
    if "if" in buggy_line and "=" in buggy_line and "==" not in buggy_line:
        return (
            "Assignment in Condition",
            "Logical Error",
            "The condition uses '=' instead of '=='. "
            "This performs assignment instead of comparison, "
            "which changes the variable value and always evaluates to true if non-zero."
        )

    # Uninitialized variable
    if re.search(r'\bint\s+\w+\s*;', buggy_line):
        return (
            "Uninitialized Variable",
            "Undefined Behavior",
            "A variable is declared but not initialized. "
            "Using an uninitialized variable leads to unpredictable values "
            "because it contains garbage memory."
        )

    # Division by zero
    if "/" in buggy_line and "0" in buggy_line:
        return (
            "Division by Zero",
            "Runtime Error",
            "Dividing by zero causes runtime failure and undefined behavior in C++."
        )

    # Missing return
    if "return" not in buggy_line and "return" in correct_line:
        return (
            "Missing Return Statement",
            "Undefined Behavior",
            "The function does not return a value despite having a non-void return type. "
            "This causes undefined behavior."
        )

    # Generic logic mismatch
    if buggy_line != correct_line:
        return (
            "Logic Mismatch",
            "Logical Error",
            "The logic differs from the correct implementation, "
            "causing incorrect output or incorrect computation."
        )

    return (
        "Unknown Issue",
        "Logical Error",
        "The statement differs from expected behavior."
    )


def generate_explanation(incorrect_code: str, correct_code: str, bug_line: int) -> str:

    incorrect_lines = incorrect_code.split("\n")
    correct_lines = correct_code.split("\n")

    buggy_line = incorrect_lines[bug_line - 1] if bug_line > 0 else ""
    correct_line = correct_lines[bug_line - 1] if bug_line > 0 else ""

    bug_category, error_type, reason = detect_bug_type(buggy_line, correct_line)

    # Retrieve documentation context
    nodes = retriever.retrieve(buggy_line)
    context_text = ""
    for n in nodes[:2]:
        context_text += n.get_text() + "\n"

    explanation = f"""
Bug Detected at Line {bug_line}

Incorrect Statement:
{buggy_line}

Correct Statement:
{correct_line}

Bug Category:
{bug_category}

Error Type:
{error_type}

Why This Is an Error:
{reason}

Impact:
This issue may cause incorrect output, unexpected behavior,
or program instability depending on execution flow.

Technical Reference (Retrieved from Documentation):
{context_text[:500]}

How It Is Fixed:
The corrected statement restores the intended logic
and ensures the program behaves as expected.
""".strip()

    return explanation
