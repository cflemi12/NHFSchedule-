"""
Class for side event rooms.
@author: Chase Fleming
@date: 4/23/17

Defines a side event room. 

"""

from RoomClass import Room


class SideEventRoom(Room):
    """ Initiates a side event room. """

    def __init__(self, number, name, schedule):
        super(Room, self).__init__()
        self.name = name
        self.number = number
        self.schedule = schedule
        self.rounds = []
        for i in range(2):
            self.rounds.append([])
