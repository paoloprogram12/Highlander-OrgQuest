from dataclasses import dataclass
import json


@dataclass
class Club:
    name: str
    labels: list[str]


def read_club_data(path: str) -> list[Club]:
    with open(path) as f:
        out = json.load(f)

    club_list = []
    for data in out:
        club = Club(data["name"], data["labels"])
        club_list.append(club)

    return club_list
