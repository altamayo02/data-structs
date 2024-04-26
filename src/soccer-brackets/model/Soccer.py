from enum import Enum, auto
import random

from PySide6.QtWidgets import (
	QLineEdit, QComboBox, QDoubleSpinBox
)
from .BinaryTree import BinaryTree
from view.QtUI import QtUI



class Criterias(Enum):
	RESISTANCE = auto()
	STRENGTH = auto()
	SPEED = auto()
	ACCURACY = auto()


class SoccerTeam:
	def __init__(
		self,
		group: str,
		name: str = "Los innombrables",
		stats: dict[Criterias, float] = {},
	) -> None:
		self.name = name
		self.group = group
		self.stats = {}
		if len(stats) == 0:
			for i in range(1, len(Criterias) + 1):
				#self.stats[Criterias(i).name] = 0
				self.stats[Criterias(i).name] = random.randint(1, 10)
		else:
			self.stats = stats
	
	def __str__(self) -> str:
		return f"({self.group}) {self.name}: {self.stats}"


class SoccerCup:
	def __init__(self, ui_path: str, teams: list[SoccerTeam]) -> None:
		self.ui = QtUI(
			ui_path,
			self.add_team,
			self.simulate_jornada,
			self.show_brackets
		)
		self.teams = teams
		self.brackets = BinaryTree()

	def get_ui(self) -> QtUI:
		return self.ui

	def get_teams(self) -> list[SoccerTeam]:
		return self.teams

	def get_brackets(self) -> BinaryTree:
		return self.brackets

	def add_team(self):
		name = self.get_ui().get_main_widget().findChild(QLineEdit, "lineEditNombre").text()
		group = self.get_ui().get_main_widget().findChild(QComboBox, "comboBoxGrupo").currentText()

		accuracy = self.get_ui().get_main_widget().findChild(QComboBox, "comboBoxPrecision").currentText()
		resistance = self.get_ui().get_main_widget().findChild(QDoubleSpinBox, "doubleSpinBoxResistencia").value()
		speed = self.get_ui().get_main_widget().findChild(QDoubleSpinBox, "doubleSpinBoxVelocidad").value()
		strength = self.get_ui().get_main_widget().findChild(QDoubleSpinBox, "doubleSpinBoxFuerza").value()

		team = SoccerTeam(
			group,
			name,
			{
				Criterias.ACCURACY.name: accuracy,
				Criterias.RESISTANCE.name: resistance,
				Criterias.SPEED.name: speed,
				Criterias.STRENGTH.name: strength
			}
		)
		self.teams.append(team)
		self.get_ui().set_teams(self.teams)
		print(f"Pendiente: Agregar equipo {team}")

	def simulate_jornada(self):
		print("Pendiente: Simular jornada")

	def show_brackets(self):
		print("Pendiente: Dibujar llaves")

	def faceoff(self, t1: SoccerTeam, t2: SoccerTeam, criteria: Criterias, definitive = False):
		c1, c2 = t1.stats[criteria.name], t2.stats[criteria.name]
		print(c1, c2)
		if c1 > c2:
			return t1
		elif c1 < c2:
			return t2
		elif not definitive:
			return self.faceoff(t1, t2, Criterias((criteria.value + 1) % 4), True)
		else:
			return t1, t2