import sys, time, random
from Variables import *
# from Database import *
from pygame.locals import *

pygame.init()

fontObjLarge = pygame.font.Font('freesansbold.ttf', 32)  # declaring fonts
fontObjMedium = pygame.font.Font('freesansbold.ttf', 24)
fontObjSmall = pygame.font.Font('freesansbold.ttf', 18)


class Vector2:  # Vector Class
    def __init__(self, x, y):
        self.X = x
        self.Y = y


class Player:  # Player Class
    def __init__(self, playercircleicon, playerID=0, name="", icon=None, category="", posX=0, posY=0, correctanswers=0,
                 iconX=0,
                 iconY=0, circleX=0, circleY=0):
        self.PlayerID = playerID
        self.PlayerName = name
        self.PlayerIcon = icon
        self.Category = category
        self.Position = Vector2(posX, posY)
        self.CorrectAnswers = correctanswers
        self.IconPosition = Vector2(iconX, iconY)
        self.PlayerCirclePosition = Vector2(circleX, circleY)
        self.Direction = "UP"
        self.Score = 0
        self.PlayerCircleIcon = playercircleicon
        self.StartingDice = 0

    def movement(self):
        if self.Direction == "UP":
            self.Position.Y += Tools1.Steps
            self.icon_match()
        elif self.Direction == "DOWN":
            self.Position.Y -= Tools1.Steps
            self.icon_match()
        elif self.Direction == "RIGHT":
            if self.Position.X == 5 and Tools1.Steps == 3:
                self.Position -= 5
                self.icon_match()
            elif self.Position.X == 6 and Tools1.Steps == 2:
                self.Position.X -= 6
                self.icon_match()
            elif self.Position.X == 6 and Tools1.Steps == 3:
                self.Position.X -= 5
                self.icon_match()
            elif self.Position.X == 6 and Tools1.Steps == 1:
                self.Position.X -= 7
                self.icon_match()
            elif self.Position.X == 7 and Tools1.Steps == 2:
                self.Position.X -= 6
                self.icon_match()
            elif self.Position.X == 7 and Tools1.Steps == 3:
                self.Position.X -= 5
                self.icon_match()
            else:
                self.Position.X += Tools1.Steps
                self.icon_match()

        elif self.Direction == "LEFT":
            if self.Position.X == 0 and Tools1.Steps == 1:
                self.Position.X += 7
                self.icon_match()
            elif self.Position.X == 0 and Tools1.Steps == 2:
                self.Position.X += 6
                self.icon_match()
            elif self.Position.X == 0 and Tools1.Steps == 3:
                self.Position.X += 5
                self.icon_match()
            elif self.Position.X == 1 and Tools1.Steps == 2:
                self.Position.X += 6
                self.icon_match()
            elif self.Position.X == 1 and Tools1.Steps == 3:
                self.Position.X += 5
                self.icon_match()
            elif self.Position.X == 2 and Tools1.Steps == 3:
                self.Position.X += 5
                self.icon_match()
            else:
                self.Position.X -= Tools1.Steps
                self.icon_match()


    def get_rekt(self, down):
        self.Position.Y -= down
        self.icon_match()

    def update_icon(self):
        if self.PlayerIcon == "a":
            self.PlayerIcon = playerIcon_female1
        elif self.PlayerIcon == "b":
            self.PlayerIcon = playerIcon_female2
        elif self.PlayerIcon == "c":
            self.PlayerIcon = playerIcon_male1
        elif self.PlayerIcon == "d":
            self.PlayerIcon = playerIcon_male2

    def update_startPos(self):
        if self.Category == "Sport":
            self.Position.X = 0
        elif self.Category == "Geografie":
            self.Position.X = 2
        elif self.Category == "Entertainment":
            self.Position.X = 4
        elif self.Category == "Historie":
            self.Position.X = 6

    def icon_match(self):
        for key in tile_list:
            if self.Position.X == tile_list[key].Position.X and self.Position.Y == tile_list[key].Position.Y:
                self.PlayerCirclePosition.X = tile_list[key].DrawPos.X - 12
                self.PlayerCirclePosition.Y = tile_list[key].DrawPos.Y - 12


    def draw_icon(self):
        DISPLAYSURF.blit(self.PlayerCircleIcon, (self.PlayerCirclePosition.X, self.PlayerCirclePosition.Y))
        # pygame.draw.line(DISPLAYSURF, CORAL, (self.IconPosition.X,self.IconPosition.Y), (self.PlayerCirclePosition.X, self.PlayerCirclePosition.Y), 3)


player1 = Player(player1IconSmall, iconX=50, iconY=Y_1_3 - 50)  # Making objects of playerclass
player2 = Player(player2IconSmall, iconX=50, iconY=Y_2_3 - 50)
player3 = Player(player3IconSmall, iconX=WINDOWWIDTH - 200, iconY=Y_1_3 - 50)
player4 = Player(player4IconSmall, iconX=WINDOWWIDTH - 200, iconY=Y_2_3 - 50)

PlayerList = [player1, player2, player3, player4]  # List of playerobjects


class Tools():  # Tools class
    def __init__(self):
        self.Value = 0
        self.DiceImage = ""
        self.DiceResult = 0
        self.QuestionType = ""
        self.Steps = 0

    def dice(self):
        self.DiceResult = random.randint(1, 6)

    def steps(self):
        self.dice()
        self.question_type()
        if self.DiceResult == 1 or self.DiceResult == 2:
            self.Steps = 1
        elif self.DiceResult == 3 or self.DiceResult == 4:
            self.Steps = 2
        elif self.DiceResult == 5 or self.DiceResult == 6:
            self.Steps = 3

    def question_type(self):
        if self.DiceResult == 1 or self.DiceResult == 3 or self.DiceResult == 5:
            self.QuestionType = "Open"
        elif self.DiceResult == 2 or self.DiceResult == 4 or self.DiceResult == 6:
            self.QuestionType = "MC"

    def timer(self):
        i = 50

        while 1:
            i -= 1
            output = "\rTimer:%s" % str(i)
            sys.stdout.write(output)
            sys.stdout.flush()
            time.sleep(1)
            if i == 0:
                break

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


Tools1 = Tools()  # making tools object

class Tile:  # tiles for the map
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
        elif self.Category == "Historie":
            pygame.draw.circle(DISPLAYSURF, LIGHT_YELLOW, (self.DrawPos.X, self.DrawPos.Y), 10, 0)
        elif self.Category == "Win":
            pygame.draw.circle(DISPLAYSURF, BLACK, (self.DrawPos.X, self.DrawPos.Y), 13, 0)
        elif self.Category == "Bottom":
            pygame.draw.circle(DISPLAYSURF, WHITE, (self.DrawPos.X, self.DrawPos.Y), 10, 0)

    def get_attributes(self):
        return self.Category, self.Position.X, self.Position.Y, self.DrawPos.X, self.DrawPos.Y


def generate_tiles():  # Function that generates tiles on the map
    n = 640
    i = 60
    global tile_list
    tile_list = {}
    for x in range(1, 11):
        tile_list["tile_{}_{}_{}".format('blauw', x, 'a')] = Tile("Sport", 0, x, X_1_3, n)
        tile_list["tile_{}_{}_{}".format('blauw', x, 'b')] = Tile("Sport", 1, x, X_1_3 + i, n)
        tile_list["tile_{}_{}_{}".format('groen', x, 'a')] = Tile("Geografie", 2, x, X_1_3 + (2 * i), n)
        tile_list["tile_{}_{}_{}".format('groen', x, 'b')] = Tile("Geografie", 3, x, X_1_3 + (3 * i), n)
        tile_list["tile_{}_{}_{}".format('rood', x, 'a')] = Tile("Entertainment", 4, x, X_1_3 + (4 * i), n)
        tile_list["tile_{}_{}_{}".format('rood', x, 'b')] = Tile("Entertainment", 5, x, X_1_3 + (5 * i), n)
        tile_list["tile_{}_{}_{}".format('geel', x, 'a')] = Tile("Historie", 6, x, X_1_3 + (6 * i), n)
        tile_list["tile_{}_{}_{}".format('geel', x, 'b')] = Tile("Historie", 7, x, X_1_3 + (7 * i), n)
        n -= 40

    i = 30

    for y in range(12, 17):
        tile_list["tile_{}_{}_{}".format('blauw', y, 'a')] = Tile("Sport", 0, y, X_1_3 + i, n)
        tile_list["tile_{}_{}_{}".format('blauw', y, 'b')] = Tile("Sport", 1, y, X_1_3 + i, n)
        tile_list["tile_{}_{}_{}".format('groen', y, 'a')] = Tile("Geografie", 2, y, X_1_3 + (i * 5), n)
        tile_list["tile_{}_{}_{}".format('groen', y, 'b')] = Tile("Geografie", 3, y, X_1_3 + (i * 5), n)
        tile_list["tile_{}_{}_{}".format('rood', y, 'a')] = Tile("Entertainment", 4, y, X_1_3 + (i * 9), n)
        tile_list["tile_{}_{}_{}".format('rood', y, 'b')] = Tile("Entertainment", 5, y, X_1_3 + (i * 9), n)
        tile_list["tile_{}_{}_{}".format('geel', y, 'a')] = Tile("Historie", 6, y, X_1_3 + (i * 13), n)
        tile_list["tile_{}_{}_{}".format('geel', y, 'b')] = Tile("Historie", 7, y, X_1_3 + (i * 13), n)
        n -= 40

    for z in range(0, 9):
        tile_list["tile_{}_{}".format('Top', z)] = Tile("Win", z, 16, X_1_2 + 40, 30)

    i = 60

    n = 680
    for u in range(0, 8):
        if u % 2 == 0:
            tile_list["tile_{}_{}".format('Bottom', u)] = Tile("Bottom", u, 0, X_1_3 + (u*i), n)




def how_many_icons(AmountOfPlayers):  # amount of players screen
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


def show_turn(currentPlayer):  # shows whose turn it is
    showed = True
    abc = PlayerList[currentPlayer].PlayerName
    while showed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    showed = False

        textYourTurn = fontObjLarge.render("Hey {} it's your turn!".format(abc), True, BLACK, WHITE)
        textYourTurnRect = textYourTurn.get_rect()
        textYourTurnRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 5)

        DISPLAYSURF.blit(textYourTurn, textYourTurnRect)

        pygame.display.update()
        time.sleep(1)
        showed = False
        FPSCLOCK.tick(FPS / 2)


def input_name(players):  # takes input name
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
        textEnterNameRect.center = (X_1_2, Y_1_4)

        block = font.render(name, True, BLACK)
        rect = block.get_rect()
        rect.center = DISPLAYSURF.get_rect().center
        DISPLAYSURF.blit(block, rect)
        DISPLAYSURF.blit(textEnterName, textEnterNameRect)
        pygame.display.update()


def enter_name():  # loops input_name() for all active players
    entered = True
    j = 0

    while entered:
        for players in range(AmountOfPlayers):
            PlayerList[players].PlayerName = input_name(players)

        entered = False


def choose_icon():  # loops show_icon_menu for all active players
    chosen = True

    while chosen:
        for players in range(AmountOfPlayers):
            PlayerList[players].PlayerIcon = show_icon_menu(players)

        chosen = False


def choose_category_loop(AmountOfPlayers):
    cater = True

    while cater:
        for players in range(AmountOfPlayers):
            PlayerList[players].Category = choose_category(players)
        cater = False


def choose_category(currentPlayer):
    cat = True
    global sport, geog, entert, hist
    playerName = PlayerList[currentPlayer].PlayerName

    DISPLAYSURF.blit(backGroundImage, (0, 0))
    textCategory = fontObjLarge.render("Hey {} pick your Category".format(playerName), True, BLACK, WHITE)
    textCategoryRect = textCategory.get_rect()
    textCategoryRect.center = (X_1_2, (Y_1_4 - 100))

    DISPLAYSURF.blit(textCategory, textCategoryRect)

    textButtonSport = fontObjLarge.render("Sport", True, WHITE, BLUE)
    textButtonGeografie = fontObjLarge.render("Geografie", True, WHITE, GREEN)
    textButtonEntertainment = fontObjLarge.render("Entertainment", True, WHITE, RED)
    textButtonHistorie = fontObjLarge.render("Historie", True, WHITE, YELLOW)

    if sport == True:
        DISPLAYSURF.blit(textButtonSport, (X_1_3 - 50, Y_1_3))
    if geog == True:
        DISPLAYSURF.blit(textButtonGeografie, (X_1_3 - 50, Y_2_3))
    if entert == True:
        DISPLAYSURF.blit(textButtonEntertainment, (X_2_3 - 50, Y_1_3))
    if hist == True:
        DISPLAYSURF.blit(textButtonHistorie, (X_2_3 - 50, Y_2_3))

    pygame.display.update()

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
                if sport == True and textButtonSport.get_rect(center=(X_1_3 - 50, Y_1_3)).collidepoint(x, y):
                    PlayerList[currentPlayer].Category = "Sport"
                    PlayerList[currentPlayer].update_startPos()
                    sport = False
                    cat = False

                elif geog == True and textButtonGeografie.get_rect(center=(X_1_3 - 50, Y_2_3)).collidepoint(x, y):
                    PlayerList[currentPlayer].Category = "Geografie"
                    PlayerList[currentPlayer].update_startPos()
                    geog = False
                    cat = False

                elif entert == True and textButtonEntertainment.get_rect(center=(X_2_3 - 50, Y_1_3)).collidepoint(x, y):
                    PlayerList[currentPlayer].Category = "Entertainment"
                    PlayerList[currentPlayer].update_startPos()
                    entert = False
                    cat = False

                elif hist == True and textButtonHistorie.get_rect(center=(X_2_3 - 50, Y_2_3)).collidepoint(x, y):
                    PlayerList[currentPlayer].Category = "Historie"
                    PlayerList[currentPlayer].update_startPos()
                    hist = False
                    cat = False

        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)

def who_starts_loop():
    startsloop = True
    while startsloop:
        for players in range(len(ActivePlayers)):
            who_starts(players)

        startsloop = False


def who_starts(players):
    starts = True
    global currentPlayer
    p1DiceCheck = False
    p2DiceCheck = False
    p3DiceCheck = False
    p4DiceCheck = False

    textWhoStarts = fontObjLarge.render("Click your name to roll the dice and decide who starts", True, BLACK, WHITE)
    textWhoStartsRect = textWhoStarts.get_rect()
    textWhoStartsRect.center = (X_1_2, Y_1_4)

    textButtonContinue = fontObjMedium.render("Click to Continue", True, BLACK, LIGHT_CORAL)
    textButtonDice1 = fontObjMedium.render("Player1: {}".format(PlayerList[0].PlayerName), True, BLACK, LIGHT_CORAL)
    textButtonDice2 = fontObjMedium.render("Player2: {}".format(PlayerList[1].PlayerName), True, BLACK, LIGHT_CORAL)
    textButtonDice3 = fontObjMedium.render("Player3: {}".format(PlayerList[2].PlayerName), True, BLACK, LIGHT_CORAL)
    textButtonDice4 = fontObjMedium.render("Player4: {}".format(PlayerList[3].PlayerName), True, BLACK,LIGHT_CORAL)

    while starts:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if textButtonDice1.get_rect(center=(X_1_4-200, Y_1_2)).collidepoint(x, y):
                    p1DiceCheck = True
                    print(PlayerList[players].StartingDice)

                elif textButtonDice2.get_rect(center=(X_1_4+50, Y_1_2)).collidepoint(x, y):
                    p2DiceCheck = True
                    print(PlayerList[players].StartingDice)

                elif textButtonDice3.get_rect(center=(X_1_4+300, Y_1_2)).collidepoint(x, y):
                    p3DiceCheck = True
                    print(PlayerList[players].StartingDice)

                elif textButtonDice4.get_rect(center=(X_1_4+550, Y_1_2)).collidepoint(x, y):
                    p4DiceCheck = True
                    print(PlayerList[players].StartingDice)

                elif p1DiceCheck == True or p2DiceCheck == True or p3DiceCheck == True or p4DiceCheck == True and textButtonContinue.get_rect(center=(X_1_2-100, X_1_4+100)).collidepoint(x, y):
                    starts = False

        DISPLAYSURF.blit(backGroundImage, (0,0))
        DISPLAYSURF.blit(textWhoStarts, textWhoStartsRect)

        if p1DiceCheck:
            DISPLAYSURF.blit(p1Dice, (X_1_4-200, Y_1_2+100))
            DISPLAYSURF.blit(textButtonContinue, (X_1_2-100, Y_1_4 - 100))
        elif p2DiceCheck:
            DISPLAYSURF.blit(p1Dice, (X_1_4 - 200, Y_1_2 + 100))
            DISPLAYSURF.blit(p2Dice, (X_1_4 + 50, Y_1_2 + 100))
            DISPLAYSURF.blit(textButtonContinue, (X_1_2-100, Y_1_4 - 100))
        elif p3DiceCheck:
            DISPLAYSURF.blit(p1Dice, (X_1_4 - 200, Y_1_2 + 100))
            DISPLAYSURF.blit(p2Dice, (X_1_4 + 50, Y_1_2 + 100))
            DISPLAYSURF.blit(p3Dice, (X_1_4 + 300, Y_1_2 + 100))
            DISPLAYSURF.blit(textButtonContinue, (X_1_2-100, Y_1_4 - 100))
        elif p4DiceCheck:
            DISPLAYSURF.blit(p1Dice, (X_1_4 - 200, Y_1_2 + 100))
            DISPLAYSURF.blit(p2Dice, (X_1_4 + 50, Y_1_2 + 100))
            DISPLAYSURF.blit(p3Dice, (X_1_4 + 300, Y_1_2 + 100))
            DISPLAYSURF.blit(p4Dice, (X_1_4 + 550, Y_1_2 + 100))
            DISPLAYSURF.blit(textButtonContinue, (X_1_2-100, Y_1_4 - 100))

        if AmountOfPlayers == 1:
            DISPLAYSURF.blit(textButtonDice1, (X_1_4-200, Y_1_2))

        elif AmountOfPlayers == 2:
            DISPLAYSURF.blit(textButtonDice1, (X_1_4-200 , Y_1_2))
            DISPLAYSURF.blit(textButtonDice2, (X_1_4+50, Y_1_2))

        elif AmountOfPlayers == 3:
            DISPLAYSURF.blit(textButtonDice1, (X_1_4 - 200, Y_1_2))
            DISPLAYSURF.blit(textButtonDice2, (X_1_4+50, Y_1_2))
            DISPLAYSURF.blit(textButtonDice3, (X_1_4 + 300, Y_1_2))

        elif AmountOfPlayers == 4:
            DISPLAYSURF.blit(textButtonDice1, (X_1_4 - 200, Y_1_2))
            DISPLAYSURF.blit(textButtonDice2, (X_1_4+50, Y_1_2))
            DISPLAYSURF.blit(textButtonDice3, (X_1_4 + 300, Y_1_2))
            DISPLAYSURF.blit(textButtonDice4, (X_1_4 + 550, Y_1_2))


        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def pick_direction(currentPlayer):
    directed = True

    textButtonUp = fontObjLarge.render("  UP  ", True, BLACK, LIGHT_CORAL)
    textButtonDown = fontObjLarge.render("DOWN", True, BLACK, LIGHT_CORAL)
    textButtonRight = fontObjLarge.render("RIGHT", True, BLACK, LIGHT_CORAL)
    textButtonLeft = fontObjLarge.render("LEFT", True, BLACK, LIGHT_CORAL)

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



def compare_dices():
    comparing = True
    currentPlayer = 0
    while comparing:
        for players in range(AmountOfPlayers):
            if PlayerList[players].StartingDice > PlayerList[players+1].StartingDice:
                currentPlayer = players

        comparing = False
        return currentPlayer




def show_dice():  # shows dice result on screen
    return Tools1.show_dice_image()


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
        menuKnopInstructions = fontObjMedium.render('Instructions', True, BLACK, LIGHT_CORAL)
        menuKnopHighscores = fontObjMedium.render('Highscores', True, BLACK, LIGHT_CORAL)
        menuKnopExitGame = fontObjMedium.render('Exit Game', True, BLACK, LIGHT_CORAL)

        DISPLAYSURF.blit(backGroundImage, (0, 0))
        DISPLAYSURF.blit(textWelcome, textWelcomeRect)
        DISPLAYSURF.blit(menuKnopStart, (X_1_2 - 50, Y_1_2))
        DISPLAYSURF.blit(menuKnopLoadGame, (X_1_2 - 50, Y_1_2 + 50))
        DISPLAYSURF.blit(menuKnopInstructions, (X_1_2 - 50, Y_1_2 + 100))
        DISPLAYSURF.blit(menuKnopHighscores, (X_1_2 - 50, Y_1_2 + 150))
        DISPLAYSURF.blit(menuKnopExitGame, (X_1_2 - 50, Y_1_2 + 200))

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
                if menuKnopStart.get_rect(center=(X_1_2 - 50, Y_1_2)).collidepoint(x, y):
                    menud = False
                    show_gameplay()
                elif menuKnopInstructions.get_rect(center=(X_1_2 - 50, Y_1_2 + 100)).collidepoint(x, y):
                    menud = False
                    show_instructions_menu()
                elif menuKnopHighscores.get_rect(center=(X_1_2 - 50, Y_1_2 + 150)).collidepoint(x, y):
                    menud = False
                    show_highscore_menu()
                elif menuKnopExitGame.get_rect(center=(X_1_2 - 50, Y_1_2 + 200)).collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def show_instructions_menu():  # instruction screen 1
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if instructionsImage.get_rect().collidepoint(x, y):
                    instructions = False
                    show_instructions_menu1()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(instructionsImage, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def show_instructions_menu1():  # instructionscreen 2
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if instructionsImageNED1.get_rect().collidepoint(x, y):
                    instructions1 = False
                    show_instructions_menu2()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(instructionsImageNED1, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def show_instructions_menu2():  # instructionscreen 3
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if instructionsImageNED2.get_rect().collidepoint(x, y):
                    instructions2 = False
                    show_instructions_menu3()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(instructionsImageNED2, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def show_instructions_menu3():  # instruction screen 4
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if instructionsImageNED3.get_rect().collidepoint(x, y):
                    instructions3 = False
                    show_instructions_menu()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(instructionsImageNED3, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def show_players_menu():  # choose amount of players u want to play with
    chooseplayers = True

    global AmountOfPlayers

    textChoosePlayers = fontObjLarge.render('How many players?', True, BLACK, None)
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
                if textChoosePlayers1.get_rect(center=(X_1_2 - 50, Y_1_2)).collidepoint(x, y):
                    AmountOfPlayers = 1
                    chooseplayers = False
                if textChoosePlayers2.get_rect(center=(X_1_2 - 50, Y_1_2 + 50)).collidepoint(x, y):
                    AmountOfPlayers = 2
                    chooseplayers = False
                if textChoosePlayers3.get_rect(center=(X_1_2 - 50, Y_1_2 + 100)).collidepoint(x, y):
                    AmountOfPlayers = 3
                    chooseplayers = False
                if textChoosePlayers4.get_rect(center=(X_1_2 - 50, Y_1_2 + 150)).collidepoint(x, y):
                    AmountOfPlayers = 4
                    chooseplayers = False

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(backGroundImage, (0, 0))

        DISPLAYSURF.blit(textChoosePlayers, (X_1_2 - 100, Y_1_4))
        DISPLAYSURF.blit(textChoosePlayers1, (X_1_2 - 50, Y_1_2))
        DISPLAYSURF.blit(textChoosePlayers2, (X_1_2 - 50, Y_1_2 + 50))
        DISPLAYSURF.blit(textChoosePlayers3, (X_1_2 - 50, Y_1_2 + 100))
        DISPLAYSURF.blit(textChoosePlayers4, (X_1_2 - 50, Y_1_2 + 150))

        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def show_icon_menu(players):  # shows screen where players pick their icons
    global iconed, fem1, fem2, male1, male2
    iconed = True

    playerName = PlayerList[players].PlayerName

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(backGroundImage, (0, 0))

    textPlayerIcon = fontObjLarge.render('Hey {} please click on your preferred character!'.format(playerName), True,
                                         BLACK, None)
    textPlayerIconRect = textPlayerIcon.get_rect()
    textPlayerIconRect.center = (X_1_2, (Y_1_4 - 100))

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
                if fem1 == True and playerIcon_female1.get_rect(center=(X_1_5 - 100, Y_1_2 - 100)).collidepoint(x, y):
                    playerIcon = "a"
                    fem1 = False
                    iconed = False

                if fem2 == True and playerIcon_female2.get_rect(center=(X_2_5 - 100, Y_1_2 - 100)).collidepoint(x, y):
                    playerIcon = "b"
                    fem2 = False
                    iconed = False

                if male1 == True and playerIcon_male1.get_rect(center=(X_3_5 - 100, Y_1_2 - 100)).collidepoint(x, y):
                    playerIcon = "c"
                    male1 = False
                    iconed = False

                if male2 == True and playerIcon_male2.get_rect(center=(X_4_5 - 100, Y_1_2 - 100)).collidepoint(x, y):
                    playerIcon = "d"
                    male2 = False
                    iconed = False

        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)
    return playerIcon


def show_gameplay():  # loop for gameplay
    global gameplayed, berlp, currentPlayer
    berlp = show_dice()
    gameplayed = True
    currentPlayer = compare_dices()
    currentRound = 1
    show_players_menu()
    enter_name()
    choose_icon()
    how_many_icons(AmountOfPlayers)
    who_starts_loop()
    choose_category_loop(AmountOfPlayers)


    while gameplayed:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    show_pause()

                elif event.key == pygame.K_d:
                    if currentPlayer < len(ActivePlayers) - 1:
                        currentPlayer += 1
                        berlp = show_dice()
                        show_turn(currentPlayer)
                        PlayerList[currentPlayer].movement()
                        PlayerList[currentPlayer].draw_icon()
                        pygame.display.update()

                        if currentRound > 1:
                            pick_direction(currentPlayer)
                            berlp = show_dice()
                            pygame.display.update()

                        PlayerList[currentPlayer].movement()
                        PlayerList[currentPlayer].draw_icon()
                        pygame.display.update()

                    else:
                        currentRound+= 1
                        currentPlayer = 0
                        show_turn(currentPlayer)
                        if currentRound > 1:
                            pick_direction(currentPlayer)
                            berlp = show_dice()
                            pygame.display.update()

                        PlayerList[currentPlayer].movement()
                        PlayerList[currentPlayer].draw_icon()
                        pygame.display.update()

        generate_tiles()

        DISPLAYSURF.blit(backGroundImage, (0, 0))

        abc = PlayerList[currentPlayer].PlayerName

        textWhoseTurn = fontObjLarge.render("It's {}'s turn".format(abc), True, BLACK, WHITE)
        textWhoseTurnRect = textWhoseTurn.get_rect()
        textWhoseTurnRect.center = (X_1_4 - 130, Y_1_4 - 40)

        textCurrentRound = fontObjLarge.render("Round: {}".format(currentRound), True, BLACK, WHITE)
        textCurrentRoundRect = textCurrentRound.get_rect()
        textCurrentRoundRect.center = (X_1_4-150, Y_1_4 - 80)

        textDiceResult = fontObjSmall.render("{}'s Dice Result:".format(abc), True, BLACK, WHITE)
        textDiceResultRect = textDiceResult.get_rect()
        textDiceResultRect.center = (WINDOWWIDTH-150, 20)

        DISPLAYSURF.blit(berlp, (WINDOWWIDTH - 200, 40))

        textStepsResult = fontObjSmall.render('Steps Result: {}'.format(Tools1.Steps),True, BLACK, WHITE)
        textStepsResultRect = textStepsResult.get_rect()
        textStepsResultRect.center = (WINDOWWIDTH - 150, 170)

        textQuestionType = fontObjSmall.render('Question Type: {}'.format(Tools1.QuestionType), True, BLACK, WHITE)
        textQuestionTypeRect = textQuestionType.get_rect()
        textQuestionTypeRect.center = (WINDOWWIDTH - 150, 200)

        DISPLAYSURF.blit(textDiceResult, textDiceResultRect)
        DISPLAYSURF.blit(textStepsResult, textStepsResultRect)
        DISPLAYSURF.blit(textQuestionType, textQuestionTypeRect)



        textPlayer1Name = fontObjMedium.render("P1: {}".format(PlayerList[0].PlayerName), True, BLACK, WHITE)
        textPlayer1Dir = fontObjSmall.render("Direction: {}".format(PlayerList[0].Direction), True, BLACK, WHITE)
        textPlayer2Name = fontObjMedium.render("P2: {}".format(PlayerList[1].PlayerName), True, BLACK, WHITE)
        textPlayer2Dir = fontObjSmall.render("Direction: {}".format(PlayerList[1].Direction), True, BLACK, WHITE)
        textPlayer3Name = fontObjMedium.render("P3: {}".format(PlayerList[2].PlayerName), True, BLACK, WHITE)
        textPlayer3Dir = fontObjSmall.render("Direction: {}".format(PlayerList[2].Direction), True, BLACK, WHITE)
        textPlayer4Name = fontObjMedium.render("P4: {}".format(PlayerList[3].PlayerName), True, BLACK, WHITE)
        textPlayer4Dir = fontObjSmall.render("Direction: {}".format(PlayerList[3].Direction), True, BLACK, WHITE)


        DISPLAYSURF.blit(textWhoseTurn, textWhoseTurnRect)
        DISPLAYSURF.blit(textCurrentRound, textCurrentRoundRect)


        for key in tile_list:
            tile_list[key].draw_tile()

        for k in range(AmountOfPlayers):
            PlayerList[k].icon_match()
            PlayerList[k].draw_icon()

        for j in range(AmountOfPlayers):
            if PlayerList[j].Position.Y >= 16:
                PlayerList[j].Score += 1
                gameplayed = False
                print(PlayerList[j].Score)
                show_main_menu()

        pygame.display.update()

        if AmountOfPlayers == 1:
            DISPLAYSURF.blit(textPlayer1Name, (50, Y_1_3 - 50))
            DISPLAYSURF.blit(textPlayer1Dir, (50, Y_1_3 - 25))
            DISPLAYSURF.blit(player1.PlayerIcon, (0, Y_1_3))

        elif AmountOfPlayers == 2:
            DISPLAYSURF.blit(textPlayer1Name, (50, Y_1_3 - 50))
            DISPLAYSURF.blit(textPlayer1Dir, (50, Y_1_3 - 25))
            DISPLAYSURF.blit(player1.PlayerIcon, (0, Y_1_3))

            DISPLAYSURF.blit(textPlayer2Name, (50, Y_2_3 - 50))
            DISPLAYSURF.blit(textPlayer2Dir, (50, Y_2_3 - 25))
            DISPLAYSURF.blit(player2.PlayerIcon, (0, Y_2_3))

        elif AmountOfPlayers == 3:
            DISPLAYSURF.blit(textPlayer1Name, (50, Y_1_3 - 50))
            DISPLAYSURF.blit(textPlayer1Dir, (50, Y_1_3 - 25))
            DISPLAYSURF.blit(player1.PlayerIcon, (0, Y_1_3))

            DISPLAYSURF.blit(textPlayer2Name, (50, Y_2_3 - 50))
            DISPLAYSURF.blit(textPlayer2Dir, (50, Y_2_3 - 25))
            DISPLAYSURF.blit(player2.PlayerIcon, (0, Y_2_3))

            DISPLAYSURF.blit(textPlayer3Name, (WINDOWWIDTH - 170, Y_1_3 + 25))
            DISPLAYSURF.blit(textPlayer3Dir, (WINDOWWIDTH - 170, Y_1_3 + 50))
            DISPLAYSURF.blit(player3.PlayerIcon, (WINDOWWIDTH - 200, Y_1_3+75))

        elif AmountOfPlayers == 4:
            DISPLAYSURF.blit(textPlayer1Name, (50, Y_1_3 - 50))
            DISPLAYSURF.blit(textPlayer1Dir, (50, Y_1_3 - 25))
            DISPLAYSURF.blit(player1.PlayerIcon, (0, Y_1_3))

            DISPLAYSURF.blit(textPlayer2Name, (50, Y_2_3 - 50))
            DISPLAYSURF.blit(textPlayer2Dir, (50, Y_2_3 - 25))
            DISPLAYSURF.blit(player2.PlayerIcon, (0, Y_2_3))

            DISPLAYSURF.blit(textPlayer3Name, (WINDOWWIDTH - 170, Y_1_3 - 50))
            DISPLAYSURF.blit(textPlayer3Dir, (WINDOWWIDTH - 170, Y_1_3 - 25))
            DISPLAYSURF.blit(player3.PlayerIcon, (WINDOWWIDTH - 200, Y_1_3))

            DISPLAYSURF.blit(textPlayer4Name, (WINDOWWIDTH - 170, Y_2_3 - 50))
            DISPLAYSURF.blit(textPlayer4Dir, (WINDOWWIDTH - 170, Y_2_3 - 25))
            DISPLAYSURF.blit(player4.PlayerIcon, (WINDOWWIDTH - 200, Y_2_3))

        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)


def show_highscore_menu():  # shows highscore screen
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


def show_pause():  # shows pause menu, is bugged atm
    global paused
    global gameplayed
    paused = True

    textPauseMenu = fontObjLarge.render('Welcome to the Pause Menu', True, BLACK, None)
    textPauseMenuRect = textPauseMenu.get_rect()
    textPauseMenuRect.center = (X_1_2, WINDOWHEIGHT / 4)

    textResumeGame = fontObjLarge.render('Resume Game', True, BLACK, LIGHT_CORAL)
    textMainMenu = fontObjLarge.render('Main Menu', True, BLACK, LIGHT_CORAL)
    textExitGame = fontObjLarge.render("Exit Game", True, BLACK, LIGHT_CORAL)

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
                if textResumeGame.get_rect(center=(X_1_2 - 50, Y_1_2)).collidepoint(x, y):
                    paused = False

                elif textMainMenu.get_rect(center=(X_1_2 - 50, Y_1_2 + 75)).collidepoint(x, y):
                    show_main_menu()
                    paused = False
                    gameplayed = False


                elif textExitGame.get_rect(center=(X_1_2 - 50, Y_1_2 + 150)).collidepoint(x, y):
                    pygame.quit()
                    quit()

        DISPLAYSURF.blit(textPauseMenu, textPauseMenuRect)
        DISPLAYSURF.blit(textResumeGame, (X_1_2 - 50, Y_1_2))
        DISPLAYSURF.blit(textMainMenu, (X_1_2 - 50, Y_1_2 + 75))
        DISPLAYSURF.blit(textExitGame, (X_1_2 - 50, Y_1_2 + 150))

        pygame.display.update()
        FPSCLOCK.tick(FPS / 2)



p1Dice = show_dice()
player1.StartingDice = Tools1.DiceResult
p2Dice = show_dice()
player2.StartingDice = Tools1.DiceResult
p3Dice = show_dice()
player3.StartingDice = Tools1.DiceResult
p4Dice = show_dice()
player4.StartingDice = Tools1.DiceResult

show_main_menu()