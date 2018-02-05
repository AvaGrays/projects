import pygame
import random
import pygame.locals
import time
import smoothing


pygame.init()

C=pygame.time.Clock()

w=pygame.display.set_mode(([900,900]))
w.fill((255, 255, 255))
pygame.display.flip()

w.fill((255,255,255))

size=5

x1, y1=pygame.mouse.get_pos()
x2, y2=pygame.mouse.get_pos()

color=((0, 0, 0))

pos_x=10
pos_y=10

x=0
y=0

bk=((0,0,0))


#doc_size=int(input("How big do you want your screen, use commas: "))

#doc_size2=doc_size.split(",")

#print(doc_size2)

w=pygame.display.set_mode((900, 900))

tools=pygame.Rect(0, 0, 900, 40)
fill=[]
fill_point=0

w.fill((255, 255, 255))                       

print("press space to change color")
print("use up and down arrows to change size")
print("press the x to close")
drawing=False


playing=True
while playing:  
   
    
    
    cur_x,cur_y = pygame.mouse.get_pos()
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing=False
        
        if event.type == pygame.KEYDOWN:

            #ranodom color 
            if event.key == pygame.K_SPACE:

                r=random.randint(0, 255)
                g=random.randint(0, 255)
                b=random.randint(0, 255)

                
                
                color=((r, g, b))

                pygame.draw.circle(w, color, (pos_x, pos_y), size)

                pygame.display.flip()
                
                
            #the key controls
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                name=input(("Please name your document: "))
                pygame.image.save(w, name + ".jpeg")
                print(name, " was saved to your desktop.")

                
            elif event.key == pygame.K_UP:
                size+=5
                pos_x+=3
                pos_y+=3
                      
                pygame.display.flip()
            elif event.key == pygame.K_DOWN:
                size-=5
                pos_x-=3
                pos_y-=3
                          
                pygame.display.flip()
            elif event.key == pygame.K_LEFT:
                r_bk=random.randint(0, 255)
                g_bk=random.randint(0, 255)
                b_bk=random.randint(0, 255)

                bk=((r_bk, g_bk, b_bk))
                
                w.fill((bk))
                
                pygame.draw.rect(w, (200, 200, 200), tools)
        
                pygame.draw.circle(w, color, (pos_x, pos_y), size)        
    
                pygame.display.flip()
            elif event.key == pygame.K_RETURN:
                color=bk               
            
        #drawing the line w/ unlimited success             
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            x1,y1 = pygame.mouse.get_pos()
            x2,y2 = pygame.mouse.get_pos()           
            
            drawing = True
        elif pygame.mouse.get_pressed() == (1, 0, 0):            
            pygame.draw.line(w,(color),(x1,y1),(x2,y2),size*2)
            pygame.draw.circle(w, (color),(x1, y1), size)
            pygame.draw.circle(w, (color),(x2, y2), size)         
            
            x1,y1 = x2,y2
            
            x2,y2 = pygame.mouse.get_pos()
            pygame.display.flip()

        elif size < 5:
            size=5
        
        if event.type == pygame.MOUSEBUTTONUP:
            drawing=False             
            
            if len(fill) >  2:
                
                if abs(fill[0][0] - (fill[len(fill)-1][0]))<size:
                    print("I'm working")
                    print(fill[0], fill[len(fill)-1])
                    pygame.draw.polygon(w, color, fill)
                    smoothing.smooth(fill, 0)
                    pygame.display.flip()
                    fill=[]    
                    print("is it empty" + str(fill) )
                     
            fill=[]
            if len(fill) < 2:
                pygame.draw.circle(w, color, (x1, y1), size)
                pygame.display.flip()
            
                
        if event.type == pygame.MOUSEMOTION and drawing:
            fill_point = pygame.mouse.get_pos()
            #print(str(fill_point))
            fill_point = pygame.mouse.get_pos()
           
            fill.append(fill_point)

        
                                 
        

        pygame.draw.rect(w, (200, 200, 200), tools)
        
        pygame.draw.circle(w, color, (pos_x, pos_y), size)        
        
        if event.type == pygame.QUIT:
            playing = False
    
        C.tick(60)
