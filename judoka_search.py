#!/usr/bin/env python

import psycopg2
import sys

def search_db(args):
    query = """ SELECT * FROM judoka WHERE (ftechnique = %s AND height=%s AND gender=%s AND categories=%s)"""
    cur.execute(query, (args[0], args[1], args[2], args[3]))

if __name__ == "__main__":
    try:
        args = sys.argv
        print(args)
    except:
        print("Please enter arguments")
        print("[Fav. technique] [Height] [Gender] [Category]")
        exit()
