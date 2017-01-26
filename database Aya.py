#import psycopg2 as p

#con = p.connect("dbname='project2' user='postgres' host='localhost' password='ayasagr1998'")
#cur = con.cursor()
#cur.execute("select* from mc_questions")
#rows = cur.fetchall()
#for r in rows:
#    print(r)


import math
import pygame
import psycopg2

#number = int(input('what is ur number')) not working!
command = input("Select * from highscores")


# use database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=project2 user=postgres")
    cursor = connection.cursor()

    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()
    print(results)

# Uploads a score into the hiscore table
def upload_score(name, score):
    interact_with_database("UPDATE score SET score = {} WHERE name = '{}'"
                        .format(name, score))

# Downloads score data from database   dont know this either
def download_scores():
    return interact_with_database("SELECT * FROM score")

# Downloads the top score from database
def download_top_score():
    result = interact_with_database("SELECT * FROM highscores ORDER BY score")[0][1]
    return result


interact_with_database(command)

interact_with_database("select * from highscores")
