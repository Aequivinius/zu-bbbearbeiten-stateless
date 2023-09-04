from dataclasses import dataclass
from datetime import datetime

items = []


@dataclass
class Item:
    text: str
    date: datetime
    isCompleted: bool = False


def add(text, date):
    date = datetime.strptime(date, '%Y-%m-%d')
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    items.append(Item(text, date))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted



