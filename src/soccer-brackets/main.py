import sys
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
	QApplication, QWidget, QTreeWidget, QTreeWidgetItem
)

from model.SoccerTeam import SoccerTeam, Criterias

class SoccerCupSimulator:
	def __init__(self, teams: list[SoccerTeam]) -> None:
		# Only declared for the static analyzer
		self.app: QApplication
		self.main_widget: QWidget

		self.app, self.main_widget = self._load_ui("./src/soccer-brackets/ui/soccer-brackets.ui")
		self.brackets = None

	def _load_ui(self, ui_path: str) -> QWidget:
		ui_file = QFile(ui_path)
		if not ui_file.open(QIODevice.OpenModeFlag.ReadOnly):
			raise Exception(f"Cannot open file: {ui_file.errorString()}")

		# 1. UI Loader
		loader = QUiLoader()
		# 2. Application
		app = QApplication()
		# 3. Widget
		main_widget = loader.load(ui_file)
		ui_file.close()

		if not main_widget:
			raise Exception(loader.errorString())

		canvas: QWidget = main_widget.findChild(QWidget, "centralWidget")
		tree: QTreeWidget = canvas.findChild(QTreeWidget, "treeWidgetGrupos")
		self._load_csv(tree)

		return app, main_widget
	
	def _load_csv(self, tree: QTreeWidget):
		for g in range(tree.topLevelItemCount()):
			while(True):
				grupo: QTreeWidgetItem = tree.topLevelItem(g)
				# Nuevo grupo
				# tree.children().append()
				# Nuevo equipo
				equipo = QTreeWidgetItem()
				equipo.setText(0, "Colombia")
				grupo.addChild(equipo)
				if grupo.childCount() == 4: break
		tree.expandAll()

	def faceoff(self, t1: SoccerTeam, t2: SoccerTeam, criteria: Criterias, definitive = False):
		c1, c2 = t1.stats[criteria.name], t2.stats[criteria.name]
		if c1 > c2:
			return t1
		elif c1 < c2:
			return t2
		elif not definitive:
			return self.faceoff(t1, t2, Criterias(criteria.value + 1 % 4), True)
		else:
			return t1, t2
		
	def show(self):
		self.main_widget.show()
		sys.exit(self.app.exec())

if __name__ == "__main__":
	team = SoccerTeam()
	print(team.stats)
	scs = SoccerCupSimulator([])
	print(scs.faceoff(SoccerTeam(), SoccerTeam(), Criterias.PRECISION))
	scs.show()