import pygame
import math

pygame.init()
window_dimensions = (1200, 500)
win = pygame.display.set_mode(window_dimensions)
pygame.display.set_caption("projectile")

class Projectile(object):
	def __init__(self, x, y, color,radius):
		self.x = x
		self.y = y
		self.color = color
		self.radius = radius

	def draw(self, win):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
		pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius-3)

	@staticmethod
	def ball_path(startx, starty, power, ang, time):
		velx = math.cos(angle) * power
		vely = math.sin(angle) * power
		distx = velx * time
		disty = vely * time - 2.45 * time**2
		newx = round(startx + distx)
		newy = round(starty - disty)

		return (newx, newy)

def redraw_window():
    win.fill((44, 44, 44))
    my_projectile.draw(win)
    pygame.draw.line(win, (0, 0, 0), line[0], line[1])
    pygame.display.update()

def find_angle(pos):
    sX = my_projectile.x
    sY = my_projectile.y
    try: angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except: angle = math.pi / 2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle

    return angle

# mainloop
my_projectile = Projectile(200, 480, (255, 255, 255), 8)

x = 0
y = 0
power = 0
angle = 0
time = 0
shoot = False
# clock = pygame.time.Clock()
run = True
while run:
	# clock.tick(200)
	if shoot:
		if my_projectile.y < 500 - my_projectile.radius:
			time += 0.04
			new_pos = Projectile.ball_path(x, y, power, angle, time)
			my_projectile.x = new_pos[0]
			my_projectile.y = new_pos[1]
		else:
			shoot = False
			time = 0
			my_projectile.y = 480

	line = [(my_projectile.x, my_projectile.y), pygame.mouse.get_pos()]

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if not shoot:
				shoot = True
				x = my_projectile.x
				y = my_projectile.y
				power = math.sqrt((line[1][1]-line[1][0])**2+(line[0][1]-line[0][0])**2)/12
				time = 0
				angle = find_angle(pygame.mouse.get_pos())
	redraw_window()

pygame.quit()
