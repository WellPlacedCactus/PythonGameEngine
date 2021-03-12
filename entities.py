
import pygame

class Entity:

	def_width = 30
	def_height = 30

	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def tick(self, state):
		pass

	def draw(self, screen, camera):
		pass


class EntityManager:

	def __init__(self):
		self.entities = []
		self.camera = Camera()

	def add(self, e):
		self.entities.append(e)

	def tick(self, state):
		for entity in self.entities:
			entity.tick(state)

	def draw(self, screen):
		for entity in self.entities:
			entity.draw(screen, self.camera)


class Camera(Entity):
	
	def __init__(self):
		self.xx = 0
		self.yy = 0

	def center(self, entity):
		self.xx = entity.x - (640 - entity.w) / 2
		self.yy = entity.y - (480 - entity.h) / 2


class Player(Entity):

	def __init__(self, x, y):
		super().__init__(x, y, Entity.def_width, Entity.def_height)

		# strafe
		self.vx = 0
		self.vy = 0
		self.vm = 10
		self.acc = 1
		self.dec = self.acc

		# jump
		self.jp = 20
		self.cj = True

	def inp(self, state):

		if state.kleft:
			self.vx -= self.acc
			if self.vx < -self.vm:
				self.vx = -self.vm
		else:
			if self.vx < 0:
				self.vx += self.dec
				if self.vx > 0:
					self.vx = 0

		if state.kright:
			self.vx += self.acc
			if self.vx > self.vm:
				self.vx = self.vm
		else:
			if self.vx > 0:
				self.vx -= self.dec
				if self.vx < 0:
					self.vx = 0

		if state.klctrl:
			if self.cj:
				self.cj = False
				self.vy -= self.jp

	def move(self, state):
		self.vy += 1 # gravity

		self.x += self.vx

		for entity in state.entity_manager.entities:
			if type(entity) == Platform:
				if self.collision(self, entity):
					if self.vx < 0:
						if self.x < entity.x + entity.w:
							self.vx = 0
							self.x = entity.x + entity.w
					if self.vx > 0:
						if self.x + self.w > entity.x:
							self.vx = 0
							self.x = entity.x - self.w

		self.y += self.vy

		for entity in state.entity_manager.entities:
			if type(entity) == Platform:
				if self.collision(self, entity):
					if self.vy < 0:
						if self.y < entity.y + entity.h:
							self.y = entity.y + entity.h
							self.vy = 0
					if self.vy > 0:
						if self.y + self.h > entity.y:
							self.vy = 0
							self.y = entity.y - self.h
							self.cj = True

		if self.y + self.h > 450: # floor
			self.vy = 0
			self.y = 450 - self.h
			self.cj = True

	def tick(self, state):
		self.inp(state)
		self.move(state)
		state.entity_manager.camera.center(self)

	def draw(self, screen, camera):
		pygame.draw.rect(
			screen,
			(255, 255, 255),
			(self.x - camera.xx, self.y - camera.yy, self.w, self.h))

	def collision(self, r1, r2):
		if (r1.x < r2.x + r2.w and
			r1.x + r1.w > r2.x and
			r1.y < r2.y + r2.h and
			r1.y + r1.h > r2.y):
			return True
		else:
			return False


class Platform(Entity):

	def __init__(self, x, y, w, h):
		super().__init__(x, y, w, h)
	
	def tick(self, state):
		pass

	def draw(self, screen, camera):
		pygame.draw.rect(
			screen,
			(255, 144, 0),
			(self.x - camera.xx, self.y - camera.yy, self.w, self.h))
