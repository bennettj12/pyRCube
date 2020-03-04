import rCube as R
import pygame
import time
import copy
from os import system,name

def draw_rCube(cube,x,y,of):
    oXO = x
    oYO = y
    
    # DRAW FRONT
    for x in range(3): # x is y, y is x actually...
        oY = oYO + x*30*of # Y offset is the original Y plus 30* the row of the side we are on.
        oX = oXO # For each row on the front, there doesn't need to be any X offset.
        for y in range(3):
            xoffset = 25*y*of
            yoffset = 10*y*of
            color = R.cellColor(cube.green.cell(y,x)) 
            pygame.draw.polygon(screen,(color), [(oX + xoffset,oY + yoffset),(oX + 25*of + xoffset,oY + 10*of + yoffset),(oX + 25*of + xoffset,oY + 40*of + yoffset),(oX + xoffset,oY + 30*of + yoffset)])
            pygame.draw.polygon(screen,(0,0,0), [(oX + xoffset,oY + yoffset),(oX + 25*of + xoffset,oY + 10*of + yoffset),(oX + 25*of + xoffset,oY + 40*of + yoffset),(oX + xoffset,oY + 30*of + yoffset)],4)

    oXO +=75*of
    oYO += 60*of
    # DRAW RIGHT
    for x in range(3):
        oY = oYO + x*30*of
        oX = oXO
        for y in range(3):
            xoffset = 25*y*of
            yoffset = 10*y*of
            color = R.cellColor(cube.red.cell(y,x)) 
            pygame.draw.polygon(screen,(color), [(oX + xoffset,oY - yoffset),(oX + 25*of + xoffset,oY - 10*of - yoffset),(oX + 25*of + xoffset,oY - 40*of - yoffset),(oX + xoffset,oY - 30*of - yoffset)])
            pygame.draw.polygon(screen,(0,0,0), [(oX + xoffset,oY - yoffset),(oX + 25*of + xoffset,oY - 10*of - yoffset),(oX + 25*of + xoffset,oY - 40*of - yoffset),(oX + xoffset,oY - 30*of - yoffset)],4)
    oYO -=60*of
    oXO -=75*of
    oX = oXO
    oY = oYO
    # DRAW TOP
    
    for x in range(3):
        oY = oYO - x*10*of
        oX = oXO + x*25*of
        for y in range(3):
            xoffset = 25*y*of
            yoffset = 10*y*of
            if x == 2:
                xadj = 0
            elif x == 0:
                xadj = 2
            else:
                xadj = 1
            color = R.cellColor(cube.white.cell(y,xadj)) 
            pygame.draw.polygon(screen, (color), [(oX + xoffset,oY + yoffset),(oX+25*of + xoffset,oY-10*of + yoffset),(oX+50*of+ xoffset,oY + yoffset),(oX+25*of + xoffset,oY+10*of + yoffset)])
            pygame.draw.polygon(screen, (0,0,0), [(oX + xoffset,oY + yoffset),(oX+25*of + xoffset,oY-10*of + yoffset),(oX+50*of + xoffset,oY + yoffset),(oX+25*of + xoffset,oY+10*of + yoffset)],4)
def randomizeCube():
    return True
    
##############################################################
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1280, 600])
pygame.display.set_caption('Cube Viewer')

#make a rubix cube
cube = R.rCube()

# Backpath is a stack that holds the inverse of the moves made, so popping off the stack would give the correct
# sequence of moves to solve the cube without any fancy algorithms.
backPath = [] 



#Configuring Buttons
font = pygame.font.Font('freesansbold.ttf', 32) 
white = (255, 255, 255) 


leftBtn = pygame.Rect(850+75,50,150,50)
lbText = font.render('L', True, white) 
lbTextRect = lbText.get_rect()
lbTextRect.center = (1000, 75)

leftiBtn = pygame.Rect(1015+75,50,150,50)
libText = font.render("L'", True, white) 
libTextRect = libText.get_rect()
libTextRect.center = (1165, 75) 

rightBtn = pygame.Rect(850+75,50+(65*1),150,50)
rbText = font.render('R', True, white) 
rbTextRect = rbText.get_rect()
rbTextRect.center = (1000, 75+(65*1))

rightiBtn = pygame.Rect(1015+75,50+(65*1),150,50)
ribText = font.render("R'", True, white) 
ribTextRect = ribText.get_rect()
ribTextRect.center = (1165, 75+(65*1)) 

upBtn = pygame.Rect(850+75,50+(65*2),150,50)
ubText = font.render('U', True, white) 
ubTextRect = ubText.get_rect()
ubTextRect.center = (1000, 75+(65*2))

upiBtn = pygame.Rect(1015+75,50+(65*2),150,50)
uibText = font.render("U'", True, white) 
uibTextRect = uibText.get_rect()
uibTextRect.center = (1165, 75+(65*2)) 

downBtn = pygame.Rect(850+75,50+(65*3),150,50)
dbText = font.render('D', True, white) 
dbTextRect = dbText.get_rect()
dbTextRect.center = (1000, 75+(65*3))

downiBtn = pygame.Rect(1015+75,50+(65*3),150,50)
dibText = font.render("D'", True, white) 
dibTextRect = dibText.get_rect()
dibTextRect.center = (1165, 75+(65*3)) 

frontBtn = pygame.Rect(850+75,50+(65*4),150,50)
fbText = font.render('F', True, white) 
fbTextRect = fbText.get_rect()
fbTextRect.center = (1000, 75+(65*4))

frontiBtn = pygame.Rect(1015+75,50+(65*4),150,50)
fibText = font.render("F'", True, white) 
fibTextRect = fibText.get_rect()
fibTextRect.center = (1165, 75+(65*4)) 

backBtn = pygame.Rect(850+75,50+(65*5),150,50)
bbText = font.render('B', True, white) 
bbTextRect = bbText.get_rect()
bbTextRect.center = (1000, 75+(65*5))

backiBtn = pygame.Rect(1015+75,50+(65*5),150,50)
bibText = font.render("B'", True, white) 
bibTextRect = bibText.get_rect()
bibTextRect.center = (1165, 75+(65*5)) 

randomizeBtn = pygame.Rect(850+75,50+(65*6),315,50)
randomizeText = font.render("Randomize", True, white) 
randomizeTextRect = randomizeText.get_rect()
randomizeTextRect.center = (1000+(82.5),75+(65*6))

resetBtn = pygame.Rect(850+75,50+(65*7),315,50)
resetText = font.render("Reset", True, white) 
resetTextRect = resetText.get_rect()
resetTextRect.center = (1000+(82.5),75+(65*7))

#set up clock
clock = pygame.time.Clock()
time_elapsed_since_last_action = 0
time_elapsed = 0
# the standard speed for randomization and resetting is 250ms per turn. On large resets the
# move interval will be lowered during the reset
defaultMoveInterval = 200
moveInterval = defaultMoveInterval
totalMoveList = []
animating = False # set to true to animate the above movelist 1 second after program start
resetting = False # this is true when the cube is being reset to a solved state
listIndex = 0
# Run until the user asks to quit
running = True
while running:
    # Fill the background with grey
    screen.fill((128, 128, 128))

    # Draw cube
    draw_rCube(cube,75,155,3)

    #   Drawing our buttons
    pygame.draw.rect(screen,[50,50,50],leftBtn)
    pygame.draw.rect(screen,[50,50,50],leftiBtn)
    pygame.draw.rect(screen,[50,50,50],rightBtn)
    pygame.draw.rect(screen,[50,50,50],rightiBtn)
    pygame.draw.rect(screen,[50,50,50],upBtn)
    pygame.draw.rect(screen,[50,50,50],upiBtn)
    pygame.draw.rect(screen,[50,50,50],downBtn)
    pygame.draw.rect(screen,[50,50,50],downiBtn)
    pygame.draw.rect(screen,[50,50,50],frontBtn)
    pygame.draw.rect(screen,[50,50,50],frontiBtn)
    pygame.draw.rect(screen,[50,50,50],backBtn)
    pygame.draw.rect(screen,[50,50,50],backiBtn)
    
    pygame.draw.rect(screen,[50,50,50],randomizeBtn)
    pygame.draw.rect(screen,[50,50,50],resetBtn)


    screen.blit(lbText, lbTextRect) 
    screen.blit(libText, libTextRect) 
    screen.blit(rbText, rbTextRect) 
    screen.blit(ribText, ribTextRect) 
    screen.blit(ubText, ubTextRect) 
    screen.blit(uibText, uibTextRect) 
    screen.blit(dbText, dbTextRect) 
    screen.blit(dibText, dibTextRect)
    screen.blit(fbText, fbTextRect) 
    screen.blit(fibText, fibTextRect) 
    screen.blit(bbText, bbTextRect) 
    screen.blit(bibText, bibTextRect)
    
    screen.blit(randomizeText,randomizeTextRect)
    screen.blit(resetText,resetTextRect)

    #   Button Event Checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.pos 

            # each button has an 'if'
            if leftBtn.collidepoint(mousePos):
                cube.turn('L')
                backPath.append(R.Cubes.reverseMove("L"))
                system('cls')
                cube.print()
            if leftiBtn.collidepoint(mousePos):
                cube.turn("Li")
                backPath.append(R.Cubes.reverseMove("Li"))
                system('cls')
                cube.print()
            if rightBtn.collidepoint(mousePos):
                cube.turn('R')
                backPath.append(R.Cubes.reverseMove("R"))
                system('cls')
                cube.print()
            if rightiBtn.collidepoint(mousePos):
                cube.turn("Ri")
                backPath.append(R.Cubes.reverseMove("Ri"))
                system('cls')
                cube.print()
            if upBtn.collidepoint(mousePos):
                cube.turn('U')
                backPath.append(R.Cubes.reverseMove("U"))
                system('cls')
                cube.print()
            if upiBtn.collidepoint(mousePos):
                cube.turn("Ui")
                backPath.append(R.Cubes.reverseMove("Ui"))
                system('cls')
                cube.print()
            if downBtn.collidepoint(mousePos):
                cube.turn('D')
                backPath.append(R.Cubes.reverseMove("D"))
                system('cls')
                cube.print()
            if downiBtn.collidepoint(mousePos):
                cube.turn("Di")
                system('cls')
                backPath.append(R.Cubes.reverseMove("Di"))
                cube.print()
            if frontBtn.collidepoint(mousePos):
                cube.turn('F')
                system('cls')
                backPath.append(R.Cubes.reverseMove("F"))
                cube.print()
            if frontiBtn.collidepoint(mousePos):
                cube.turn("Fi")                
                backPath.append(R.Cubes.reverseMove("Fi"))
                system('cls')
                cube.print()
            if backBtn.collidepoint(mousePos):
                cube.turn('B')
                backPath.append(R.Cubes.reverseMove("B"))
                system('cls')
                cube.print()
            if backiBtn.collidepoint(mousePos):
                cube.turn("Bi")
                backPath.append(R.Cubes.reverseMove("Bi"))
                system('cls')
                cube.print()
            if resetBtn.collidepoint(mousePos):
                print('resetbutton - ' + str(animating))
                if not animating:
                    totalMoveList = backPath.copy()
                    totalMoveList = totalMoveList[::-1]
                    listIndex = 0
                    backPath = []
                    resetting = True
                    animating = True
                    if len(totalMoveList) > 10:
                        moveInterval = (2500/len(totalMoveList)) # set the move interval so that the entire animation takes 5 seconds
            if randomizeBtn.collidepoint(mousePos):
                print('randobutton')
                if not animating:
                    totalMoveList = R.Cubes.generateRandomMoveList(20)
                    listIndex = 0
                    animating = True


            



    #   This section handles animation of move sequences, it can be used by making sure your cube is 
    #   at the correct starting position, putting your move list into "totalMoveList", setting listIndex to 0,
    #   and setting "animating" to true. When the sequence has finished, "animating" will be set to false
    dt = clock.tick()
    time_elapsed_since_last_action += dt
    time_elapsed += dt
    if time_elapsed_since_last_action > moveInterval and not listIndex>len(totalMoveList)-1 and time_elapsed > 1000 and animating:
        cube.turn(totalMoveList[listIndex]) #make the turn of the cycle
        if not resetting:
            backPath.append(R.Cubes.reverseMove(totalMoveList[listIndex]))
        # Clear screen and print text display of cube
        system('cls')
        cube.print()
        
        #   Increment index, check if last cycle of the list and set animating to false if so.
        listIndex += 1
        if(listIndex) == len(totalMoveList):
            animating = False
            resetting = False
            moveInterval = defaultMoveInterval
        #   Reset time since last action
        print(str(backPath) + ' | ' + str(animating) + ' | ' + str(len(totalMoveList)) + ' | ' + str((listIndex)))
        time_elapsed_since_last_action = 0


    # Flip the display
    pygame.display.flip()

#No longer running, 
pygame.quit()


