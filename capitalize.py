#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the solve function below.
s = input()
MyList = s.split(' ')
MyList = [word.capitalize() for word in MyList]
print( ' '.join(MyList))  # Join the list into a single string separated by spaces

"""
Task:
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan"""
    

