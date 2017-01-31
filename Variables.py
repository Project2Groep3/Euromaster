import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

GREEN = (34, 177, 76)
LIGHT_GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
LIGHT_BLUE = ()
RED = (200, 0, 0)
LIGHT_RED = (255, 0, 0)
YELLOW = (200, 200, 0)
LIGHT_YELLOW = (255, 255, 0)

TURQUOISE = (174, 243, 227)
CORAL = (255, 127, 80)
LIGHT_CORAL = (250, 127, 80)

# Frames per second
FPS = 30
FPSCLOCK = pygame.time.Clock()

AmountOfPlayers = 0
paused = False
fem1 = True
fem2 = True
male1 = True
male2 = True
sport = True
geog = True
entert = True
hist = True

# Resolution
WINDOWWIDTH = 1024
WINDOWHEIGHT = 768

# Declaring displaysurf
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

# scales of the screen
X_1_2 = int(WINDOWWIDTH / 2)
X_1_3 = int(WINDOWWIDTH / 3)
X_1_4 = int(WINDOWWIDTH / 4)
X_1_5 = int(WINDOWWIDTH / 5)
X_2_3 = int(WINDOWWIDTH / 3 * 2)
X_2_4 = int(WINDOWWIDTH / 4 * 2)
X_2_5 = int(WINDOWWIDTH / 5 * 2)
X_3_4 = int(WINDOWWIDTH / 4 * 3)
X_3_5 = int(WINDOWWIDTH / 5 * 3)
X_4_4 = int(WINDOWWIDTH / 4 * 4)
X_4_5 = int(WINDOWWIDTH / 5 * 4)

Y_1_2 = int(WINDOWHEIGHT / 2)
Y_1_3 = int(WINDOWHEIGHT / 3)
Y_1_4 = int(WINDOWHEIGHT / 4)
Y_2_3 = int(WINDOWHEIGHT / 3 * 2)
Y_3_4 = int(WINDOWHEIGHT / 4 * 3)

backGroundImage = pygame.image.load('images/MainMenu.png')
gameBackground = pygame.image.load("images/gamebg1.png")

playerIcon_male1 = pygame.image.load("images/icon_male1.png")
playerIcon_male2 = pygame.image.load("images/icon_male2.png")
playerIcon_female1 = pygame.image.load("images/icon_female1.png")
playerIcon_female2 = pygame.image.load("images/icon_female2.png")

player1IconSmall = pygame.image.load("images/playericon1Small.png")
player2IconSmall = pygame.image.load("images/playericon2Small.png")
player3IconSmall = pygame.image.load("images/playericon3Small.png")
player4IconSmall = pygame.image.load("images/playericon4Small.png")


diceImage1 = pygame.image.load('images/dice1.jpg')
diceImage2 = pygame.image.load('images/dice2.jpg')
diceImage3 = pygame.image.load('images/dice3.jpg')
diceImage4 = pygame.image.load('images/dice4.jpg')
diceImage5 = pygame.image.load('images/dice5.jpg')
diceImage6 = pygame.image.load('images/dice6.jpg')

instructionsImage = pygame.image.load('images/Instructions.jpg')
instructionsImageNED1 = pygame.image.load('images/NEDERLANDS-instructionsimg1.png')
instructionsImageNED2 = pygame.image.load('images/NEDERLANDS-instructionsimg2.png')
instructionsImageNED3 = pygame.image.load('images/NEDERLANDS-instructionsimg3.png')
instructionsImageEN1 = pygame.image.load('images/ENGELS-instructionsimg1.png')
instructionsImageEN2 = pygame.image.load('images/ENGELS-instructionsimg2.png')
instructionsImageEN3 = pygame.image.load('images/ENGELS-instructionsimg3.png')

winnerscreen = pygame.image.load('images/winnaarscherm.png')

correctAnswer = False