import psycopg2 as p
import random

def op_questions_Historie():
    x = random.randint(0,14)
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cur.execute("select question from op_questions where category = 'Historie' and questionID > 15 and questionID < 31")

    rows = cur.fetchall()
    for r in rows[x]:
        print(r)
op_questions_Historie()

def mc_questions_Historie():
    con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
    cur = con.cursor()
    cur.execute("select * from mc_questions where category = 'Historie' and questionID > 0 and questionID < 16")

    rows = cur.fetchall()
    for r in rows:
        print(r)
#mc_questions_Historie()

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
