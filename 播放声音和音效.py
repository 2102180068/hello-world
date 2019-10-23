"""
   作者：周
   时间：2019/10/10
   功能：
"""

import pygame
import  sys
from pygame.locals import *


pygame.init()
pygame.mixer.init()

#播放背景音乐
pygame.mixer.music.load('bg_music.ogg')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

#加载猫叫
cat_sound = pygame.mixer.Sound('cat.wav')
cat_sound.set_volume(0.2)
#加载狗叫
dog_sound = pygame.mixer.Sound('dog.wav')
dog_sound.set_volume(0.2)

#设置窗口
bg_size = width,height = 300,200
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('~~')

pause = False

#加载、设置暂停播放按钮
pause_image = pygame.image.load('pause.png').convert_alpha()
unpause_image = pygame.image.load('unpause.png').convert_alpha()

pause_rect = pause_image.get_rect()
pause_rect.left,pause_rect.top = (width-pause_rect.width)//2,(height-pause_rect.height)//2

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            #鼠标左键，播放猫叫
            if event.button == 1:
                cat_sound.play()

            #鼠标右键，播放狗叫
            if event.button == 3:
                dog_sound.play()

        if event.type == KEYDOWN:

            if event.key == K_SPACE:
                pause = not pause

    screen.fill((255,255,255))
    if pause:
        screen.blit(pause_image,pause_rect)
        pygame.mixer.music.pause()
    else:
        screen.blit(unpause_image, pause_rect)
        pygame.mixer.music.unpause()

    pygame.display.flip()
    clock.tick(30)








