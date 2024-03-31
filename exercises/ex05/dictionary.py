"""Dictionary ex05 assignment."""

__author__ = "730472183"


def invert(x_dict: dict[str, str]) -> dict[str, str]:
    """Inverts a given dictionary."""
    inverted_dict = {}
    for key, value in x_dict.items():
        if value in inverted_dict:
            raise KeyError("Duplicate value encountered")
        inverted_dict[value] = key
    return inverted_dict

        
def favorite_color(color_dict: dict[str, str]) -> str:
    """Returns the most frequently occurring color in the dictionary."""
    color_count: dict[str, int] = {}
    max_count = 0
    most_popular_color = ""

    for name in color_dict:
        color = color_dict[name]

        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

        if color_count[color] > max_count or (color_count[color] == max_count and color < most_popular_color):
            max_count = color_count[color]
            most_popular_color = color

    return most_popular_color


def count(values: list[str]) -> dict[str, int]:
    """Counts the frequencies of each unique value in the input list."""
    result_dict: dict[str, int] = {}

    for item in values:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1

    return result_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Categorizes words into lists based on the starting letter."""
    result_dict: dict[str, list[str]] = {}

    for word in words:
        if word and 'a' <= word[0].lower() <= 'z':
            first_letter = word[0].lower()

            if first_letter in result_dict:
                result_dict[first_letter].append(word)
            else:
                result_dict[first_letter] = [word]

    return result_dict


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> None:
    """Updates the attendance log with the new attendance information."""
    if day in attendance_log:
        if student not in attendance_log[day]:
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]