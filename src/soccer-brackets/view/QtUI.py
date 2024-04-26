import sys
from PySide6.QtCore import QFile, QIODevice, QObject
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
	QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QPushButton, QComboBox
)


class QtUI:
	def __init__(
		self,
		ui_path: str,
		add_method,
		sim_method,
		draw_method
	) -> None:
		self.ui_path = ui_path
		ui_file = QFile(ui_path)
		if not ui_file.open(QIODevice.OpenModeFlag.ReadOnly):
			raise Exception(f"Cannot open file: {ui_file.errorString()}")

		# 1. UI Loader
		loader = QUiLoader()
		# 2. Application
		self.app = QApplication()
		# 3. Widget
		self.main_widget = loader.load(ui_file)
		ui_file.close()

		if not self.main_widget:
			raise Exception(loader.errorString())

		self._bind(add_method, sim_method, draw_method)

	def get_app(self) -> QApplication:
		return self.app

	def get_main_widget(self) -> QWidget:
		return self.main_widget

	def _bind(self, add_slot, sim_slot, draw_slot) -> QWidget:
		btn_agregar: QPushButton = self.main_widget.findChild(QPushButton, "pushButtonAgregar")
		btn_agregar.clicked.connect(add_slot)

		btn_simular: QPushButton = self.main_widget.findChild(QPushButton, "pushButtonSimular")
		btn_simular.clicked.connect(sim_slot)

		btn_dibujar: QPushButton = self.main_widget.findChild(QPushButton, "pushButtonVisualizar")
		btn_dibujar.clicked.connect(draw_slot)

		tree: QTreeWidget = self.main_widget.findChild(QTreeWidget, "treeWidgetGrupos")
		#self._load_csv(tree)

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

	# TODO - No repetition
	def set_teams(self, teams: list):
		tree_groups: QTreeWidget = self.main_widget.findChild(QTreeWidget, "treeWidgetGrupos")
		while tree_groups.topLevelItemCount() > 0:
			tree_groups.takeTopLevelItem(0)

		# Only for the static analyzer
		from model.Soccer import SoccerTeam
		teams: list[SoccerTeam] = teams
		for t in teams:
			team = QTreeWidgetItem()
			team.setText(0, t.name)
			print(f"Hola {ord(t.group) - 65}")
			tree_groups.topLevelItem(ord(t.group) - 65).addChild(team)

	
	def show(self):
		self.main_widget.show()
		sys.exit(self.app.exec())