import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GRAY = (80, 78, 81)

class Planet:
  AU = 149.6e6 * 1000 # AU = astronomical units
  G = 6.67428e-11
  SCALE = 250 / AU  # 1AU = 100 pixels
  TIMESTEP = 3600*24  # 1 day

  def __init__(self, x, y, radius, color, mass):
    self.x = x
    self.y = y
    self.radius = radius
    self.color = color
    self.mass = mass

    self.orbit = []
    self.sun = False
    self.distance_to_sun = 0

    self.x_vel = 0
    self.y_vel = 0

  def draw(self, win):
    x = self.x * self.SCALE + WIDTH / 2
    y = self.y * self.SCALE + HEIGHT / 2
    pygame.draw.circle(win, self.color, (x, y), self.radius)

def main():
  run = True
  clock = pygame.time.Clock()

  sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
  sun.sun = True

  mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GRAY, 3.3 * 10**23)

  venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)

  earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)

  mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)

  planets = [sun, mercury, venus, earth, mars]

  while run:
    clock.tick(60)
    # WIN.fill(WHITE)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    for planet in planets:
      planet.draw(WIN)
    
    pygame.display.update()


  pygame.quit()

main() 


