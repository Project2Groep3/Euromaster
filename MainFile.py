import sys, time, random
from Variables import *
# from Database import *
from pygame.locals import *

pygame.init()

fontObjLarge = pygame.font.Font('freesansbold.ttf', 32) #declaring fonts
fontObjMedium = pygame.font.Font('freesansbold.ttf', 24)
fontObjSmall = pygame.font.Font('freesansbold.ttf', 18)

class Vector2: # Vector Class
    def __init__(self, x, y):
        self.X = x
        self.Y = y

class Player: # Player Class
    def __init__(self, playerID=0, name="", icon=None, category="", posX=0, posY=0, correctanswers=0, iconX=X_1_2 + 40, iconY=660):
        self.PlayerID = playerID
        self.PlayerName = name
        self.PlayerIcon = icon
        self.Category = category
        self.Position = Vector2(posX, posY)
        self.CorrectAnswers = correctanswers
        self.IconPosition = Vector2(iconX, iconY)
        self.Direction = "UP"
        self.Score = 0

    def movement(self):
        if self.Direction == "UP":
            self.Position.Y -= Tools1.steps()
            self.icon_match()
        elif self.Direction == "DOWN":
            self.Position.Y += Tools1.steps()
            self.icon_match()
        elif self.Direction == "RIGHT":
            self.Position.X += Tools1.steps()
            self.icon_match()
        elif self.Direction == "LEFT":
            self.Position -= Tools1.steps()
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
            self.PlayerIcon = playerIcon_female1
        elif self.PlayerIcon == "b":
            self.PlayerIcon = playerIcon_female2
        elif self.PlayerIcon == "c":
            self.PlayerIcon = playerIcon_male1
        elif self.PlayerIcon == "d":
            self.PlayerIcon = playerIcon_male2

    def icon_match(self):
        for key in tile_list:
            if self.Position.X == tile_list[key].Position.X and self.Position.Y == tile_list[key].Position.Y:
                self.IconPosition.X = tile_list[key].DrawPos.X
                self.IconPosition.Y = tile_list[key].DrawPos.Y

    def draw_icon(self):
        DISPLAYSURF.blit(self.PlayerIcon, (self.IconPosition.X, self.IconPosition.Y))



player1 = Player() # Making objects of playerclass
player2 = Player()
player3 = Player()
player4 = Player()


PlayerList = [player1, player2, player3, player4] # List of playerobjects

class Tools(): #Tools class
    def __init__(self):
        self.Value = 0
        self.DiceImage = ""
        self.DiceResult = 0
        self.QuestionType = ""

    def dice(self):
        self.DiceResult = random.randint(1, 6)

    def steps(self):
        self.dice()
        if self.DiceResult == 1 or self.DiceResult == 2:
            return 1
        elif self.DiceResult == 3 or self.DiceResult == 4:
            return 2
        elif self.DiceResult == 5 or self.DiceResult == 5:
            return 3

    def question_type(self):
        if self.DiceResult == 1 or self.DiceResult == 3 or self.DiceResult == 5:
            self.QuestionType = "Open"
        elif self.DiceResult == 2 or self.DiceResult == 4 or self.DiceResult == 6:
            self.QuestionType = "MC"

    def timer(self):
        for i in range(50, 0, -1):
            time.sleep(1)

    def show_dice_image(self):
        self.steps()
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

Tools1 = Tools() # making tools object

class Tile: # tiles for the map
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


def generate_tiles(): # Function that generates tiles on the map
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



def how_many_icons(AmountOfPlayers): # amount of players screen
    global ActivePlayers
    ActivePlayers = []
    for i in range(AmountOfPlayers):
        ActivePlayers.append(PlayerList[i])

    j = 0
    for players in range(len(ActivePlayers)):
        j += 1
        PlayerList[players].PlayerID = j

    for k in range(len(ActivePlayers)):
        PlayerList[k].update_icon()


def show_turn(currentPlayer): # shows whose turn it is
    showed = True
    abc = PlayerList[currentPlayer].PlayerName
    while showed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    showed = False

        textYourTurn = fontObjLarge.render("Hey {} it's your turn!".format(abc), True, BLACK, LIGHT_CORAL)
        textYourTurnRect = textYourTurn.get_rect()
        textYourTurnRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 5)


        DISPLAYSURF.blit(textYourTurn, textYourTurnRect)

        pygame.display.update()
        time.sleep(1)
        showed = False
        FPSCLOCK.tick(FPS / 2)


def input_name(players): # takes input name
    currentPlayer = players + 1
    name = ""
    font = pygame.font.Font(None, 50)
    named = True
    while named:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    named = False
                    return name
            elif evt.type == QUIT:
                return

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(backGroundImage, (0, 0))
        textEnterName = fontObjLarge.render("Player{} please type in your name and press enter.".format(currentPlayer),
                                            True, BLACK, None)
        textEnterNameRect = textEnterName.get_rect()
        textEnterNameRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 5)

        block = font.render(name, True, BLACK)
        rect = block.get_rect()
        rect.center = DISPLAYSURF.get_rect().center
        DISPLAYSURF.blit(block, rect)
        DISPLAYSURF.blit(textEnterName, textEnterNameRect)
        pygame.display.update()


def enter_name(): #loops input_name() for all active players
    entered = True
    j = 0

    while entered:
        for players in range(AmountOfPlayers):
            PlayerList[players].PlayerName = input_name(players)

        entered = False

def choose_icon(): # loops show_icon_menu for all active players
    chosen = True

    while chosen:
        for players in range(AmountOfPlayers):
            PlayerList[players].PlayerIcon = show_icon_menu(players)

        chosen = False


def choose_category(currentPlayer):
    cat = True
    textButtonCategory = fontObjLarge.render("Choose your Category", True, BLACK, LIGHT_CORAL)
    textButton = fontObjLarge.render("  UP  ", True, BLACK, GREEN)
    textButtonDown = fontObjLarge.render("DOWN", True, BLACK, GREEN)
    textButtonRight = fontObjLarge.render("RIGHT", True, BLACK, GREEN)
    textButtonLeft = fontObjLarge.render("LEFT", True, BLACK, GREEN)


    while cat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cat = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if textButtonUp.get_rect(center=(X_1_2 - 50, Y_1_2 - 100)).collidepoint(x, y):
                    PlayerList[currentPlayer].Direction = "UP"
                    cat = False

                elif textButtonDown.get_rect(center=(X_1_2 - 50, Y_1_2)).collidepoint(x, y):
                    PlayerList[currentPlayer].Direction = "DOWN"
                    cat = False

                elif textButtonRight.get_rect(center=(X_1_2 + 25, Y_1_2 - 50)).collidepoint(x, y):
                    PlayerList[currentPlayer].Direction = "RIGHT"
                    directed = False

                elif textButtonLeft.get_rect(center=(X_1_2 - 125, Y_1_2 - 50)).collidepoint(x, y):
                    PlayerList[currentPlayer].Direction = "LEFT"
                    directed = False

#
# def who_starts():

def pick_direction(currentPlayer):
    directed = True

    textButtonUp = fontObjLarge.render("  UP  ", True, BLACK, GREEN)
    textButtonDown = fontObjLarge.render("DOWN", True, BLACK, GREEN)
    textButtonRight = fontObjLarge.render("RIGHT", True, BLACK, GREEN)
    textButtonLeft = fontObjLarge.render("LEFT", True, BLACK, GREEN)

    while directed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    directed = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if textButtonUp.get_rect(center=(X_1_2 - 50, Y_1_2 - 100)).collidepoint(x, y):
                    PlayerList[currentPlayer].Direction = "UP"
                    directed = False

                elif textButtonDown.get_rect(center=(X_1_2 - 50, Y_1_2)).collidepoint(x, y):
                    PlayerList[currentPlayer].Direction = "DOWN"
                    directed = False

                elif textButtonRight.get_rect(center=(X_1_2 + 25, Y_1_2 - 50)).collidepoint(x, y):
                    PlayerList[currentPlayer].Direction = "RIGHT"
                    directed = False

                elif textButtonLeft.get_rect(center=(X_1_2 - 125, Y_1_2 - 50)).collidepoint(x, y):
                    PlayerList[currentPlayer].Direction = "LEFT"
                    directed = False


        DISPLAYSURF.blit(textButtonUp, (X_1_2 - 50, Y_1_2 - 100))
        DISPLAYSURF.blit(textButtonDown, (X_1_2 - 50, Y_1_2))
        DISPLAYSURF.blit(textButtonRight, (X_1_2 + 25, Y_1_2 - 50))
        DISPLAYSURF.blit(textButtonLeft, (X_1_2 - 125, Y_1_2 - 50))



        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)

def show_dice(): # shows dice result on screen
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


def show_main_menu():  # shows main menu

    pygame.init()
    menud = True
    pygame.display.set_caption('Euromaster')

    while menud:

        DISPLAYSURF.fill(WHITE)

        textWelcome = fontObjLarge.render('Welcome to Euromaster!', True, BLACK, None)
        textWelcomeRect = textWelcome.get_rect()
        textWelcomeRect.center = (X_1_2, Y_1_4)

        menuKnopStart = fontObjMedium.render('Start Game', True, BLACK, LIGHT_CORAL)
        menuKnopLoadGame = fontObjMedium.render('Load Game', True, BLACK, LIGHT_CORAL)
        menuKnopInstructions = fontObjMedium.render('Instructions', True, BLACK,LIGHT_CORAL)
        menuKnopHighscores = fontObjMedium.render('Highscores', True, BLACK, LIGHT_CORAL)
        menuKnopExitGame = fontObjMedium.render('Exit Game', True, BLACK, LIGHT_CORAL)

        DISPLAYSURF.blit(backGroundImage, (0, 0))
        DISPLAYSURF.blit(textWelcome, textWelcomeRect)
        DISPLAYSURF.blit(menuKnopStart, (X_1_2-50, Y_1_2))
        DISPLAYSURF.blit(menuKnopLoadGame, (X_1_2-50, Y_1_2+50))
        DISPLAYSURF.blit(menuKnopInstructions, (X_1_2-50, Y_1_2 + 100))
        DISPLAYSURF.blit(menuKnopHighscores, (X_1_2-50, Y_1_2 + 150))
        DISPLAYSURF.blit(menuKnopExitGame, (X_1_2-50, Y_1_2 + 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if menuKnopStart.get_rect(center=(X_1_2-50, Y_1_2)).collidepoint(x, y):
                    menud = False
                    show_gameplay()
                elif menuKnopInstructions.get_rect(center=(X_1_2-50, Y_1_2 + 100)).collidepoint(x, y):
                    menud = False
                    show_instructions_menu()
                elif menuKnopHighscores.get_rect(center=(X_1_2-50, Y_1_2 + 150)).collidepoint(x, y):
                    menud = False
                    show_highscore_menu()
                elif menuKnopExitGame.get_rect(center=(X_1_2-50, Y_1_2 + 200)).collidepoint(x, y):
                    pygame.quit()
                    sys.exit()


        pygame.display.update()
        FPSCLOCK.tick(FPS)


def show_instructions_menu(): # instruction screen 1
    instructions = True

    while instructions:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instructions = False
                    show_main_menu()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if instructionsImage.get_rect().collidepoint(x, y):
                    instructions = False
                    show_instructions_menu1()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(instructionsImage, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def show_instructions_menu1(): # instructionscreen 2
    instructions1 = True

    while instructions1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instructions1 = False
                    show_main_menu()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if instructionsImageNED1.get_rect().collidepoint(x, y):
                    instructions1 = False
                    show_instructions_menu2()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(instructionsImageNED1, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def show_instructions_menu2(): #instructionscreen 3
    instructions2 = True

    while instructions2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instructions2 = False
                    show_main_menu()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if instructionsImageNED2.get_rect().collidepoint(x, y):
                    instructions2 = False
                    show_instructions_menu3()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(instructionsImageNED2, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def show_instructions_menu3(): # instruction screen 4
    instructions3 = True

    while instructions3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instructions3 = False
                    show_main_menu()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if instructionsImageNED3.get_rect().collidepoint(x, y):
                    instructions3 = False
                    show_instructions_menu()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(instructionsImageNED3, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def show_players_menu(): # choose amount of players u want to play with
    chooseplayers = True

    global AmountOfPlayers

    textChoosePlayers = fontObjLarge.render('How many players?', True, BLACK, CORAL)
    textChoosePlayers1 = fontObjMedium.render('1 Player', True, BLACK, LIGHT_CORAL)
    textChoosePlayers2 = fontObjMedium.render('2 Players', True, BLACK, LIGHT_CORAL)
    textChoosePlayers3 = fontObjMedium.render('3 Players', True, BLACK, LIGHT_CORAL)
    textChoosePlayers4 = fontObjMedium.render('4 Players', True, BLACK, LIGHT_CORAL)

    while chooseplayers:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if textChoosePlayers1.get_rect(center=(X_1_2-50, Y_1_2)).collidepoint(x, y):
                    AmountOfPlayers = 1
                    chooseplayers = False
                if textChoosePlayers2.get_rect(center=(X_1_2-50, Y_1_2+50)).collidepoint(x, y):
                    AmountOfPlayers = 2
                    chooseplayers = False
                if textChoosePlayers3.get_rect(center=(X_1_2-50, Y_1_2+100)).collidepoint(x, y):
                    AmountOfPlayers = 3
                    chooseplayers = False
                if textChoosePlayers4.get_rect(center=(X_1_2-50, Y_1_2+150)).collidepoint(x, y):
                    AmountOfPlayers = 4
                    chooseplayers = False


        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(backGroundImage, (0, 0))


        DISPLAYSURF.blit(textChoosePlayers, (X_1_2-100, Y_1_4))
        DISPLAYSURF.blit(textChoosePlayers1, (X_1_2-50, Y_1_2))
        DISPLAYSURF.blit(textChoosePlayers2, (X_1_2-50, Y_1_2 + 50))
        DISPLAYSURF.blit(textChoosePlayers3, (X_1_2-50, Y_1_2 + 100))
        DISPLAYSURF.blit(textChoosePlayers4, (X_1_2-50, Y_1_2 + 150))

        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def show_icon_menu(players): # shows screen where players pick their icons
    global iconed, fem1, fem2, male1, male2
    iconed = True


    playerName = PlayerList[players].PlayerName

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(backGroundImage, (0, 0))

    textPlayerIcon = fontObjLarge.render('Hey {} please click on your preferred character!'.format(playerName), True, BLACK, None)
    textPlayerIconRect = textPlayerIcon.get_rect()
    textPlayerIconRect.center = (WINDOWWIDTH / 2, (WINDOWHEIGHT / 4 - 100))

    DISPLAYSURF.blit(textPlayerIcon, textPlayerIconRect)
    if fem1 == True:
        DISPLAYSURF.blit(playerIcon_female1, (X_1_5 - 100, Y_1_2 - 100))
    if fem2 == True:
        DISPLAYSURF.blit(playerIcon_female2, (X_2_5 - 100, Y_1_2 - 100))
    if male1 == True:
        DISPLAYSURF.blit(playerIcon_male1, (X_3_5 - 100, Y_1_2 - 100))
    if male2 == True:
        DISPLAYSURF.blit(playerIcon_male2, (X_4_5 - 100, Y_1_2 - 100))

    pygame.display.update()

    while iconed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if playerIcon_female1.get_rect(center=(X_1_5 - 100, Y_1_2 - 100)).collidepoint(x, y):
                    playerIcon = "a"
                    fem1 = False
                    iconed = False

                if playerIcon_female2.get_rect(center=(X_2_5 - 100, Y_1_2 - 100)).collidepoint(x, y):
                    playerIcon = "b"
                    fem2 = False
                    iconed = False

                if playerIcon_male1.get_rect(center=(X_3_5 - 100, Y_1_2 - 100)).collidepoint(x, y):
                    playerIcon = "c"
                    male1 = False
                    iconed = False

                if playerIcon_male2.get_rect(center=(X_4_5 - 100, Y_1_2 - 100)).collidepoint(x, y):
                    playerIcon = "d"
                    male2 = False
                    iconed = False



        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)
    return playerIcon


def timer():
    frame_count = 0
    start_time = 50
    total_seconds = frame_count // FPS
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    output_string = ""

    text = fontObjLarge.render(output_string, True, BLACK)
    DISPLAYSURF.blit(text, [910, 10])

    total_seconds = start_time - (frame_count // FPS)
    if total_seconds < 0:
        total_seconds = 0

    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_string = "{0:02}:{1:02}".format(minutes, seconds)

    text = fontObjLarge.render(output_string, True, BLACK)
    DISPLAYSURF.blit(text, [960, 10])

    frame_count += 1
    
timer()
def show_gameplay(): # loop for gameplay
    global gameplayed
    gameplayed = True
    currentPlayer = 0

    show_players_menu()
    enter_name()
    choose_icon()
    how_many_icons(AmountOfPlayers)

    while gameplayed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    show_pause()

                elif event.key == pygame.K_r:
                    show_dice()
                elif event.key == pygame.K_d:
                    if currentPlayer < len(ActivePlayers) - 1:
                        currentPlayer += 1
                        show_turn(currentPlayer)
                        pick_direction(currentPlayer)

                    else:
                        currentPlayer = 0
                        show_turn(currentPlayer)
                        pick_direction(currentPlayer)

        generate_tiles()

        DISPLAYSURF.blit(gameBackground, (0, 0))

        abc = PlayerList[currentPlayer].PlayerName

        textWhoseTurn = fontObjLarge.render("It's:  {} turn!".format(abc), True, BLACK, None)
        textWhoseTurnRect = textWhoseTurn.get_rect()
        textWhoseTurnRect.center = (X_1_4 - 130, Y_1_4-100)


        DISPLAYSURF.blit(textWhoseTurn, textWhoseTurnRect)


        pygame.display.update()

        for key in tile_list:
            tile_list[key].draw_tile()

        for k in range(len(ActivePlayers)):
            PlayerList[k].draw_icon()

        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)




def show_highscore_menu(): # shows highscore screen
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
                if event.key == pygame.K_ESCAPE:
                    highscored = False

        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)

def show_pause(): # shows pause menu, is bugged atm
    global paused
    global gameplayed
    paused = True


    textPauseMenu = fontObjLarge.render('Welcome to the Pause Menu', True, BLACK, None)
    textPauseMenuRect = textPauseMenu.get_rect()
    textPauseMenuRect.center = (X_1_2, WINDOWHEIGHT / 4)

    textResumeGame = fontObjMedium.render('Resume Game', True, BLACK, LIGHT_CORAL)
    textMainMenu = fontObjMedium.render('Main Menu', True, BLACK, LIGHT_CORAL)
    textExitGame = fontObjMedium.render("Exit Game", True, BLACK, LIGHT_CORAL)

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if textResumeGame.get_rect(center=(X_1_2-50, Y_1_2)).collidepoint(x, y):
                    paused = False

                elif textMainMenu.get_rect(center=(X_1_2-50, Y_1_2 +50)).collidepoint(x, y):
                    show_main_menu()
                    paused = False
                    gameplayed = False


                elif textExitGame.get_rect(center=(X_1_2 - 50, Y_1_2 + 100)).collidepoint(x, y):
                    pygame.quit()
                    quit()



        DISPLAYSURF.blit(textPauseMenu, textPauseMenuRect)
        DISPLAYSURF.blit(textResumeGame, (X_1_2-50, Y_1_2))
        DISPLAYSURF.blit(textMainMenu, (X_1_2-50, Y_1_2 +50))
        DISPLAYSURF.blit(textExitGame, (X_1_2 - 50, Y_1_2 + 100))


        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


show_main_menu()
