
'''

Written by Him Legend Nathan Vu

"the orange box"

Requirements
	- pygame (pip install pygame)

To Run
	- have python
	- go to this folder in a terminal
	- type 'python game.py'

To Exit
	- Press 'Esc'

'''

import pygame
from states import StateManager, MenuState, GameState, DeathState

class Game:

	WIDTH = 640
	HEIGHT = 480
	FPS = 60

	def __init__(self):
		self.screen = pygame.display.set_mode([Game.WIDTH, Game.HEIGHT])
		pygame.display.set_caption('the orange box')
		self.clock = pygame.time.Clock()
		self.state_manager = StateManager([
			MenuState(),
			GameState(),
			DeathState()
		], 1)
		self.start()

	def stop(self):
		self.running = False

	def start(self):
		self.running = True
		self.loop()

	def loop(self):
		while self.running:

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					self.running = False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.running = False
					self.state_manager.keydown(event.key)

				if event.type == pygame.KEYUP:
					self.state_manager.keyup(event.key)

				if event.type == pygame.MOUSEBUTTONUP:
					self.state_manager.mousebuttonup()

			self.tick()
			self.draw()
			self.clock.tick(Game.FPS)

		pygame.quit()

	def tick(self):
		self.state_manager.tick()

	def draw(self):
		self.screen.fill((0, 0, 0))
		self.state_manager.draw(self.screen)
		pygame.display.flip()

if __name__ == '__main__':
	Game()
