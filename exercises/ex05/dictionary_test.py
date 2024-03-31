"""Writing tests for the dictionary functions."""

__author__ = "730472183"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert() -> None:
    """A test of the invert function."""
    dict1: dict[str, str] = {"nuts": "bolts"}
    inverted_dict: dict[str, str] = {}
    inverted_dict = invert(dict1)
    assert inverted_dict == {"bolts": "nuts"}


def test_invert2() -> None:
    """A second test of the invert function."""
    dict1: dict[str, str] = {"bingo": "bongo"}
    inverted_dict: dict[str, str] = {}
    inverted_dict = invert(dict1)
    assert inverted_dict == {"bongo": "bingo"}


def test_invert3() -> None:
    """A third test of the invert function."""
    dict1: dict[str, str] = {"oh snap": "a hat", "crazy": "funky hat"}
    inverted_dict: dict[str, str] = {}
    inverted_dict = invert(dict1)
    assert inverted_dict == {"a hat": "oh snap", "funky hat": "crazy"}


def test_favorite_color() -> None:
    """A test of the favorite color function."""
    dict1: dict = {"Jared": "blue", "Susie": "blue", "Emma": "red"}
    most_popular_color: str = ""
    most_popular_color = favorite_color(dict1)
    assert most_popular_color == "blue"


def test_favorite_color2() -> None:
    """A second test of the favorite color function."""
    dict1: dict = {"Megan": "pink", "Jorge": "pink", "Pete": "pink", "Paco": "green"}
    most_popular_color: str = ""
    most_popular_color = favorite_color(dict1)
    assert most_popular_color == "pink"


def test_favorite_color3() -> None:
    """A third test of the favorite color function."""
    dict1: dict = {"Jose": "purple", "Mike": "emerald", "Tammy": "pink", "Neila": "emerald"}
    most_popular_color: str = ""
    most_popular_color = favorite_color(dict1)
    assert most_popular_color == "emerald"


def test_count() -> None:
    """A test of the count function."""
    values: list[str] = ["2", "bingo", "AHHHHH", "I'm tired", "2"]  
    result_dict: dict[str, int] = {}
    result_dict = count(values)  
    assert result_dict == {"2": 2, "bingo": 1, "AHHHHH": 1, "I'm tired": 1}


def test_count2() -> None:
    """A second test of the count function."""
    values: list[str] = ["beep", "boop", "beep", "boop", "beep"]  
    result_dict: dict[str, int] = {}
    result_dict = count(values)  
    assert result_dict == {"beep": 3, "boop": 2}


def test_count3() -> None:
    """A third test of the count function."""
    values: list[str] = ["yaba", "daba", "doo"]  
    result_dict: dict[str, int] = {}
    result_dict = count(values)  
    assert result_dict == {"yaba": 1, "daba": 1, "doo": 1}


def test_alphabetizer() -> None:
    """A test of the alphabetizer function."""
    words: list[str] = ["hey", "i'm", "sleepy"]
    result_dict: dict[str, list[str]] = {}
    result_dict = alphabetizer(words)
    assert result_dict == {"h": ["hey"], "i": ["i'm"], "s": ["sleepy"]}


def test_alphabetizer2() -> None:
    """A second test of the alphabetizer function."""
    words: list[str] = ["am", "are", "at", "be"]
    result_dict: dict[str, list[str]] = {}
    result_dict = alphabetizer(words)
    assert result_dict == {"a": ["am", "are", "at"], "b": ["be"]}


def test_alphabetize3() -> None:
    """A third test of the alphabetizer function."""
    words: list[str] = ["sneeze", "lousy", "ding"]
    result_dict: dict[str, list[str]] = {}
    result_dict = alphabetizer(words)
    assert result_dict == {"d": ["ding"], "l": ["lousy"], "s": ["sneeze"]}


def test_update_attendance() -> None:
    """A test for the update attendance function."""
    attendance_log: dict[str, list[str]] = {}
    day: str = "monday"
    student: str = "haley"
    update_attendance(attendance_log, day, student)
    assert attendance_log == {"monday": ["haley"]}


def test_update_attendance2() -> None:
    """A second test for the update attendance function."""
    attendance_log: dict[str, list[str]] = {}
    day: str = "tuesday"
    student: str = "harry, sally"
    update_attendance(attendance_log, day, student)
    assert attendance_log == {"tuesday": ["harry, sally"]}


def test_update_attendance3() -> None:
    """A third test for the update attendance function."""
    attendance_log: dict[str, list[str]] = {}
    day: str = "wednesday"
    student: str = "Anna"
    update_attendance(attendance_log, day, student)
    student2: str = "Anna"
    update_attendance(attendance_log, day, student2)
    assert attendance_log == {"wednesday": ["Anna"]}