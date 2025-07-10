#!/usr/bin/python3
"""
A module used to create my json data file.
This module provides functionality to create a JSON data file with a specified structure.
"""
import json
import os

def create_db(struct={}, filename="data.json"):
    myfileStruct = {
        "region": [
            
            {
            "id": 0,
            "name": "Ashanti",
            "model":
                [
                    {"Verhulst": []},
                    {"Gompertz": []},
                    {"Richard": []}
                ], 
            "parameters":
                [
                {"verhulst": {}},
                {"gompertz": {}},
                {"richard": {}}
                ],
            "Errors":
            [
                    {"verhulst": {}},
                    {"gompertz": {}},
                    {"richard": {}}
            ]
            }
        
        ],
        "orgData":
            {"year": [1960,1970, 1984, 2000, 2010],
             "population": []
             }
    }
    if not struct:
        struct = myfileStruct
    try:
        #if os.path.exists(filename):
        #    print(f"File {filename} already exists. Please choose a different name or delete the existing file.")
        #    exit(1)
        #else:
        with open(filename, "wt", encoding="utf-8") as file:
            json.dump(struct, file, indent=4)
    except IOError as e:
        print("Unable to write to file!")
    except FileNotFoundError as e:
        print(f"File not found!")
    except Exception as e:
        print("[{}]{}".format(e.__class__.__name__, e))
        

def read_db(filename="data.json"):
    try:
        with open(filename, "rt", encoding="utf-8") as file:
           return json.load(file)
    except IOError as e:
        print("Unable to read file!")
    except FileNotFoundError as e:
        print(f"File not found!")
    except Exception as e:
        print("[{}]{}".format(e.__class__.__name__, e))

def add_to_db(data, filename="data.json"):
    try:
        db = read_db(filename)
        if "region" in data:
            db["region"].extend(data["region"])
        if "orgData" in data:
            db["orgData"] = data["orgData"]
        with open(filename, "wt", encoding="utf-8") as file:
            json.dump(db, file, indent=4)
    except IOError as e:
        print("Unable to write to file!")
    except FileNotFoundError as e:
        print(f"File not found!")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

