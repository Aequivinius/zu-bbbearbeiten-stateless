from dataclasses import dataclass

items = []


@dataclass
class Item:
    text: str
    date: str
    isCompleted: bool = False


def add(text, date):
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    items.append(Item(text, date))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted


def sort_by_date():
    global items
    items = sorted(items, key=lambda x: x.date)