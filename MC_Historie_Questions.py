import psycopg2 as p
import random, time
import pygame
global cool
from Variables import *

def Meerkeuzevragen_Historie():
    questionID = (random.randint(0,14))
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")


    def op_questions_Historie():
        cur = con.cursor()
        cur.execute("select question from mc_questions where category = 'Historie' and questionID > 0 and questionID < 16")
        rows = cur.fetchall()
        for r in rows[questionID]:
            return(r)
    output_questions = op_questions_Historie()

    def Answer_a_Historie():
        cor = con.cursor()
        cor.execute("select answera from mc_questions where category = 'Historie' and questionID > 0 and questionID < 16")
        raws = cor.fetchall()
        for i in raws[questionID]:
           return(i)
    answer_choice_a = Answer_a_Historie()

    def Answer_b_Historie():
        cor = con.cursor()
        cor.execute("select answerb from mc_questions where category = 'Historie' and questionID > 0 and questionID < 16")
        raws = cor.fetchall()
        for i in raws[questionID]:
           return(i)
    answer_choice_b = Answer_b_Historie()

    def Answer_c_Historie():
        cor = con.cursor()
        cor.execute("select answerc from mc_questions where category = 'Historie' and questionID > 0 and questionID < 16")
        raws = cor.fetchall()
        for i in raws[questionID]:
           return(i)
    answer_choice_c = Answer_c_Historie()

    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    font = pygame.font.Font(None, 25)
    font2 = pygame.font.Font(None, 35)

    def mc_answers_Historie(name):
        cor = con.cursor()
        cor.execute("select correctanswer from mc_questions where category = 'Historie' and questionID > 0 and questionID < 16")
        raws = cor.fetchall()
        for q in raws[questionID]:
            if name in q.lower():
                return("Answer is correct!")
            else:
                return("Answer is incorrect :(")

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
                        check_answer = mc_answers_Historie(name)
                        DISPLAYSURF.blit(backGroundImage, (0, 0))
                        answer = font2.render(check_answer, True, (0, 0, 0))
                        screen.blit(answer, (412, 364))
                        pygame.display.flip()
                        time.sleep(2)
                        Loop = False


            DISPLAYSURF.blit(backGroundImage, (0, 0))
            show_input = font2.render(name, 1, (0, 0, 0))
            show_answer_a = font.render(answer_choice_a, True, (0,0,0))
            show_answer_b = font.render(answer_choice_b, True, (0,0,0))
            show_answer_c = font.render(answer_choice_c, True, (0,0,0))
            show_question = font.render(output_questions, True, (0, 0, 0))
            rect = show_question.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(show_answer_a, (50,600))
            screen.blit(show_answer_b, (391,600))
            screen.blit(show_answer_c, (733,600))
            screen.blit(show_question, rect)
            screen.blit(show_input, (412, 464))
            pygame.display.flip()
    insert_answer()
