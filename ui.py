
import pygame

class UIObject:

	def __init__(self, x, y, w, h, cidle, chover, cactive, clickfunc):
		self.x = x
		self.y = y
		self.w = w
		self.h = h

		self.cidle = cidle
		self.chover = chover
		self.cactive = cactive

		self.clickfunc = clickfunc
		self.c = cidle

	def tick(self):
		mx, my = pygame.mouse.get_pos()
		b1, b2, b3 = pygame.mouse.get_pressed(num_buttons=3)
		if (mx > self.x and
			my > self.y and
			mx < self.x + self.w and
			my < self.y + self.h):
			if b1:
				self.c = self.cactive
			else:
				self.c = self.chover
		else:
			self.c = self.cidle

	def draw(self, screen):
		pygame.draw.rect(
			screen,
			self.c,
			(self.x, self.y, self.w, self.h))

	def mousebuttonup(self):
		mx, my = pygame.mouse.get_pos()
		if (mx > self.x and
			my > self.y and
			mx < self.x + self.w and
			my < self.y + self.h):
			self.clickfunc()

class UIManager:

	def __init__(self):
		self.objects = []

	def add(self, obj):
		self.objects.append(obj)

	def tick(self):
		for obj in self.objects:
			obj.tick()

	def draw(self, screen):
		for obj in self.objects:
			obj.draw(screen)

	def mousebuttonup(self):
		for obj in self.objects:
			obj.mousebuttonup()
