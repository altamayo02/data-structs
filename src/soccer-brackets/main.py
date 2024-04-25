import sys
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
	QApplication, QWidget, QTreeWidget, QTreeWidgetItem
)

from model.SoccerTeam import SoccerTeam, Criterias

class SoccerCupSimulator:
	def __init__(self, teams: list[SoccerTeam]) -> None:
		self.app, self.main_widget = self._load_ui()
		self.brackets = None

	def _load_ui(self) -> QWidget:
		ui_file = QFile("./src/soccer-brackets/ui/soccer-brackets.ui")
		if not ui_file.open(QIODevice.ReadOnly):
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
	
	def _load_csv(tree: QTreeWidget):
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

	def faceoff(self, t1: SoccerTeam, t2: SoccerTeam, criteria: str, definitive = False):
		c1, c2 = getattr(t1, criteria), getattr(t2, criteria)
		if c1 > c2:
			return t1
		elif c1 < c2:
			return t2
		else:
			return self.faceoff(t1, t2, "Criterias()", True)
		
	def show(self):
		self.main_widget.show()
		sys.exit(self.app.exec())

if __name__ == "__main__":
	scs = SoccerCupSimulator()
	