import pygame, sys, time, random, psycopg2
from Variables import *
from pygame.locals import *

pygame.init()

Euromaster-Aya
FPS = 30
FPSCLOCK = pygame.time.Clock()

AmountOfPlayers = 0

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

X_1_2 = int(WINDOWWIDTH / 2)
X_1_3 = int(WINDOWWIDTH / 3)

Y_1_2 = int(WINDOWHEIGHT / 2)
Y_1_3 = int(WINDOWHEIGHT / 3)
Y_1_4 = int(WINDOWHEIGHT / 4)

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
TURQUOISE = (174, 243, 227)
CORAL = (255, 127, 80)
LIGHT_CORAL = (250, 127, 80)


# Images
backGroundImage = pygame.image.load('MainMenu.png')
gameBackground = pygame.image.load("gamebg1.png")

playerIcon1 = pygame.image.load("playericon1.png")
playerIcon2 = pygame.image.load("playericon2.png")
playerIcon3 = pygame.image.load("playericon3.png")
playerIcon4 = pygame.image.load("playericon4.png")


diceImage1 = pygame.image.load('dice1.jpg')
diceImage2 = pygame.image.load('dice2.jpg')
diceImage3 = pygame.image.load('dice3.jpg')
diceImage4 = pygame.image.load('dice4.jpg')
diceImage5 = pygame.image.load('dice5.jpg')
diceImage6 = pygame.image.load('dice6.jpg')

instructionsImage = pygame.image.load('Instructions.png')
instructionsImageNED1 = pygame.image.load('NEDERLANDS-instructionsimg1.png')
instructionsImageNED2 = pygame.image.load('NEDERLANDS-instructionsimg2.png')
instructionsImageNED3 = pygame.image.load('NEDERLANDS-instructionsimg3.png')
instructionsImageEN1 = pygame.image.load('ENGELS-instructionsimg1.png')
instructionsImageEN2 = pygame.image.load('ENGELS-instructionsimg2.png')
instructionsImageEN3 = pygame.image.load('ENGELS-instructionsimg3.png')


fontObjLarge = pygame.font.Font('freesansbold.ttf', 32)
fontObjMedium = pygame.font.Font('freesansbold.ttf', 24)
fontObjSmall = pygame.font.Font('freesansbold.ttf', 18)


# Vector class and position
class Vector2:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


# Player class
class Player:
    def __init__(self, playerID=0, name="", icon=None, category="", posX=0, posY=0, correctanswers=0, iconX=0, iconY=0):
        self.PlayerID = playerID
        self.PlayerName = name
        self.PlayerIcon = icon
        self.Category = category
        self.Position = Vector2(posX, posY)
        self.CorrectAnswers = correctanswers
        self.IconPosition = Vector2(iconX, iconY)

    def move_right(self):
        # self.Position.X += Tools1.steps()
        self.Position.X += 1
        self.icon_match()

    def move_left(self):
        # self.Position.X -= Tools1.steps()
        self.Position.X -= 1
        self.icon_match()

    def move_up(self):
        # self.Position.Y -= Tools1.steps()
        self.Position.Y += 1
        self.icon_match()

    def move_down(self):
        # self.Position.Y += Tools1.steps()
        self.Position.Y -= 1
        self.icon_match()

    def get_rekt(self, down):
        self.Position.Y -= down
        self.icon_match()

    def update_icon(self):
        if self.Category == "Sport":
            self.Position.X = 1
        elif self.Category == "Geografie":
            self.Position.X = 3
        elif self.Category == "Entertainment":
            self.Position.X = 5
        elif self.Category == "Geschiedenis":
            self.Position.X = 7

        if self.PlayerIcon == "a":
            self.PlayerIcon = playerIcon_male1
        elif self.PlayerIcon == "b":
            self.PlayerIcon = playerIcon_male2
        elif self.PlayerIcon == "c":
            self.PlayerIcon = playerIcon_female1
        elif self.PlayerIcon == "d":
            self.PlayerIcon = playerIcon_female2

    def icon_match(self):
        for key in tile_list:
            if self.Position.X == tile_list[key].Position.X and self.Position.Y == tile_list[key].Position.Y:
                self.IconPosition.X = tile_list[key].DrawPos.X
                self.IconPosition.Y = tile_list[key].DrawPos.Y

    def draw_icon(self):
        DISPLAYSURF.blit(self.PlayerIcon, (self.IconPosition.X, self.IconPosition.Y))


# Making objects of playerclass
player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()

# List of playerobjects
PlayerList = [player1, player2, player3, player4]


# Tile class
class Tile:
    def __init__(self, category, posX, posY, drawX, drawY):
        self.Category = category
        self.Position = Vector2(posX, posY)
        self.DrawPos = Vector2(drawX, drawY)

    def draw_tile(self):
        if self.Category == "Sport":
            pygame.draw.circle(DISPLAYSURF, BLUE, (self.DrawPos.X, self.DrawPos.Y), 10, 0)
        elif self.Category == "Geografie":
            pygame.draw.circle(DISPLAYSURF, LIGHT_GREEN, (self.DrawPos.X, self.DrawPos.Y), 10, 0)
        elif self.Category == "Entertainment":
            pygame.draw.circle(DISPLAYSURF, RED, (self.DrawPos.X, self.DrawPos.Y), 10, 0)
        elif self.Category == "Geschiedenis":
            pygame.draw.circle(DISPLAYSURF, YELLOW, (self.DrawPos.X, self.DrawPos.Y), 10, 0)
        elif self.Category == "Win":
            pygame.draw.circle(DISPLAYSURF, BLACK, (self.DrawPos.X, self.DrawPos.Y), 13, 0)
        elif self.Category == "Bottom":
            pygame.draw.circle(DISPLAYSURF, BLACK, (self.DrawPos.X, self.DrawPos.Y), 10, 0)

    def get_attributes(self):
        return self.Category, self.Position.X, self.Position.Y, self.DrawPos.X, self.DrawPos.Y


def text_to_button(msg, color, buttonX, buttonY, buttonWidth, buttonHeight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonX + (buttonWidth / 2)), buttonY + (buttonHeight / 2))
    DISPLAYSURF.blit(textSurf, textRect)


def text_objects(text, color, size="small"):
    global textSurface
    if size == "small":
        textSurface = fontObjSmall.render(text, True, color)
    elif size == "medium":
        textSurface = fontObjMedium.render(text, True, color)
    elif size == "large":
        textSurface = fontObjLarge.render(text, True, color)

    return textSurface, textSurface.get_rect()


# def player_names():



# def who_starts():



# Function that generates tiles on the map
def generate_tiles():
    n = 640
    i = 60
    global tile_list
    tile_list = {}
    for x in range(0, 10):
        tile_list["tile_{}_{}_{}".format('blauw', x, 'a')] = Tile("Sport", 1, x, X_1_3, n)
        tile_list["tile_{}_{}_{}".format('blauw', x, 'b')] = Tile("Sport", 2, x, X_1_3 + i, n)
        tile_list["tile_{}_{}_{}".format('groen', x, 'a')] = Tile("Geografie", 3, x, X_1_3 + (2 * i), n)
        tile_list["tile_{}_{}_{}".format('groen', x, 'b')] = Tile("Geografie", 4, x, X_1_3 + (3 * i), n)
        tile_list["tile_{}_{}_{}".format('rood', x, 'a')] = Tile("Entertainment", 5, x, X_1_3 + (4 * i), n)
        tile_list["tile_{}_{}_{}".format('rood', x, 'b')] = Tile("Entertainment", 6, x, X_1_3 + (5 * i), n)
        tile_list["tile_{}_{}_{}".format('geel', x, 'a')] = Tile("Geschiedenis", 7, x, X_1_3 + (6 * i), n)
        tile_list["tile_{}_{}_{}".format('geel', x, 'b')] = Tile("Geschiedenis", 8, x, X_1_3 + (7 * i), n)
        n -= 40

    i = 30

    for y in range(11, 16):
        tile_list["tile_{}_{}_{}".format('blauw', y, 'a')] = Tile("Sport", 1, y, X_1_3 + i, n)
        tile_list["tile_{}_{}_{}".format('groen', y, 'a')] = Tile("Geografie", 2, y, X_1_3 + (i * 5), n)
        tile_list["tile_{}_{}_{}".format('rood', y, 'a')] = Tile("Entertainment", 3, y, X_1_3 + (i * 9), n)
        tile_list["tile_{}_{}_{}".format('geel', y, 'a')] = Tile("Geschiedenis", 4, y, X_1_3 + (i * 13), n)
        n -= 40

    tile_list.update(
        {'top_tile': Tile("Win", 1, 16, X_1_2 + 40, 30), 'bottom_tile': Tile("Bottom", 0, 0, X_1_2 + 40, 660)})

    # for key in tile_list:
    #     tile_list[key].draw_tile()


# Class tools with dices etc
class Tools():
    def __init__(self):
        self.Value = 0
        self.DiceImage = ""
        self.DiceResult = self.dice()

    def dice(self):
        return random.randint(1, 6)

    def steps(self):
        DiceResult = self.dice()
        if DiceResult == 1 or DiceResult == 2:
            return 1
        elif DiceResult == 3 or DiceResult == 4:
            return 2
        elif DiceResult == 5 or DiceResult == 5:
            return 3

    def timer(self):
        for i in range(50, 0, -1):
            time.sleep(1)

    def show_dice_image(self):
        if self.DiceResult == 1:
            self.DiceImage = diceImage1
        elif self.DiceResult == 2:
            self.DiceImage = diceImage2
        elif self.DiceResult == 3:
            self.DiceImage = diceImage3
        elif self.DiceResult == 4:
            self.DiceImage = diceImage4
        elif self.DiceResult == 5:
            self.DiceImage = diceImage5
        elif self.DiceResult == 6:
            self.DiceImage = diceImage6

        return self.DiceImage


# Object of tools class
Tools1 = Tools()


# Function that shows the screen how many players u want to play with
def how_many_icons(AmountOfPlayers):
    global ActivePlayers
    ActivePlayers = []
    for i in range(AmountOfPlayers):
        ActivePlayers.append(PlayerList[i])

    j = 0
    for players in range(len(ActivePlayers)):
        j += 1
        PlayerList[players].PlayerID = j
        PlayerList[players].PlayerName = input("Player" + str(j) + " Please type in your name: ")
        # PlayerList[players].Category = input("Choose a Category: ")
        PlayerList[players].PlayerIcon = input("Choose an Icon!")

    for k in range(len(ActivePlayers)):
        PlayerList[k].update_icon()
        print(PlayerList[k].PlayerID, PlayerList[k].PlayerName, PlayerList[k].PlayerIcon)


# Function that shows when it's a player turn
def show_turn(currentPlayer):
    showed = True
    abc = PlayerList[currentPlayer].PlayerName

    while showed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # print(event.unicode)
                if event.key == pygame.K_ESCAPE:
                    showed = False

        textYourTurn = fontObjLarge.render("Hey {} it's your turn!".format(abc), True, BLACK, None)
        textYourTurnRect = textYourTurn.get_rect()
        textYourTurnRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 5)

        DISPLAYSURF.blit(textYourTurn, textYourTurnRect)

        pygame.display.update()
        time.sleep(1)
        showed = False
        FPSCLOCK.tick(FPS / 2)


# Function that displays dice result on the screen
def show_dice():
    diced = True

    while diced:
        textDiceResult = fontObjLarge.render('The result of your dice is:', True, BLACK, WHITE)
        textDiceResultRect = textDiceResult.get_rect()
        textDiceResultRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 4)

        DISPLAYSURF.blit(textDiceResult, textDiceResultRect)

        DISPLAYSURF.blit(Tools1.show_dice_image(), (WINDOWWIDTH / 2, WINDOWHEIGHT / 2))

        pygame.display.update()

        time.sleep(1)
        diced = False
        FPSCLOCK.tick(FPS / 2)


def show_buttons():  # function that shows button screen test
    buttoned = True

    while buttoned:

        DISPLAYSURF.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        cur = pygame.mouse.get_pos()

        if 140 + 120 > cur[0] > 140 and 500 + 50 > cur[1] > 500:
            pygame.draw.rect(DISPLAYSURF, LIGHT_GREEN, (140, 500, 120, 50))
        else:
            pygame.draw.rect(DISPLAYSURF, GREEN, (140, 500, 120, 50))

        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def show_main_menu():  # Function that shows Main menu

    pygame.init()
    menud = True

    pygame.display.set_caption('Euromaster')

    while menud:

        DISPLAYSURF.fill(WHITE)

        textWelcome = fontObjLarge.render('Welcome to Euromaster!', True, BLACK, None)
        textWelcomeRect = textWelcome.get_rect()
        textWelcomeRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 4)

        menuKnopStart = fontObjSmall.render('Press S to Start Game', True, BLACK, None)
        menuKnopStartRect = menuKnopStart.get_rect()
        menuKnopStartRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 1.80)

        menuKnopLoadGame = fontObjSmall.render('Press L to Load Game', True, BLACK, None)
        menuKnopLoadGameRect = menuKnopLoadGame.get_rect()
        menuKnopLoadGameRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 1.65)

        menuKnopInstructions = fontObjSmall.render('Press I for Instructions', True, BLACK, None)
        menuKnopInstructionsRect = menuKnopInstructions.get_rect()
        menuKnopInstructionsRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 1.53)

        menuKnopHighscores = fontObjSmall.render('Press H for Highscores', True, BLACK, None)
        menuKnopHighscoresRect = menuKnopHighscores.get_rect()
        menuKnopHighscoresRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 1.42)

        menuKnopExitGame = fontObjSmall.render('Press E to Exit Game', True, BLACK, None)
        menuKnopExitGameRect = menuKnopExitGame.get_rect()
        menuKnopExitGameRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 1.33)

        DISPLAYSURF.blit(backGroundImage, (0, 0))
        DISPLAYSURF.blit(textWelcome, textWelcomeRect)
        DISPLAYSURF.blit(menuKnopStart, menuKnopStartRect)
        DISPLAYSURF.blit(menuKnopLoadGame, menuKnopLoadGameRect)
        DISPLAYSURF.blit(menuKnopInstructions, menuKnopInstructionsRect)
        DISPLAYSURF.blit(menuKnopHighscores, menuKnopHighscoresRect)
        DISPLAYSURF.blit(menuKnopExitGame, menuKnopExitGameRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_i:
                    show_instructions_menu()

                elif event.key == pygame.K_s:
                    menud = False

                elif event.key == pygame.K_l:
                    show_buttons()

                elif event.key == pygame.K_h:
                    show_highscore_menu()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# Function that shows the instruction menu
def show_instructions_menu():
    instructions = True

    while instructions:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instructions = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(instructionsImage, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


# Function that shows the highscore menu
def show_highscore_menu():
    highscored = True

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(backGroundImage, (0, 0))

    textHighscore = fontObjLarge.render('Highscores', True, BLACK, None)
    textHighscoreRect = textHighscore.get_rect()
    textHighscoreRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 4)

    DISPLAYSURF.blit(textHighscore, textHighscoreRect)

    while highscored:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # print(event.unicode)
                if event.key == pygame.K_ESCAPE:
                    highscored = False

        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


# Function that shows menu where u can pick the amount of players
def show_players_menu():
    chooseplayers = True

    global AmountOfPlayers

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(backGroundImage, (0, 0))

    textChoosePlayers = fontObjLarge.render('Choose the number of players', True, BLACK, None)
    textChoosePlayersRect = textChoosePlayers.get_rect()
    textChoosePlayersRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 4)

    textChoosePlayers1 = fontObjMedium.render('Press 1 for 1 player', True, BLACK, None)
    textChoosePlayersRect1 = textChoosePlayers1.get_rect()
    textChoosePlayersRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 1.9)

    textChoosePlayers2 = fontObjMedium.render('Press 2 for 2 players', True, BLACK, None)
    textChoosePlayersRect2 = textChoosePlayers2.get_rect()
    textChoosePlayersRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 1.75)

    textChoosePlayers3 = fontObjMedium.render('Press 3 for 3 players', True, BLACK, None)
    textChoosePlayersRect3 = textChoosePlayers3.get_rect()
    textChoosePlayersRect3.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 1.6)

    textChoosePlayers4 = fontObjMedium.render('Press 4 for 4 players', True, BLACK, None)
    textChoosePlayersRect4 = textChoosePlayers4.get_rect()
    textChoosePlayersRect4.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 1.45)

    DISPLAYSURF.blit(textChoosePlayers, textChoosePlayersRect)
    DISPLAYSURF.blit(textChoosePlayers1, textChoosePlayersRect1)
    DISPLAYSURF.blit(textChoosePlayers2, textChoosePlayersRect2)
    DISPLAYSURF.blit(textChoosePlayers3, textChoosePlayersRect3)
    DISPLAYSURF.blit(textChoosePlayers4, textChoosePlayersRect4)

    while chooseplayers:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    AmountOfPlayers = 1
                    chooseplayers = False

                elif event.key == pygame.K_2:
                    AmountOfPlayers = 2
                    chooseplayers = False

                elif event.key == pygame.K_3:
                    AmountOfPlayers = 3
                    chooseplayers = False

                elif event.key == pygame.K_4:
                    AmountOfPlayers = 4
                    chooseplayers = False

        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


# Function that shows menu where players pick their icon
def show_icon_menu():
    global iconed
    iconed = True

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(backGroundImage, (0, 0))

    textPlayerIcon = fontObjLarge.render('Choose your icon!', True, BLACK, None)
    textPlayerIconRect = textPlayerIcon.get_rect()
    textPlayerIconRect.center = (WINDOWWIDTH / 2, (WINDOWHEIGHT / 4 - 100))

    DISPLAYSURF.blit(textPlayerIcon, textPlayerIconRect)

    DISPLAYSURF.blit(playerIcon_female1, (X_1_5 - 100, Y_1_2 - 100))
    DISPLAYSURF.blit(playerIcon_female2, (X_2_5 - 100, Y_1_2 - 100))
    DISPLAYSURF.blit(playerIcon_male1, (X_3_5 - 100, Y_1_2 - 100))
    DISPLAYSURF.blit(playerIcon_male2, (X_4_5 - 100, Y_1_2 - 100))

    pygame.display.update()

    how_many_icons(AmountOfPlayers)
    show_gameplay()

    while iconed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


# Function for the main game loop
def show_gameplay():
    gameplayed = True

    currentPlayer = 0

    while gameplayed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # print(event.unicode)
                # if event.key == pygame.K_ESCAPE:
                #     gameplayed = False
                if event.key == pygame.K_UP:
                    PlayerList[currentPlayer].move_up()

                elif event.key == pygame.K_DOWN:
                    PlayerList[currentPlayer].move_down()

                elif event.key == pygame.K_RIGHT:
                    PlayerList[currentPlayer].move_right()

                elif event.key == pygame.K_LEFT:
                    PlayerList[currentPlayer].move_left()

                elif event.key == pygame.K_p:
                    show_pause()


def show_instructions_menu():
    instructions = True

    while instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

                elif event.key == pygame.K_r:
                    show_dice()
                elif event.key == pygame.K_d:
                    if currentPlayer < len(ActivePlayers) - 1:
                        currentPlayer += 1
                        show_turn(currentPlayer)
                        print(currentPlayer)
                    else:
                        currentPlayer = 0
                        show_turn(currentPlayer)
                        print(currentPlayer)

        generate_tiles()
        # DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(gameBackground, (0, 0))

        for key in tile_list:
            tile_list[key].draw_tile()


        for k in range(len(ActivePlayers)):
            PlayerList[k].draw_icon()


            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if instructionsImage.get_rect().collidepoint(x, y):
                    instructions = False
                    show_instructions_menu1()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(instructionsImage, (0, 0))

        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def show_instructions_menu1():
    instructions1 = True


    while instructions1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instructions = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if instructionsImageNED1.get_rect().collidepoint(x, y):
                    instructions1 = False
                    show_instructions_menu2()


        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(instructionsImageNED1, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def show_instructions_menu2():
    instructions2 = True


    while instructions2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instructions = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if instructionsImageNED2.get_rect().collidepoint(x, y):
                    instructions2 = False
                    show_instructions_menu3()


        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(instructionsImageNED2, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)

def show_instructions_menu3():
    instructions3 = True


    while instructions3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instructions = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if instructionsImageNED3.get_rect().collidepoint(x, y):
                    instructions3 = False
                    show_instructions_menu()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(instructionsImageNED3, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)



def show_main_menu():
    pygame.init()
    menud = True

    pygame.display.set_caption('Euromaster')

    while menud:

# Function that shows the pause menu
def show_pause():
    paused = True


    while paused:
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(backGroundImage, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                elif event.key == pygame.K_e:
                    pygame.quit()
                    quit()

        textPauseMenu = fontObjLarge.render('Welcome to the Pause Menu.', True, BLACK, None)
        textPauseMenuRect = textPauseMenu.get_rect()
        textPauseMenuRect.center = (X_1_2, WINDOWHEIGHT / 4)

        # old code, made to function
        # cur = pygame.mouse.get_pos()
        #
        # if X_1_2 + 150 > cur[0] > X_1_2 and Y_1_2-50 + 50 > cur[1] > Y_1_2-50:
        #     pygame.draw.rect(DISPLAYSURF, LIGHT_GREEN, (X_1_2-50, Y_1_2-50, 150, 50))
        # else:
        #     pygame.draw.rect(DISPLAYSURF, GREEN, (X_1_2-50, Y_1_2-50, 150, 50))
        #
        # if X_1_2 + 150 > cur[0] > X_1_2 and Y_1_2+50 + 50 > cur[1] > Y_1_2+50:
        #     pygame.draw.rect(DISPLAYSURF, LIGHT_GREEN, (X_1_2-50, Y_1_2+50, 150, 50))
        # else:
        #     pygame.draw.rect(DISPLAYSURF, GREEN, (X_1_2-50, Y_1_2+50, 150, 50))
        #
        # if X_1_2 + 150 > cur[0] > X_1_2 and Y_1_2+150 + 50 > cur[1] > Y_1_2+150:
        #     pygame.draw.rect(DISPLAYSURF, LIGHT_GREEN, (X_1_2-50, Y_1_2+150, 150, 50))
        # else:
        #     pygame.draw.rect(DISPLAYSURF, GREEN, (X_1_2-50, Y_1_2+150, 150, 50))


        DISPLAYSURF.blit(textPauseMenu, textPauseMenuRect)
        button("Resume Game", X_1_2 - 50, Y_1_2 - 50, 150, 50, GREEN, LIGHT_GREEN)

        DISPLAYSURF.blit(textPauseMenu, textPauseMenuRect)
        button("Main Menu", X_1_2 - 50, Y_1_2 + 50, 150, 50, YELLOW, LIGHT_YELLOW)

        DISPLAYSURF.blit(textPauseMenu, textPauseMenuRect)
        button("Exit Game", X_1_2 - 50, Y_1_2 + 150, 150, 50, RED, LIGHT_RED)

        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


show_main_menu()
show_players_menu()
show_icon_menu()
