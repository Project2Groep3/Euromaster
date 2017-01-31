import psycopg2 as p
import random, time
import pygame
global cool
from Variables import *
def Openvragen_Entertainment():
    questionID = (random.randint(0,14))
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")


    def op_questions_Entertainment():
        cur = con.cursor()
        cur.execute("select question from op_questions where category = 'Entertainment' and questionID > 75 and questionID < 91")
        rows = cur.fetchall()
        for r in rows[questionID]:
            return(r)
    output_questions = op_questions_Entertainment()
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    font = pygame.font.Font(None, 25)
    font2 = pygame.font.Font(None, 35)

    def op_answers_Entertainment(name):
        cor = con.cursor()
        cor.execute("select correctanswer from op_questions where category = 'Entertainment' and questionID > 75 and questionID < 91")
        raws = cor.fetchall()
        for i in raws[questionID]:
            if len(name) < 3:
                return("Answer is incorrect :(")
            elif name in i.lower():
                return("Answer is correct!")
            else:
                return("Answer is incorrect :(")

    def insert_answer():
        tijd = 50
        counter, text = tijd, str(tijd).rjust(3)
        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 100)
        clock.tick(30)
        name = ""
        Loop = True
        while Loop:
            for evt in pygame.event.get():
                if counter < 1:
                    Loop = False
                    pygame.display.flip()
                if evt.type == pygame.USEREVENT:
                    counter -= 0.1
                    text = str(round(counter,1)).rjust(3) if counter > 0 else "0".rjust(3)
                    pygame.display.flip()
                if evt.type == pygame.KEYDOWN:
                    if evt.type == pygame.QUIT:
                        Loop = False
                    if evt.unicode.isalpha():
                        name += evt.unicode
                    if evt.key == pygame.K_0:
                        name = name + "0"
                    if evt.key == pygame.K_1:
                        name = name + "1"
                    if evt.key == pygame.K_2:
                        name = name + "2"
                    if evt.key == pygame.K_3:
                        name = name + "3"
                    if evt.key == pygame.K_4:
                        name = name + "4"
                    if evt.key == pygame.K_5:
                        name = name + "5"
                    if evt.key == pygame.K_6:
                        name = name + "6"
                    if evt.key == pygame.K_7:
                        name = name + "7"
                    if evt.key == pygame.K_8:
                        name = name + "8"
                    if evt.key == pygame.K_9:
                        name = name + "9"
                    elif evt.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif evt.key == pygame.K_SPACE:
                        name = name + " "
                    elif evt.key == pygame.K_RETURN:
                        check_answer = op_answers_Entertainment(name)
                        DISPLAYSURF.blit(backGroundImage, (0, 0))
                        answer = font2.render(check_answer, True, (0, 0, 0))
                        screen.blit(answer, (412, 364))
                        pygame.display.flip()
                        time.sleep(2)
                        Loop = False
            else:
                screen.blit(font2.render(text, True, (255, 255, 255)), (22, 28))
                pygame.display.flip()
                clock.tick(30)

            DISPLAYSURF.blit(backGroundImage, (0, 0))
            show_input = font2.render(name, 1, (0, 0, 0))
            show_question = font.render(output_questions, True, (0, 0, 0))
            rect = show_question.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(show_question, rect)
            screen.blit(show_input, (412, 164))
            pygame.display.flip()
    insert_answer()
