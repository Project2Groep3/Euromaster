import psycopg2 as p
import random, time
import pygame
global cool
def Openvragen_Historie():
    questionID = (random.randint(0,14))
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")


    def op_questions_Historie():
        cur = con.cursor()
        cur.execute("select question from op_questions where category = 'Historie' and questionID > 15 and questionID < 31")
        rows = cur.fetchall()
        for r in rows[questionID]:
            return(r)
    output_questions = op_questions_Historie()
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    font = pygame.font.Font(None, 25)

    def op_answers_Historie(name):
        cor = con.cursor()
        cor.execute("select correctanswer from op_questions where category = 'Historie' and questionID > 15 and questionID < 31")
        raws = cor.fetchall()
        for i in raws[questionID]:
            if name in i.lower():
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
                        check_answer = op_answers_Historie(name)
                        screen.fill((0, 0, 0))
                        answer = font.render(check_answer, True, (255, 255, 255))
                        screen.blit(answer, (100,264))
                        pygame.display.flip()
                        time.sleep(2)
                        Loop = False

            screen.fill((0, 0, 0))
            show_input = font.render(name, 1, (255, 255, 255))
            show_question = font.render(output_questions, True, (255, 255, 255))
            rect = show_question.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(show_question, rect)
            screen.blit(show_input, (341,200))
            pygame.display.flip()
    insert_answer()
