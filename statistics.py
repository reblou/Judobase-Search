#!/usr/bin/env python

import psycopg2

def avg_height():
    conn = psycopg2.connect(database="judoka")
    cur = conn.cursor()
    cur.execute("""SELECT categories, SUM(height), COUNT(*) FROM judoka GROUP BY categories""")
    res = cur.fetchall()
    print("Average height of top judoka in each category:")
    for r in res:
        print(r[0], ":", round(r[1] / r[2]), "cm")
    conn.close()
    return

def most_popular_techniques():
    conn = psycopg2.connect(database="judoka")
    cur = conn.cursor()
    cur.execute("""SELECT COUNT(*), ftechnique FROM judoka GROUP BY ftechnique ORDER BY count DESC""")
    res = cur.fetchall()
    print("Technique : Frequency")
    for r in res:
        print(r[1], ":", r[0])

if __name__ == "__main__":
    avg_height()
    most_popular_techniques()
