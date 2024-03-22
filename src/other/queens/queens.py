import pygame as pg, math
from typing import Tuple
#from pygame._sdl2 import Window

pg.font.init()
FONT = pg.font.Font(size=24)

class Queens:
	def __init__(
		self,
		screen_size: Tuple[int, int] = (854, 480),
		caption: str = "pygame-starter",
		tick_speed: int = 60,
	):
		pg.init()
		pg.display.set_caption(caption)
		pg.time.set_timer(pg.USEREVENT, 1000)

		self.screen_size = screen_size
		self.screen = pg.display.set_mode(self.screen_size, pg.RESIZABLE)
		#Window.from_display_module().maximize()
		self.clock = pg.time.Clock()
		self.tick_speed = tick_speed
		self.timer = 0
		self.queens: list[list] = [[0]]

		self.running = True
		self.surfaces = {
			"bg": [
				pg.surface.Surface(self.screen.get_size(), pg.SRCALPHA),
				pg.surface.Surface(self.screen.get_size(), pg.SRCALPHA),
				pg.surface.Surface(self.screen.get_size(), pg.SRCALPHA)
			],
			"fg": [
				pg.surface.Surface(self.screen.get_size(), pg.SRCALPHA),
				pg.surface.Surface(self.screen.get_size(), pg.SRCALPHA),
				pg.surface.Surface(self.screen.get_size(), pg.SRCALPHA)
			]
		}

	def game(self):
		TABLE_SIZE = self.timer // 1000

		# Draw grid
		for i in range(len(self.queens)):
			for j in range(len(self.queens)):
				if i == 0:
					# Trippy!
					# pg.draw.line(self.surfaces["bg"][0], "white", (10 * (j - 1), 0), (10 * j, 10 * len(self.queens)))
					pg.draw.line(self.surfaces["bg"][0], "white", (10 * j, 0), (10 * j, 10 * (len(self.queens) - 1)))
			pg.draw.line(self.surfaces["bg"][0], "white", (0, 10 * i), (10 * (len(self.queens) - 1), 10 * i))
		
		# Update matrix
		if pg.event.get(pg.USEREVENT):
			for r in self.queens:
				print(r)
			print("---")

			def mark(i, j):
				for i1 in range(len(self.queens)):
					if i1 != i: self.queens[i1][j] = 1
				for j1 in range(len(self.queens)):
					if j1 != j: self.queens[i][j1] = 1

			for i in range(len(self.queens)):
				for j in range(len(self.queens)):
					if self.queens[i][j] == 0:
						self.queens[i][j] = 2
						mark(i, j)
				self.queens[i].append(0)
			self.queens.append(len(self.queens[0]) * [0])
		
		# Draw scope
		pg.draw.rect(
			self.surfaces["fg"][-1],
			["teal", "purple", "coral", "deeppink"][self.timer // 1000 % 4],
			pg.Rect(0, 0, self.timer // 100, self.timer // 100),
			2
		)


	def reset_screen(self):
		"""
		fill the screen with black
		"""
		for layer in self.surfaces:
			for n in self.surfaces[layer]:
				n.fill((255, 255, 255, 0))
		self.screen.fill("black")

	def update(self):
		"""
		run one update cycle
		"""
		# If window is prompted to close
		if pg.event.get(pg.QUIT):
			self.running = False
		self.reset_screen()
		self.game()
		for layer in self.surfaces:
			for n in self.surfaces[layer]:
				self.screen.blit(n, (0, 0))
		pg.display.update()
		self.clock.tick(self.tick_speed)
		self.timer += self.clock.get_time()

	def run(self):
		"""
		run update at the specified tick_speed, until exit.
		"""
		while self.running:
			self.update()
		pg.quit()


if __name__ == "__main__":
	game = Queens((900, 900), "Queens", math.inf)
	game.run()