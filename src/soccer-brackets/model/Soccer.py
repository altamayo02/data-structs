from enum import Enum, auto
import random

from view.QtUI import QtUI
from services import Random
from .BinaryTree import BinaryTree
from .ISerializable import ISerializable


class Criterias(Enum):
	RESISTANCE = auto()
	STRENGTH = auto()
	SPEED = auto()
	ACCURACY = auto()


class SoccerTeam(ISerializable):
	def __init__(
		self,
		id: str = None,
		group: str = "Z",
		name: str = "Los innombrables",
		stats: dict[Criterias, float] = {},
	) -> None:
		self.id = id
		if not id:
			self.id = f"ST-{Random.random_alphanumerical(6)}"
		self.name = name
		self.group = group
		self.stats = {}
		if len(stats) == 0:
			for i in range(1, len(Criterias) + 1):
				#self.stats[Criterias(i).name] = 0
				self.stats[Criterias(i).name] = random.randint(1, 10)
		else:
			self.stats = stats
	
	def get_id(self):
		return self.id
	
	def get_name(self):
		return self.name
	
	def get_group(self):
		return self.group
	
	def get_stats(self):
		return self.stats

	def set_id(self, id):
		self.id = id

	def set_name(self, name):
		self.name = name

	def set_group(self, group):
		self.group = group

	def set_stats(self, stats):
		self.stats = stats
	
	def __str__(self) -> str:
		return f"({self.group}) {self.name}: {self.stats}"
	
	def to_dict(self):
		return {
			"id": self.id,
			"name": self.name,
			"stats": self.stats
		}


class SoccerCup(ISerializable):
	def __init__(
		self,
		path_to_initial_dialog: str,
		groups: dict[str, list[SoccerTeam]] = {}
	) -> None:
		self.groups = groups
		if len(groups) == 0:
			self.groups = { chr(i): [] for i in range(ord("A"), ord("I")) }
		self.ui = QtUI(
			path_to_initial_dialog,
			self.groups,
			{
				"add": self.add_team,
				"sim": self.simulate_jornada,
				"draw": self.show_brackets,
				"save": self.save_data,
				"load": self.load_data
			}
		)
		self.brackets = BinaryTree(1)
		self.brackets.set_left(BinaryTree(-2))
		self.brackets.set_right(BinaryTree(3))
		self.brackets.set_left(BinaryTree(-1))

	def get_ui(self) -> QtUI:
		return self.ui

	def get_groups(self) -> list[str]:
		return self.groups

	def get_brackets(self) -> BinaryTree:
		return self.brackets

	def add_team(self):
		data = self.ui.get_team_form_data()
		name = data["name"]
		group = data["group"]
		del data["name"]
		del data["group"]

		if len(self.groups[group]) < 4:
			team = SoccerTeam(
				group=group,
				name=name,
				stats=data
			)
			self.groups[group].append(team)
			self.ui.update_groups(self.groups)
		else:
			self.ui.warn(
				f"El equipo {group} ya tiene 4 integrantes. Ingrese el equipo a otro grupo."
			)

	def simulate_jornada(self):
		num_teams = self.count_teams()
		if num_teams != 32:
			self.ui.warn(f"Se requieren 32 equipos para simular la copa. Se han recibido: {num_teams}")
			return
		print("Pendiente: Simular jornada")

	def show_brackets(self):
		print("Pendiente: Dibujar llaves")

	def load_data(self):
		data = self.ui.open_file()
		for group_id in data["groups"]:
			group: list[dict] = data["groups"][group_id]
			self.groups[group_id] = [SoccerTeam(
				team["id"], group_id, team["name"], team["stats"]
			) for team in group]
		self.ui.update_groups(self.groups)

	def save_data(self):
		groups = {}
		for group in self.groups:
			groups[group] = [team.to_dict() for team in self.groups[group]]
		self.ui.save_file({
			"groups": groups,
			"brackets": self.brackets.to_dict()
		})

	def faceoff(self, t1: SoccerTeam, t2: SoccerTeam, criteria: Criterias, definitive = False):
		c1, c2 = t1.stats[criteria.name], t2.stats[criteria.name]
		if c1 > c2:
			return t1
		elif c1 < c2:
			return t2
		elif not definitive:
			return self.faceoff(t1, t2, Criterias((criteria.value + 1) % 4), True)
		else:
			return t1, t2
	
	def count_teams(self) -> int:
		num_teams = 0
		for group in self.groups:
			num_teams += len(self.groups[group])
		return num_teams