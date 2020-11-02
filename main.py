
# environment: pygameenv

import pygame as pg
import time
import random

WIDTH = 600
HEIGHT = 600

BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 30

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))	
pg.display.set_caption('Memory Game')
clock = pg.time.Clock()
pg.font.init()

BLANK = pg.image.load('images/blank.png').convert_alpha()
BG = pg.image.load('images/bg.png').convert_alpha()
 
images = []	
pair = []



class Boxes(pg.sprite.Sprite):
	def __init__(self, **kwargs):
		pg.sprite.Sprite.__init__(self)

		self.img = kwargs['img']
		self.name = kwargs['name']
		self.state = 'close'
		self.image = BLANK
		self.rect = self.image.get_rect()
		self.rect.center = (kwargs['cx'], kwargs['cy'])

	def show(self):
		global compare, piece_one

		self.image = self.img
		if len(pair) < 2:
			pair.append(self)
		

	def check(self):
		global pair

		if len(pair) == 2:
			if pair[0].name != pair[1].name:
				time.sleep(.50)
				pair[0].image = BLANK
				pair[1].image = BLANK
			else:
				pair[0].state = 'open'
				pair[1].state = 'open'

			pair = []
		
		
		
		
fruit = None
fruits = None


def init_tiles():
	global fruit, fruits
	fruit = pg.sprite.Group()
	fruits = []

	for i in range(2):
		for j in range(10):
			index = j + 1
			images.append(
				{'name': 'm{}'.format(index),
				'image': pg.image.load('images/m{}.png'.format(index))
				}
			)

	cx = 92
	for i in range(5):
		cy = 100
		for j in range(4):
			item = random.choice(images)
			lemon = Boxes(cx=cx, cy=cy, img=item['image'], name=item['name'])
			images.remove(item)
			fruit.add(lemon)
			fruits.append(lemon)
			cy += 104
		cx += 104

init_tiles()

screen.blit(BG, (0, 0))

running = True

while running:
	clock.tick(FPS)
	# screen.fill(BLACK)
	pg.display.flip()
	fruit.draw(screen)

	m = pg.mouse.get_pos()

	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False

		if event.type == pg.MOUSEBUTTONDOWN:
			for i in fruits:
				if i.rect.collidepoint(m):
					i.show()
		if event.type == pg.MOUSEBUTTONUP:
			for i in fruits:
				if i.rect.collidepoint(m):
					i.check()

	is_all_open	= 0		
	for f in fruits:
		if f.state == 'close':
			is_all_open += 1

	if is_all_open == 0:
		fruit = pg.sprite.Group()

					
					
pg.quit()

