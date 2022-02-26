import pygame
print("Musica: ")
pygame.init()
pygame.mixer.music.load('ex3/musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()
