from PIL import Image
import numpy as np
import math
import pygame

img = Image.open('Assets\\testboi1.jpg')
new_width = (img.width*90)//img.height
img = img.resize((new_width,90))
imarr = np.array(img)
print(imarr.shape)

density = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*',
'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O',
'0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u',
'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1',
'{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i',
'!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ',
 ' ', ' ', ' ', ' ']


X = img.width*7
Y = img.height*7
pygame.init()
screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption("Image To Ascii")

font = pygame.font.SysFont('Courier New',10)



done = False
while not done:
    c = 0
    for i in range(imarr.shape[0]):
        s = ''
        for j in range(imarr.shape[1]):
            b_val = imarr[i][j][0]//3 + imarr[i][j][1]//3 + imarr[i][j][2]//3
            index = math.floor((len(density)-1)*(1 - (b_val/255)))
            s+=density[index]
            #print(density[index],end='')
        text = font.render(s, True, (255,255,255))
        textRect = text.get_rect()
        textRect.center = ((X//2,c))
        screen.blit(text,textRect)
        c+=8
        #print()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
    pygame.display.update()
