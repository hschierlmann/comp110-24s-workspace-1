"""Test my garden functions."""

__author__ = "730472183"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind() -> None:
    """Test the add_by_kind function."""
    garden: dict[str, list[str]] = {"trees": ["oak", "hickory"]}
    new_plant_kind: str = "trees"
    new_plant: str = "maple"
    add_by_kind(garden, new_plant_kind, new_plant)
    assert garden == {"trees": ["oak", "hickory", "maple"]}


def test_add_by_kind2() -> None:
    """Second add by kind test."""
    garden2: dict[str, list[str]] = {"fruit": ["mango", "orange"]}
    plant_kind: str = "nuts"
    new_plant_2: str = "almonds"
    add_by_kind(garden2, plant_kind, new_plant_2)
    assert garden2 == {"fruit": ["mango", "orange"], "nuts": ["almonds"]}


def test_add_by_kind3() -> None:
    """Third add by kind test."""
    garden3: dict[str, list[str]] = {"herbs": ["basil", "cilantro"]}
    plant_kind2: str = "herbs"
    new_plant_3: str = "thyme"
    add_by_kind(garden3, plant_kind2, new_plant_3)
    assert garden3 == {"herbs": ["basil", "cilantro", "thyme"]}


def test_add_by_date() -> None:
    """Tests add by date function."""
    garden: dict[str, list[str]] = {"June": ["basil", "carrots"]}
    new_plant_date: str = "August"
    new_plant: str = "kale"
    add_by_date(garden, new_plant_date, new_plant)
    assert garden == {"June": ["basil", "carrots"], "August": ["kale"]}


def test_add_by_date2() -> None:
    """Second add by date test."""
    garden2: dict[str, list[str]] = {"May": ["cucumber", "corn"]}
    new_plant_date2: str = "May"
    new_plant2: str = "squash"
    add_by_date(garden2, new_plant_date2, new_plant2)
    assert garden2 == {"May": ["cucumber", "corn", "squash"]}


def test_lookup_by_kind_and_date() -> None:
    """Testing the lookup by kind and date function."""
    kind_list: dict[str, list[str]] = {"herbs": ["basil", "thyme", "cilantro", "thyme"], "nut": ["almonds"], "trees": ["oak", "hickory", "maple"], "fruit": ["mango", "orange"], "vegetable": ["kale", "carrots", "cucumber", "corn", "squash"]}
    month_list: dict[str, list[str]] = {"June": ["basil", "carrots"], "August": ["kale"], "May": ["cucumber", "corn", "squash"]}
    lookup_by_kind_and_date(kind_list, month_list, "vegetable", "June")
    assert lookup_by_kind_and_date(kind_list, month_list, "vegetable", "June") == "vegetables to plant in June: ['carrots']"


def test_lookup_by_kind_and_date2() -> None:
    """Second lookup by kind and date test."""
    kind_list2: dict[str, list[str]] = {"herbs": ["basil", "thyme", "cilantro", "thyme"], "nut": ["almonds"], "trees": ["oak", "hickory", "maple"], "fruit": ["mango", "orange"], "vegetable": ["kale", "carrots", "cucumber", "corn", "squash"]}
    month_list2: dict[str, list[str]] = {"June": ["basil", "carrots"], "August": ["kale"], "May": ["cucumber", "corn", "squash"]}
    lookup_by_kind_and_date(kind_list2, month_list2, "nut", "May")
    assert lookup_by_kind_and_date(kind_list2, month_list2, "nut", "May") == "No nuts to plant in May."
    
