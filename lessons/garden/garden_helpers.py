"""Some functions for my garden plan!"""

__author__ = "730472183"


def add_by_kind(plants_by_kind: dict[str, list[str]], plant_kind: str, plant: str) -> None:
    """Adds a plant to a garden dictionary, grouped by kind."""
    if plant_kind in plants_by_kind:
        plants_by_kind[plant_kind].append(plant)
    else:
        plants_by_kind[plant_kind] = [plant]


def add_by_date(plants_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Adds a plant to a garden dictionary, sorted by the date in which the seeds should be sown."""
    if month not in plants_by_date:
        plants_by_date[month] = [plant]
    else:
        plants_by_date[month].append(plant)


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], plant_kind: str, month: str) -> str:
    """Looks up plants of a certain kind sown on a certain date."""
    kind_list: list[str] = plants_by_kind[plant_kind]
    month_list: list[str] = plants_by_date[month]
    combined_list: list[str] = []
    if plant_kind not in plants_by_kind or month not in plants_by_date:
        return [] 
    for plant in kind_list:
        for other_plant in month_list:
            if plant == other_plant:  # plant is in both kind_list and month_list
                combined_list.append(other_plant)
    # "<kind>s to plant in <month>: <combined_list>"
    if len(combined_list) > 0:
        return f"{plant_kind}s to plant in {month}: {combined_list}"
    else:
        return f"No {plant_kind}s to plant in {month}."