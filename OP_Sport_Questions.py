import psycopg2 as p
import random, time
import pygame
global cool
import Variables
from Variables import *


def Openvragen_Sport():
    questionID = (random.randint(0,14))
    con = p.connect("dbname='project2' user='postgres' host='localhost' password='Drakenadem97'")


    def op_questions_Sport():
        cur = con.cursor()
        cur.execute("select question from op_questions where category = 'Sport' and questionID > 45 and questionID < 61")
        rows = cur.fetchall()
        for r in rows[questionID]:
            return(r)
    output_questions = op_questions_Sport()
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    font = pygame.font.Font(None, 25)
    font2 = pygame.font.Font(None, 35)

    def op_answers_Sport(name):
        cor = con.cursor()
        cor.execute("select correctanswer from op_questions where category = 'Sport' and questionID > 45 and questionID < 61")
        raws = cor.fetchall()
        for i in raws[questionID]:
            if len(name) < 3:
                return("Incorrect!")
            elif name in i.lower():
                Variables.correctAnswer = True
                return("Correct!")
            else:
                return("Incorrect!")

    def insert_answer():
        name = ""
        Loop = True
        while Loop:
            for evt in pygame.event.get():
                if evt.type == pygame.KEYDOWN:
                    if evt.type == pygame.QUIT:
                        Loop = False
                    if evt.unicode.isalpha():
                        name += evt.unicode
                    elif evt.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif evt.key == pygame.K_SPACE:
                        name = name + " "
                    elif evt.key == pygame.K_RETURN:
                        check_answer = op_answers_Sport(name)
                        DISPLAYSURF.blit(backGroundImage, (0, 0))
                        answer = font2.render(check_answer, True, (0, 0, 0))
                        screen.blit(answer, (412, 364))
                        pygame.display.flip()
                        time.sleep(2)
                        Loop = False

            DISPLAYSURF.blit(backGroundImage, (0, 0))
            show_input = font2.render(name, 1, (0, 0, 0))
            show_question = font.render(output_questions, True, (0, 0, 0))
            rect = show_question.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(show_question, rect)
            screen.blit(show_input, (412, 464))
            pygame.display.flip()
    insert_answer()
