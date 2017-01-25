import psycopg2 as p

con = p.connect("dbname='euromast' user='postgres' host='localhost' password='Drakenadem97'")
cur = con.cursor()
cur.execute("select * from op_questions where category = 'Sport'")
rows = cur.fetchall()


for r in rows:
    print(r)

