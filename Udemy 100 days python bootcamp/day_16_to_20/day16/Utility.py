class question:
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer

import random   
database = [
    {'text': 'A compiler translates code written in a high-level programming language into machine code.', 'answer': True},
    {'text': 'JavaScript is a case-sensitive programming language.', 'answer': True},
    {'text': 'An array is a data structure that stores elements of different data types.', 'answer': False},
    {'text': 'HTTPS is a secure version of HTTP that uses encryption to protect data transmitted over the internet.', 'answer': True},
    {'text': 'An algorithm is a step-by-step procedure for solving a problem.', 'answer': True},
    {'text': 'SQL is a programming language used for managing and manipulating relational databases.', 'answer': True},
    {'text': 'In object-oriented programming, inheritance is the process of creating a new class from an existing class.', 'answer': True},
    {'text': 'The primary purpose of an index in a database is to speed up data retrieval operations.', 'answer': True},
    {'text': 'HTTP stands for Hypertext Transfer Protocol.', 'answer': True},
    {'text': 'DNS stands for Domain Name System.', 'answer': True},
    {'text': 'Java is a purely functional programming language.', 'answer': False},
    {'text': 'Python is a statically typed programming language.', 'answer': False},
    {'text': 'A stack follows the Last-In-First-Out (LIFO) principle.', 'answer': True},
    {'text': 'A linked list is a linear data structure.', 'answer': True},
    {'text': 'A binary search tree guarantees constant-time insertion and deletion operations.', 'answer': False},
    {'text': 'A queue follows the First-In-First-Out (FIFO) principle.', 'answer': True},
    {'text': 'A hash table provides constant-time average case complexity for insertion, deletion, and retrieval operations.', 'answer': True},
    {'text': 'Python supports multiple inheritance.', 'answer': True},
    {'text': 'Python is a compiled language.', 'answer': False},
    {'text': 'Python has static typing.', 'answer': False},
    {'text': 'Python does not support functional programming features.', 'answer': False},
    {'text': 'C supports object-oriented programming.', 'answer': False},
    {'text': 'C programs must have a main() function as the entry point.', 'answer': True},
    {'text': 'C does not provide automatic garbage collection.', 'answer': True},
    {'text': 'SQL is a programming language.', 'answer': False},
    {'text': 'SQL can only be used with relational databases.', 'answer': False},
    {'text': 'The SELECT statement is used to update data in an SQL database.', 'answer': False},
    {'text': 'SQL stands for Structured Query Language.', 'answer': True},
    {'text': 'SQL supports procedural programming constructs.', 'answer': False}
]

questions=[]
questions=random.sample(database,10)

