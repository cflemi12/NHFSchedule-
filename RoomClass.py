"""
Class for rooms.
@author: Chase Fleming
@date: 4/23/17

Defines a room.

"""


class Room(object):

    """ Initiates a room. """

    def __init__(self, number):
        self.number = number
        self.rounds = []
        for i in range(8):
            roster = {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None, "i": None,
                      "j": None}
            self.rounds.append(roster)