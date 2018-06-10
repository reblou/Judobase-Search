#!/usr/bin/env python

import sys
import main

def search_technique(data, technique):
    for judoka in data["competitors"].values():
        print(judoka['ftechique'])


if __name__ == "__main__":
    d = main.read_from_file()
    ars = sys.argv
    print(ars)
    ars.pop(0)
    res = search_technique(d, ars[0])
    print(res)

    """
    except Exception as e:
        print(str(e))
        print("Please enter arguments:")
        print("[Fav. technique] [Height] [Gender] [Category]")
        exit()
        """
