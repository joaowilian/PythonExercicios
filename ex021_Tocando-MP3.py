import pygame
pygame.mixer.init()
pygame.mixer.music.load('fun.mp3')
pygame.mixer.music.play(start=200)# tempo em segundos
input()