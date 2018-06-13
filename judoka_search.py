#!/usr/bin/env python

import sys
import main
import re

def search_technique(data, technique):
    for id, judoka in data["competitors"].items():
        if (re.match(technique, judoka['ftechique'])):
            #print(id)
            #print(data["competitors"][id]["family_name"])
            print_results(data["competitors"][id], id)

""" Makes regex for maching argument to data technique name."""
def make_regex(argu):
    rx = ".*[" + argu[0].upper()
    rx += argu[0] + "]"
    for char in argu[1:]:
        rx += char + "-*.*"

    return rx

def print_results(data, id):
    # wc(s)

    print("--", id, ":", data["given_name"], data["family_name"])
    print("\t" + data["ftechique"])
    print("\t" + data["gender"])
    print("\t" + data["age"], "years old")
    print("\t" + data["height"] + "cm")
    print("\t" + data["country"])
    print("\t" + data["points"], "points")
    print("\t" + data["place"], "place")
    #print("\t" + data["categories"])
    print()




if __name__ == "__main__":
    d = main.read_from_file()
    ars = sys.argv
    ars.pop(0)
    search_technique(d, make_regex(ars[0]))

    """
    except Exception as e:
        print(str(e))
        print("Please enter arguments:")
        print("[Fav. technique] [Height] [Gender] [Category]")
        exit()
        """
