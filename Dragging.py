#Dragging a window
import pygame
pygame.init()

#Variables
x1=400
y1=400
window = pygame.display.set_mode([x1, y1])
drawing=True
border=False
a=0

##When you press the mouse at the border and the window updates,
##the computer thinks after the update that the mousebutton has just gone up.
##Thus, change_window is to make it so the computer responds to the second MOUSEBUTTONUP,
##not the first.
change_window=False

window.fill((255, 255, 255))
while drawing:
    x, y = pygame.mouse.get_pos()

    #if currently dragging
    if border:
        x1=x+difx
        y1=y+dify
        window=pygame.display.set_mode([x1, y1])
        window.fill((255, 255, 255)) #Here, you have to re-draw everything
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            drawing=False

        #if the right/bottom edges of the screen are pressed
        if event.type==pygame.MOUSEBUTTONDOWN and (x1-x<=20 or y1-y<=20):
            difx=x1-x
            dify=y1-y
            border=True

        #if you unpress the mouse
        if event.type==pygame.MOUSEBUTTONUP and change_window:
            change_window=False
            border=False
        #to fix the bug
        elif event.type==pygame.MOUSEBUTTONUP and change_window==False and border:
            change_window=True
            
    pygame.display.flip()
    
