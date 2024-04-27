import sys
from PySide6.QtCore import QFile, QIODevice, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
	QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QPushButton, QComboBox,
	QLineEdit, QDoubleSpinBox, QLabel, QFileDialog
)
from PySide6.QtGui import QAction

from services.JsonService import JsonService


class QtUI:
	def __init__(
		self,
		ui_path: str,
		groups: dict[str, list],
		slots: dict[str, any]
	) -> None:
		# 1. UI Loader
		loader = QUiLoader()
		# 2. Application
		app = QApplication()

		self.json_service = JsonService(True)

		self.ui_path = ui_path
		self.app = app
		self.main_window = self.open_ui(loader, ui_path)
		self.warn_dialog = self.open_ui(loader, "./src/soccer-brackets/view/ui/warning.ui")
		self._bind_slots(slots)
		self.update_groups(groups)

	def open_ui(self, loader: QUiLoader, ui_path: str):
		ui_file = QFile(ui_path)
		if not ui_file.open(QIODevice.OpenModeFlag.ReadOnly):
			raise Exception(f"Cannot open file: {ui_file.errorString()}")
		
		widget = loader.load(ui_file)
		ui_file.close()

		if not widget:
			raise Exception(loader.errorString())
		return widget		

	def get_app(self) -> QApplication:
		return self.app

	def get_main_widget(self) -> QWidget:
		return self.main_window

	def get_team_form_data(self):
		from model.Soccer import Criterias
		return {
			"group": self.get_main_widget().findChild(QComboBox, "comboBoxGrupo").currentText(),
			"name": self.get_main_widget().findChild(QLineEdit, "lineEditNombre").text(),
			Criterias.ACCURACY.name: self.get_main_widget().findChild(
					QComboBox, "comboBoxPrecision").currentText(),
			Criterias.RESISTANCE.name: self.get_main_widget().findChild(
					QDoubleSpinBox, "doubleSpinBoxResistencia").value(),
			Criterias.SPEED.name: self.get_main_widget().findChild(QDoubleSpinBox, "doubleSpinBoxVelocidad").value(),
			Criterias.STRENGTH.name: self.get_main_widget().findChild(QDoubleSpinBox, "doubleSpinBoxFuerza").value()
		}

	def _bind_slots(self, slots: dict[str, any]) -> QWidget:
		btn_add: QPushButton = self.main_window.findChild(QPushButton, "pushButtonAgregar")
		btn_add.clicked.connect(slots["add"])

		btn_simulate: QPushButton = self.main_window.findChild(QPushButton, "pushButtonSimular")
		btn_simulate.clicked.connect(slots["sim"])

		btn_draw: QPushButton = self.main_window.findChild(QPushButton, "pushButtonVisualizar")
		btn_draw.clicked.connect(slots["draw"])

		actn_save: QAction = self.main_window.findChild(QAction, "actionGuardarCopaComo")
		actn_save.triggered.connect(slots["save"])

		actn_load: QAction = self.main_window.findChild(QAction, "actionCargarCopa")
		actn_load.triggered.connect(slots["load"])

	def update_groups(self, groups: list):
		tree_groups: QTreeWidget = self.main_window.findChild(QTreeWidget, "treeWidgetGrupos")
		tree_groups.sortByColumn(0, Qt.SortOrder.AscendingOrder)
		while tree_groups.topLevelItemCount() > 0:
			tree_groups.takeTopLevelItem(0)

		# Only for the static analyzer
		from model.Soccer import SoccerTeam
		groups: dict[str, list[SoccerTeam]] = groups
		for g in groups:
			tree_group = QTreeWidgetItem()
			tree_group.setText(0, g)
			for team in groups[g]:
				tree_team = QTreeWidgetItem()
				tree_team.setText(1, team.name)
				tree_group.addChild(tree_team)
			tree_groups.addTopLevelItem(tree_group)
		tree_groups.expandAll()

	def show(self):
		self.main_window.show()
		self.app.exec()
	
	def warn(self, message: str):
		warning: QLabel = self.warn_dialog.findChild(QLabel, "labelMessage")
		warning.setText(message)
		self.warn_dialog.show()
	
	def open_file(self):
		file = QFileDialog.getOpenFileName(
			self.main_window,
			"Cargar copa",
			"./src/soccer-brackets/",
			"Archivo JSON (*.json);;Todos los archivos (*.*)"
		)
		data = self.json_service.load_json(file[0])
		return data

	def save_file(self, data):
		file = QFileDialog.getSaveFileName(
			self.main_window,
			"Guardar copa",
			"./src/soccer-brackets",
			"Archivo JSON (*.json);;Todos los archivos (*.*)"
		)
		# File path only, without filter used
		self.json_service.save_json(file[0], data)
		return True
