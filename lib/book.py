#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title
    @property
    def page_count(self):
        return self._page_count
    
    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
            # self.page_count = ""
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

Hary_potter = Book("Hary Potter", 272)
    
# print(Hary_potter.page_count)        