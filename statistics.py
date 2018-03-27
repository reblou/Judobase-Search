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
    print()
    return

def most_popular_techniques():
    conn = psycopg2.connect(database="judoka")
    cur = conn.cursor()
    cur.execute("""SELECT COUNT(*), ftechnique FROM judoka GROUP BY ftechnique ORDER BY count DESC""")
    res = cur.fetchall()
    print("Technique : Frequency")
    for r in res:
        print(r[1], ":", r[0])
    conn.close()
    print()
    return

def technique_by_category():
    conn = psycopg2.connect(database="judoka")
    cur = conn.cursor()

    try:
        cur.execute("DROP VIEW frequencies")
    except:
        pass

    cur.execute("CREATE VIEW frequencies AS (SELECT COUNT(*), categories, ftechnique FROM judoka GROUP BY ftechnique, categories)")
    cur.execute("SELECT max, a.categories, a.ftechnique FROM frequencies a INNER JOIN (SELECT categories, MAX(count) FROM frequencies as t GROUP BY categories) as b ON a.categories = b.categories AND a.count = b.max")
    res = cur.fetchall()
    for r in res:
        print(r)
    conn.close()
    print()
    return



if __name__ == "__main__":
    avg_height()
    most_popular_techniques()
    technique_by_category()
