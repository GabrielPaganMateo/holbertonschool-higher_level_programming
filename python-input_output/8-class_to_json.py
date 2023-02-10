#!/usr/bin/python3
"""
class_to_json function
"""
import json

def class_to_json(obj):
    """
    Returns the dictionary description with simple
    data structure for JSON serialization of an object
    """
    return json.dumps(obj.__dict__)