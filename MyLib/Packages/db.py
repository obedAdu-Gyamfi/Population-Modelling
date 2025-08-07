#!/usr/bin/python3
"""
A module used to create my json data file.
This module provides functionality to create a JSON data file with a specified structure.
"""
import json


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
        
        ]
    }
    if not struct:
        struct = myfileStruct
    try:
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
        #if "orgData" in data:
        #    db["orgData"].extend(data["orgData"])
        with open(filename, "wt", encoding="utf-8") as file:
            json.dump(db, file, indent=4)
    except IOError as e:
        print("Unable to write to file!")
    except FileNotFoundError as e:
        print(f"File not found!")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

def create_forecast(struct={}, filename="forecast.json"):
    myfileStruct = {
        "region": [
            
            {
            "id": 0,
            "name": "Ashanti",
            "forecast":
                [
                    {"Verhulst": []},
                    {"Gompertz": []},
                    {"Richard": []}
                ]
            }
        
        ]
    }
    if not struct:
        struct = myfileStruct
    try:
        with open(filename, "wt", encoding="utf-8") as file:
            json.dump(struct, file, indent=4)
    except IOError as e:
        print("Unable to write to file!")
    except FileNotFoundError as e:
        print(f"File not found!")
    except Exception as e:
        print("[{}]{}".format(e.__class__.__name__, e))


def add_forecast(data, filename="forecast.json"):
    try:
        db = read_db(filename)
        if "region" in data:
            db["region"].extend(data["region"])
        
        with open(filename, "wt", encoding="utf-8") as file:
            json.dump(db, file, indent=4)
    except IOError as e:
        print("Unable to write to file!")
    except FileNotFoundError as e:
        print(f"File not found!")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))