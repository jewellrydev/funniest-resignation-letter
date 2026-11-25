"""The Funniest One-Line Resignation Letter — a make.fun entry.

Prints exactly one line and nothing else, 140 characters at most:
the whole resignation letter.
"""

LINE = (
    "I quit, effective immediately — please forward all my "
    "unfinished work to the person who swore this job would look great on "
    "my resume."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 140, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
