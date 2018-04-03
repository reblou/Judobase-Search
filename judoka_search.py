#!/usr/bin/env python

import psycopg2
import sys

def search_technique(technique):
    conn = psycopg2.connect(database="judoka")
    cur = conn.cursor()
    query = """ SELECT * FROM judoka WHERE (ftechnique = %s)"""
    cur.execute(query, (technique,))
    return cur.fetchall()

if __name__ == "__main__":
    try:
        ars = sys.argv
        print(ars)
        if (len(ars) < 5):
            raise Exception('Not enough arguments')
        ars.pop(0)
        res = search_technique(ars[0])
        print(res)

    except Exception as e:
        print(str(e))
        print("Please enter arguments:")
        print("[Fav. technique] [Height] [Gender] [Category]")
        exit()
