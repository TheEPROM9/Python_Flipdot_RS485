import pygame

# Your game setup would go here
gameScreen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pygame Mouse Click - Test Game')

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
			print(f'Mouse clicked at {x} {y}')
pygame.quit()