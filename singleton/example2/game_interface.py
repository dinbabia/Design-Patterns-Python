"""Game interface"""

from abc import ABCMeta, abstractmethod


class IGame(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def add_winner(position, name):
        """Must implement add_winner"""
