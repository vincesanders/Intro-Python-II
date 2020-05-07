# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, art, items=None):
        self.name = name
        self.description = description
        self.art = art
        self.items = [] if items is None else items
    def __str__(self):
        return f'you are at the {self.name}. {self.description}'
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)