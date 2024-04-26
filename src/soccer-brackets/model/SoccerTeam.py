from enum import Enum, auto
import random


class Criterias(Enum):
	RESISTENCE = auto()
	STRENGTH = auto()
	SPEED = auto()
	PRECISION = auto()

class SoccerTeam:
	def __init__(self) -> None:
		self.stats: dict[Criterias, float] = {}
		for i in range(1, len(Criterias) + 1):
			self.stats[Criterias(i).name] = int(1 + 9 * random.random())