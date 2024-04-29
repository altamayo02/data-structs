import copy
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


class Team(ISerializable):
	def __init__(
		self,
		id: str = None,
		group: str = "Z",
		name: str = "Los innombrables",
		stats: dict[Criterias, float] = {},
	) -> None:
		self.id = id
		if not id:
			self.id = f"T-{Random.random_alphanumerical(6)}"
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


class Cup(ISerializable):
	def __init__(
		self,
		ui_path: str,
		groups: dict[str, list[Team]] = {}
	) -> None:
		self.groups = groups
		if len(groups) == 0:
			self.groups = { chr(i): [] for i in range(ord("A"), ord("I")) }
		self.ui = QtUI(
			ui_path,
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
		self.jornadas: list[list[BinaryTree]] = []

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
			team = Team(
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

	def simulate_jornada(self, id_criteria: int):
		num_teams = self.count_teams()
		if num_teams != 32:
			self.ui.warn(f"Se requieren 32 equipos para simular la copa. Se han recibido: {num_teams}")
			return
		if len(self.jornadas) > 0:
			self.jornadas.append([])
			jornada = self.jornadas[-2]
			for t in range(0, len(jornada), 2):
				match = Match(jornada[t].get_node(), jornada[t + 1].get_node(), Criterias(id_criteria))

				if match.is_tied():
					goals = random.randint(0, 3)
					jornada[t].get_node().set_goals(goals)
					jornada[t + 1].get_node().set_goals(goals)
				else:
					goals = [0, 0]
					while goals[0] != goals[1]:
						goals = sorted([random.randint(1, 5) for _ in range(2)])
					jornada[t].get_node().set_goals(goals[0])
					jornada[t + 1].get_node().set_goals(goals[0])
					# Winner before upstreaming it in the tree
					lower_winner: Standing = [
						jornada[t].get_node(), jornada[t + 1].get_node()
					][match.get_winner_index()]
					lower_winner.set_goals(goals[1])
				bintree = BinaryTree(match.get_winner(), jornada[t], jornada[t + 1])
				print(bintree)
				self.jornadas[-1].append(bintree)
		else:
			self.jornadas.append([])
			for g in self.groups:
				group = self.groups[g]
				# To find the correct standing again, team is left outside
				standings = {team: Standing(team) for team in group}
				for t1 in range(len(group) - 1):
					for t2 in range(1 + t1, len(group)):
						match = Match(
							standings[group[t1]],
							standings[group[t2]],
							Criterias(id_criteria)
						)
				winners = sorted(standings.values(), key=lambda s: s.get_score())[:2:]
				for winner in winners:
					self.jornadas[0].append(BinaryTree(winner))
			print(len(self.jornadas))
		self.ui.update_jornadas(self.jornadas)
		print("Pendiente: Simular jornada")

	def show_brackets(self):
		print("Pendiente: Dibujar llaves")

	def load_data(self):
		data = self.ui.open_file()
		for group_id in data["groups"]:
			group: list[dict] = data["groups"][group_id]
			self.groups[group_id] = [Team(
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
	
	def count_teams(self) -> int:
		num_teams = 0
		for group in self.groups:
			num_teams += len(self.groups[group])
		return num_teams


class Standing(ISerializable):
	def __init__(self, team: Team = None, goals: int = 0, score: int = 0) -> None:
		self.team = team
		self.goals = goals
		self.score = score
	
	def get_team(self):
		return self.team
	
	def get_goals(self):
		return self.goals
	
	def get_score(self):
		return self.score

	def set_goals(self, goals: int):
		self.goals = goals

	def set_score(self, score: int):
		self.score = score

	def deep_copy(self):
		return copy.deepcopy(self)

	def __str__(self) -> str:
		return f"({self.get_goals()}, {self.get_score()}) {self.team.get_name()}"

class Match(ISerializable):
	def __init__(self, s1: Standing, s2: Standing, criteria: Criterias) -> None:
		self.criteria = criteria
		self.winner = None
		self.winner_index = None
		self.loser = None
		self.tie = False
		self._faceoff(s1, s2, criteria)
	
	def _faceoff(self, standing1: Standing, standing2: Standing, criteria: Criterias, definitive = False):
		crtr1 = standing1.get_team().get_stats()[criteria.name]
		crtr2 = standing2.get_team().get_stats()[criteria.name]
		if crtr1 > crtr2:
			self.winner = standing1
			self.loser = standing2
			self.winner_index = 0
		elif crtr1 < crtr2:
			self.winner = standing2
			self.loser = standing1
			self.winner_index = 1
		elif not definitive:
			self._faceoff(standing1, standing2, Criterias((criteria.value + 1) % 4), True)
			return
		else:
			self.tie = True
			self.winner_index = random.randint(0, 1)
			self.winner = [standing1, standing2][self.winner_index]
			self.winner.set_score(self.winner.get_score() + 1)
			return
		self.winner.set_score(self.winner.get_score() + 3)
	
	def get_criteria(self):
		return self.criteria
	
	def get_winner(self):
		return self.winner
	
	def get_winner_index(self):
		return self.winner_index

	def get_loser(self):
		return self.loser
	
	def is_tied(self):
		return self.tie