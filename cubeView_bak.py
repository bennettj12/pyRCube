import rCube as R
import pygame
import time
import copy
from os import system,name
pygame.init()

def draw_rCube(cube,x,y):
    oXO = x
    oYO = y
    of = 1
    # DRAW FRONT
    for x in range(3):
        oY = oYO + x*30
        oX = oXO
        for y in range(3):
            xoffset = 25*y
            yoffset = 10*y
            color = R.cellColor(cube.green.cell(y,x)) 
            pygame.draw.polygon(screen,(color), [(oX + xoffset,oY + yoffset),(oX + 25 + xoffset,oY + 9 + yoffset),(oX + 25 + xoffset,oY + 40 + yoffset),(oX + xoffset,oY + 30 + yoffset)])
            pygame.draw.polygon(screen,(0,0,0), [(oX + xoffset,oY + yoffset),(oX + 25 + xoffset,oY + 9 + yoffset),(oX + 25 + xoffset,oY + 40 + yoffset),(oX + xoffset,oY + 30 + yoffset)],4)

    oXO +=75
    oYO += 60
    # DRAW RIGHT
    for x in range(3):
        oY = oYO + x*30
        oX = oXO
        for y in range(3):
            xoffset = 25*y
            yoffset = 10*y
            color = R.cellColor(cube.red.cell(y,x)) 
            pygame.draw.polygon(screen,(color), [(oX + xoffset,oY - yoffset),(oX + 25 + xoffset,oY - 9 - yoffset),(oX + 25 + xoffset,oY - 40 - yoffset),(oX + xoffset,oY - 30 - yoffset)])
            pygame.draw.polygon(screen,(0,0,0), [(oX + xoffset,oY - yoffset),(oX + 25 + xoffset,oY - 9 - yoffset),(oX + 25 + xoffset,oY - 40 - yoffset),(oX + xoffset,oY - 30 - yoffset)],4)
    oYO -=60
    oXO -=75
    oX = oXO
    oY = oYO
    # DRAW TOP
    
    for x in range(3):
        oY = oYO - x*10
        oX = oXO + x*25
        for y in range(3):
            xoffset = 25*y
            yoffset = 10*y
            if x == 2:
                xadj = 0
            elif x == 0:
                xadj = 2
            else:
                xadj = 1
            color = R.cellColor(cube.white.cell(y,xadj)) 
            pygame.draw.polygon(screen, (color), [(oX + xoffset,oY + yoffset),(oX+25 + xoffset,oY-10 + yoffset),(oX+50 + xoffset,oY + yoffset),(oX+25 + xoffset,oY+10 + yoffset)])
            pygame.draw.polygon(screen, (0,0,0), [(oX + xoffset,oY + yoffset),(oX+25 + xoffset,oY-10 + yoffset),(oX+50 + xoffset,oY + yoffset),(oX+25 + xoffset,oY+10 + yoffset)],4)


# Set up the drawing window
screen = pygame.display.set_mode([300, 300])

#set up clock
clock = pygame.time.Clock()
time_elapsed_since_last_action = 0
time_elapsed = 0

#make a rubix cube
cube = R.rCube()
totalMoveList = ['F','L','F','Ui','R','U','F','F','L','L','Ui','Li','B','Di','Bi','L','L','U']
animating = False # set to true to animate the above movelist 1 second after program start

listIndex = 0
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with grey
    screen.fill((128, 128, 128))

    # Draw cube
    draw_rCube(cube,75,100)
    #   This section handles animation of move sequences, it can be used by making sure your cube is 
    #   at the correct starting position, putting your move list into "totalMoveList", setting listIndex to 0,
    #   and setting "animating" to true. When the sequence has finished, "animating" will be set to false
    dt = clock.tick()
    time_elapsed_since_last_action += dt
    time_elapsed += dt
    if time_elapsed_since_last_action > 250 and not listIndex>len(totalMoveList)-1 and time_elapsed > 1000 and animating:
        cube.turn(totalMoveList[listIndex]) #make the turn of the cycle
        #   Clear screen and print text display of cube
        system('cls')
        cube.print()
        #   Increment index, check if last cycle of the list and set animating to false if so.
        listIndex += 1
        if(listIndex == len(totalMoveList)-1):
            animating = False
        #   Reset time since last action
        time_elapsed_since_last_action = 0


    # Flip the display
    pygame.display.flip()

#No longer running, 
pygame.quit()


