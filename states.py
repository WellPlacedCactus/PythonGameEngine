
import pygame
from ui import UIManager, UIObject
from entities import EntityManager, Player, Platform

class State:

	def __init__(self):
		self.kleft = False
		self.kright = False
		self.klctrl = False

		self.ui_manager = None
		self.entity_manager = None

	def tick(self):
		pass

	def draw(self, screen):
		pass


class StateManager:

	def __init__(self, states, index):
		self.states = states
		self.index = index

	def set_state(self, index):
		self.index = index

	def tick(self):
		self.states[self.index].tick()

	def draw(self, screen):
		self.states[self.index].draw(screen)

	def keydown(self, key):
		active_state = self.states[self.index]
		if key == pygame.K_LEFT:
			active_state.kleft = True
		if key == pygame.K_RIGHT:
			active_state.kright = True
		if key == pygame.K_LCTRL:
			active_state.klctrl = True

	def keyup(self, key):
		active_state = self.states[self.index]
		if key == pygame.K_LEFT:
			active_state.kleft = False
		if key == pygame.K_RIGHT:
			active_state.kright = False
		if key == pygame.K_LCTRL:
			active_state.klctrl = False

	def mousebuttonup(self):
		active_state = self.states[self.index]
		if active_state.ui_manager:
			active_state.ui_manager.mousebuttonup()


class MenuState(State):

	def __init__(self):
		super().__init__()
		self.ui_manager = UIManager()
		self.ui_manager.add(UIObject(100, 100, 50, 50,
			(255, 0, 0),
			(0, 255, 0),
			(0, 0, 255),
			lambda: print('o_O')))

	def tick(self):
		self.ui_manager.tick()

	def draw(self, screen):
		self.ui_manager.draw(screen)


class GameState(State):

	def __init__(self):
		super().__init__()
		self.entity_manager = EntityManager()
		self.entity_manager.add(Player(100, 100))
		self.add_bawx(-100, -100, 500, 500)

	def add_phorm(self, px, py, pw):
		self.entity_manager.add(Platform(px, py, pw, 5))

	def add_bawx(self, bx, by, bw, bh):
		self.entity_manager.add(Platform(bx, by, bw, 5))
		self.entity_manager.add(Platform(bx, by, 5, bh))
		self.entity_manager.add(Platform(bx + bw, by, 5, bh + 5))
		self.entity_manager.add(Platform(bx, by + bh, bw + 5, 5))

	def tick(self):
		self.entity_manager.tick(self)

	def draw(self, screen):
		self.entity_manager.draw(screen)


class DeathState(State):

	def __init__(self):
		super().__init__()

	def tick(self):
		pass

	def draw(self, screen):
		pass
