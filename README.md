![GitHub](https://img.shields.io/github/license/hunar4321/life_code)

# Trolley-Problem-Solver
This was my first attempt to dabble in machine learning. Code is not clean whatsoever. I pumped it out as fast possible to make sure I understand how ML works and no more. The project consists of a script to generate trolley problems and a script to solve them "humanely". Everything is written in Python.

To use just download all the files, put them in one folder, install all the python libraries used, and then run ```TrolleyProblemSolver.py``` or ```TrolleyProblemGenerator.py``` depending on what you want.

Trolley Problem Solver
------------------------

This is a random forest algorithm I fed a little data to *in theory* make it solve trolley problems like a human. The data used to train it has been made from the generator script and then labeled by myself and some friends. 61 samples is almost definitely not enough for the algorithm to perform well, but it was good enough to prove that it works alright. Feel free to add more samples and mess around with the code to make it better.

Trolley Problem Generator
--------------------------
This script generates X number of random trolley problems. I made this to create data for the solver algorithm project. You can edit values in the script directly to customize what sorts of problems you want, however, if you trust my settings are good enough you can run the script from the console like this:
```
python TrolleyProblemGenerator.py [number of samples]
```
This creates a .csv file in the same folder you had the script in. This file can be opened in google sheets, notepad, whatever can read .csv

This was fun to work on. Do what you want with the code, but credit would be much appreciated. Contact info in the profile.
----------

 
