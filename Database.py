import psycopg2 as p
import random

def op_questions_Historie():
    x = random.randint(0,14)
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cor = con.cursor()
    cur.execute("select question from op_questions where category = 'Historie' and questionID > 15 and questionID < 31")
    cor.execute("select correctanswer from op_questions where category = 'Historie' and questionID > 15 and questionID < 31")
    rows = cur.fetchall()
    raws = cor.fetchall()

    for r in rows[x]:
        print(r)
    for i in raws[x]:
        a = input("")
        print(i)
        if len(a) < 3:
            return("Answer is incorrect :(")
        elif a in i.lower():
            return("Answer is correct!")
        else:
            return("Answer is incorrect :(")
op_questions_Historie()


def mc_questions_Historie():
    x = random.randint(0,14)
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cor = con.cursor()
    car = con.cursor()
    cur.execute("select question from mc_questions where category = 'Historie' and questionID > 0 and questionID < 16")
    cor.execute("select answera,answerb,answerc from mc_questions where category = 'Historie' and questionID > 0 and questionID < 16")
    car.execute("select correctanswer from mc_questions where category = 'Historie' and questionID > 0 and questionID < 16")
    rows = cur.fetchall()
    raws = cor.fetchall()
    roews = car.fetchall()

    for r in rows[x]:
        print(r)
        for i in raws[x]:
            print(i)
        for q in roews[x]:
            a = input("")
            if a in q.lower():
                return("Answer is correct!")
            else:
                return("Answer is incorrect :(")
#mc_questions_Historie()


def op_questions_Sport():
    x = random.randint(0,14)
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cor = con.cursor()
    cur.execute("select question from op_questions where category = 'Sport' and questionID > 45 and questionID < 61")
    cor.execute("select correctanswer from op_questions where category = 'Sport' and questionID > 45 and questionID < 61")
    rows = cur.fetchall()
    raws = cor.fetchall()

    for r in rows[x]:
        print(r)
    for i in raws[x]:
        a = input("")
        print(i)
        if len(a) < 3:
            return("Answer is incorrect :(")
        elif a in i.lower():
            return("Answer is correct!")
        else:
            return("Answer is incorrect :(")
#op_questions_Sport()

def mc_questions_Sport():
    x = random.randint(0,14)
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cor = con.cursor()
    car = con.cursor()
    cur.execute("select question from mc_questions where category = 'Sport' and questionID > 30 and questionID < 46")
    cor.execute("select answera,answerb,answerc from mc_questions where category = 'Sport' and questionID > 30 and questionID < 46")
    car.execute("select correctanswer from mc_questions where category = 'Sport' and questionID > 30 and questionID < 46")
    rows = cur.fetchall()
    raws = cor.fetchall()
    roews = car.fetchall()
    for r in rows[x]:
        print(r)
        for i in raws[x]:
            print(i)
        for q in roews[x]:
            a = input("")
            if a in q.lower():
                return("Answer is correct!")
            else:
                return("Answer is incorrect :(")
#mc_questions_Sport()

def op_questions_Entertainment():
    x = random.randint(0,14)
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cor = con.cursor()
    cur.execute("select question from op_questions where category = 'Entertainment' and questionID > 75 and questionID < 91")
    cor.execute("select correctanswer from op_questions where category = 'Entertainment' and questionID > 75 and questionID < 91")
    rows = cur.fetchall()
    raws = cor.fetchall()

    for r in rows[x]:
        print(r)
    for i in raws[x]:
        a = input("")
        print(i)
        if len(a) < 3:
            return("Answer is incorrect :(")
        elif a in i.lower():
            return("Answer is correct!")
        else:
            return("Answer is incorrect :(")
#op_questions_Entertainment()

def mc_questions_Entertainment():
    x = random.randint(0,14)
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cor = con.cursor()
    car = con.cursor()
    cur.execute("select question from mc_questions where category = 'Entertainment' and questionID > 60 and questionID < 76")
    cor.execute("select answera,answerb,answerc from mc_questions where category = 'Entertainment' and questionID > 60 and questionID < 76")
    car.execute("select correctanswer from mc_questions where category = 'Entertainment' and questionID > 60 and questionID < 76")
    rows = cur.fetchall()
    raws = cor.fetchall()
    roews = car.fetchall()
    for r in rows[x]:
        print(r)
        for i in raws[x]:
            print(i)
        for q in roews[x]:
            a = input("")
            if a in q.lower():
                return("Answer is correct!")
            else:
                return("Answer is incorrect :(")
#mc_questions_Entertainment()

def op_questions_Geografie():
    x = random.randint(0,14)
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cor = con.cursor()
    cur.execute("select question from op_questions where category = 'Geografie' and questionID > 105 and questionID < 121")
    cor.execute("select correctanswer from op_questions where category = 'Geografie' and questionID > 105 and questionID < 121")
    rows = cur.fetchall()
    raws = cor.fetchall()

    for r in rows[x]:
        print(r)
    for i in raws[x]:
        a = input("")
        print(i)
        if len(a) < 3:
            return("Answer is incorrect :(")
        elif a in i.lower():
            return("Answer is correct!")
        else:
            return("Answer is incorrect :(")
#op_questions_Geografie()

def mc_questions_Geografie():
    x = random.randint(0,14)
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cor = con.cursor()
    car = con.cursor()
    cur.execute("select question from mc_questions where category = 'Geografie' and questionID > 90 and questionID < 106")
    cor.execute("select answera,answerb,answerc from mc_questions where category = 'Geografie' and questionID > 90 and questionID < 106")
    car.execute("select correctanswer from mc_questions where category = 'Geografie' and questionID > 90 and questionID < 106")
    rows = cur.fetchall()
    raws = cor.fetchall()
    roews = car.fetchall()
    for r in rows[x]:
        print(r)
        for i in raws[x]:
            print(i)
        for q in roews[x]:
            a = input("")
            if a in q.lower():
                return("Answer is correct!")
            else:
                return("Answer is incorrect :(")
#mc_questions_Geografie()
qq = op_questions_Historie()
while True:
    op_questions_Historie()
