import pygame
pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
sound= pygame.mixer.Sound('high.ogg')
#pygame.mixer.Sound.set_volume(1.0)
sound.play()
while True:
    continue
print("232")
