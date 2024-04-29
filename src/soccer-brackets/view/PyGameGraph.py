from typing import Tuple
import random
import pygame as pg
from pygame._sdl2 import Window

from model.Cup import Cup
from model.BinaryTree import BinaryTree
from model.Standing import Standing


class PyGame:
	def __init__(self, window_size: Tuple[int, int] = (1280, 720), caption: str = ""):
		pg.init()
		pg.font.init()
		self.FONT = pg.font.Font(size=24)

		self.window = pg.display.set_mode(window_size, pg.RESIZABLE)
		Window.from_display_module().maximize()
		self.surfaces = {
			"bg": [
				pg.surface.Surface(self.window.get_size(), pg.SRCALPHA),
				pg.surface.Surface(self.window.get_size(), pg.SRCALPHA),
				pg.surface.Surface(self.window.get_size(), pg.SRCALPHA)
			],
			"fg": [
				pg.surface.Surface(self.window.get_size(), pg.SRCALPHA),
				pg.surface.Surface(self.window.get_size(), pg.SRCALPHA),
				pg.surface.Surface(self.window.get_size(), pg.SRCALPHA)
			]
		}
		self.clock = pg.time.Clock()
		self.lifespan = self.clock.tick()
		self.is_running = True
		self.is_paused = False
		if caption: pg.display.set_caption(caption)
	
	def game(self):
		text = self.FONT.render("game() is not yet implemented", True, "purple")
		self.window.blit(text, text.get_rect(center=self.window.get_rect().center))

	def run(self):
		while self.is_running:
			# If window is prompted to close
			if pg.event.get(pg.QUIT):
				self.is_running = False

			# Clear the canvas
			for layer in self.surfaces:
				for n in self.surfaces[layer]:
					n.fill((255, 255, 255, 0))
			self.window.fill("black")

			# Game logic
			self.game()
			
			# Update the canvas
			for layer in self.surfaces:
				for n in self.surfaces[layer]:
					self.window.blit(n, (0, 0))
			pg.display.update()

			if not self.is_paused:
				self.clock.tick()
				self.lifespan += self.clock.get_time()
			elif pg.event.get(pg.MOUSEBUTTONUP):
				self.is_paused = False
		pg.quit()

class PyGameGraph(PyGame):
	def __init__(
		self, cup: Cup, window_size: Tuple[int, int] = (1280, 720), caption: str = ""
	):
		super().__init__(window_size, caption)
		self.cup = cup
		self.tree: BinaryTree = self.cup.get_jornadas()[-1][0] if self.cup.get_jornadas() else None
	
	def game(self):
		if self.tree:
			self.tree.in_order(self.tree, self.draw_node)
			
	def draw_node(self, tree: BinaryTree, position: tuple[int] = (800, 450)):
		node: Standing = tree.get_node()
		label = node.get_team().get_name()
		position = (random.randint(100, 1600), position[1] - 50 * tree.height(tree))
		rect = pg.draw.circle(self.surfaces["bg"][0], "lime", position, 30, 3)
		font = self.FONT.render(f"{label}", True, "purple")
		self.surfaces["fg"][0].blit(font, font.get_rect(center=rect.center))

	def __str__(self):
		pass