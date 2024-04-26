import sys
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
	QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QPushButton
)

from model.Soccer import Criterias, SoccerCup, SoccerTeam


if __name__ == "__main__":
	team = SoccerTeam("A")
	print(team.stats)
	scs = SoccerCup("./src/soccer-brackets/view/soccer-brackets.ui", [team])
	print(scs.faceoff(SoccerTeam("A"), SoccerTeam("A"), Criterias.ACCURACY))
	scs.get_ui().show()