import pygame as pg, math
from typing import Tuple
from pygame._sdl2 import Window

pg.init()
pg.font.init()
FONT = pg.font.Font(size=24)
TABLE_UPDATE = pg.USEREVENT
CELL_SIZE = 20

class Queens:
	def __init__(
		self,
		screen_size: Tuple[int, int] = (854, 480),
		caption: str = "pygame-starter"
	):
		self.screen_size = screen_size
		self.screen = pg.display.set_mode(self.screen_size, pg.RESIZABLE)
		Window.from_display_module().maximize()
		self.clock = pg.time.Clock()
		self.timer = 0
		self.queens: list[list] = [(0, 0)]
		self.moves = [
			(-1, -1), (-1, 0), (-1, 1),
			(0, -1), (0, 1),
			(1, -1), (1, 0), (1, 1)
		]
		self.position = 0
		self.velocity = 0.05
		self.table: list[list] = []

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

		pg.display.set_caption(caption)
		self.clock.tick()
		# FIXME - This is called before table is updated- big trouble
		pg.time.set_timer(TABLE_UPDATE, int(0 * self.clock.get_time() * self.velocity))
		print(int(self.clock.get_time() * self.velocity), self.clock.get_time(), self.velocity)

	def game(self):
		self.position += self.clock.get_time() * self.velocity
		TABLE_SIZE = int(self.position / CELL_SIZE)
		
		# Update table
		if pg.event.get(TABLE_UPDATE):
			print("Event: Table update")
			def mark(i, j):
				self.table[i][j] = 2
				for m in self.moves:
					i1 = m[0]
					j1 = m[1]
					while self.is_valid(i + i1, j + j1):
						if self.table[i + i1][j + j1] == 0:
							self.table[i + i1][j + j1] = 1
						i1 += m[0]
						j1 += m[1]
			
			for i in range(TABLE_SIZE):
				self.table.append([])
				for j in range(TABLE_SIZE):
					self.table[i].append(0)
			
			for q in self.queens:
				i, j = q[0], q[1]
				mark(i, j)

			#self.print_table()

			for i in range(TABLE_SIZE):
				for j in range(TABLE_SIZE):
					# Personal preference
					#if self.table[i][j] == 0:
					if self.table[j][i] == 0:
						self.queens.append((j, i))
						mark(j, i)
		
		# Draw grid
		for i in range(TABLE_SIZE + 1):
			for j in range(TABLE_SIZE + 1):
				if self.is_valid(i, j):
					col = {
						0: "lime",
						1: "coral",
						2: "purple"
					}[self.table[i][j]]
					pg.draw.rect(self.surfaces["bg"][0], col, pg.rect.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE))
				if i == 0:
					# Trippy!
					#pg.draw.line(self.surfaces["bg"][1], "white", (10 * (j - 1), 0), (10 * j, 10 * (TABLE_SIZE - 1)))
					pg.draw.line(self.surfaces["bg"][1], "white", (j * CELL_SIZE, 0), (j * CELL_SIZE, TABLE_SIZE * CELL_SIZE))
			pg.draw.line(self.surfaces["bg"][1], "white", (0, i * CELL_SIZE), (TABLE_SIZE * CELL_SIZE, i * CELL_SIZE))

		# Draw scope
		pg.draw.rect(
			self.surfaces["fg"][-1],
			["teal", "purple", "coral", "deeppink"][TABLE_SIZE % 4],
			pg.Rect(-1, -1, self.position + 1, self.position + 1),
			3
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
		self.clock.tick()
		self.timer += self.clock.get_time()

	def run(self):
		while self.running:
			self.update()
		pg.quit()

	def is_valid(self, i, j):
		return 0 <= i < len(self.table) and 0 <= j < len(self.table[0])
	
	def print_table(self):
		for r in self.table:
			for c in r:
				col = {
					0: 32,
					1: 31,
					2: 35
				}[c]

				print(f"\u001B[{col}m{c}", end=" ")
			print()
		print("\u001B[0m---------------")


if __name__ == "__main__":
	game = Queens((900, 900), "Queens")
	game.run()