#install pygame
import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
sleep(5)
pygame.mixer.init()
pygame.mixer.music.load('mothers day.mp3')
pygame.mixer.music.play()
sleep(8)
pygame.mixer.music.load('mothers day.mp3')
pygame.mixer.music.play()
image = pygame.image.load('mothers day final.jpg')
image = pygame.image.load('mothers-day-2019.jpg')
window.blit(image,(0,0))
pygame.display.update()
sleep(13)