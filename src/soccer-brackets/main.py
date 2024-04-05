import sys
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
	QApplication, QWidget, QTreeWidget, QTreeWidgetItem
)


class Team:
	def __init__(self) -> None:
		pass


if __name__ == "__main__":
	ui_file = QFile("./src/soccer-brackets/ui/soccer-brackets.ui")
	if not ui_file.open(QIODevice.ReadOnly):
		print(f"Cannot open file: {ui_file.errorString()}")
		sys.exit(-1)

	# 1. UI Loader
	loader = QUiLoader()
	# 2. Application
	app = QApplication(sys.argv)
	# 3. Widget
	main_widget = loader.load(ui_file)
	ui_file.close()
	if not main_widget:
		print(loader.errorString())
		sys.exit(-1)

	canvas: QWidget = main_widget.findChild(QWidget, "centralWidget")
	tree: QTreeWidget = canvas.findChild(QTreeWidget, "treeWidgetGrupos")
	tree.expandAll()
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
	main_widget.show()
	sys.exit(app.exec())