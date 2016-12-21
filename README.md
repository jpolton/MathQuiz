Primary School Games
====================

Two games written in python aimed at my primary school aged child.

Hangman, taking words from a 'dictionary'

Randomised arithmetic questions: X +/- Y for X,Y in specified range where the upper limit is set by the 'level'

To execute:

	python hangman.py

or

	python mathquiz.py

---

You might need to install some modules to get it going. I installed the tabulate module with

	conda install tabulate

---

To do
=====

* The scoring system sucks, especially for hangman
* The scoring recording could happen into a single file per game, or a SQL database
* A number of the files are common to both games and should be abstracted to a separate 'tools' collection.
