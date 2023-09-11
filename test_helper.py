import pytest
import helper
import datetime


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(text, date)

    # Then: The most recently added to-do should have a date
    item = helper.items[-1]
    assert isinstance(item.date, datetime.date)

def test_add_new_item():
   
    text = "Homework"
    date = "2023-09-05"

    helper.add(text, date)

  
    item = helper.items[-1]
    assert item.text == "Homework"
    assert item.date == datetime.date(2023, 9, 5)