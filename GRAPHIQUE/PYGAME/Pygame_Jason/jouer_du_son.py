import pygame

"""
<Sound>.play(loop = 0, fadein = 2000)
       .stop()
       .fadeout(ms)
       .set_volume(0.0 => 1.0)
       .get_volume()
       .get_lenght()
"""

window_resolution = (640, 480)
launched = True

pygame.init()
pygame.display.set_caption("Jouer du son")
window_surface = pygame.display.set_mode(window_resolution)

# star_trek = pygame.mixer.Sound("star_trek.ogg")
# star_trek.play()

pygame.mixer.music.load("star_trek.mp3")
pygame.mixer.music.play()

pygame.display.flip()


while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.pause()
            elif event.key == pygame.K_p:
                pygame.mixer.unpause()