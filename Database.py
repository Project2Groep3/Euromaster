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
adq = op_questions_Historie()
print(adq)

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
adf = mc_questions_Historie()
print(adf)

def op_questions_Sport():
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cur.execute("select * from op_questions where category = 'Sport' and questionID > 45 and questionID < 61")

    rows = cur.fetchall()
    for r in rows:
        print(r)
#op_questions_Sport()

def mc_questions_Sport():
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cur.execute("select * from mc_questions where category = 'Sport' and questionID > 30 and questionID < 46")

    rows = cur.fetchall()
    for r in rows:
        print(r)
#mc_questions_Sport()

def op_questions_Entertainment():
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cur.execute("select * from op_questions where category = 'Sport' and questionID > 75 and questionID < 91")

    rows = cur.fetchall()
    for r in rows:
        print(r)
#op_questions_Entertainment()

def mc_questions_Entertainment():
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cur.execute("select * from op_questions where category = 'Sport' and questionID > 60 and questionID < 76")

    rows = cur.fetchall()
    for r in rows:
        print(r)
#mc_questions_Entertainment()

def op_questions_Geografie():
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cur.execute("select * from op_questions where category = 'Sport' and questionID > 105 and questionID < 121")

    rows = cur.fetchall()
    for r in rows:
        print(r)
#op_questions_Geografie()

def mc_questions_Geografie():
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cur.execute("select * from op_questions where category = 'Sport' and questionID > 90 and questionID < 106")

    rows = cur.fetchall()
    for r in rows:
        print(r)
#mc_questions_Geografie()
