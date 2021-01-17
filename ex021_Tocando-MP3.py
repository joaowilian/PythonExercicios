import pygame
pygame.init() # inicia o pygame
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(start=10)# tempo em segundos que começa
input() # inicia o mixer