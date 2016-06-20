mazepy
======

Maze classes for Python. Translated from Ruby sources in the book "Mazes for Programmers" by Jamis Buck (https://pragprog.com/book/jbmaze/mazes-for-programmers).

Includes additional code not in the aforementioned book.

Requirements
------------

Python 3.

Install
-------

Install latest version: **pip install mazepy**.

Usage
-----

Use with other programs like this:: 

  from mazepy import mazepy

  grid=mazepy.Grid(10,20)
  grid=mazepy.getRandomMaze(grid)
  print("%s Maze:" % grid.algorithm)
  print(grid)

and output of the above program would be similar to::

  Recursive Backtracker Maze:
  +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  |       |               |                   |               |           |       |
  +   +   +   +---+---+   +   +   +---+---+---+   +---+   +   +   +---+---+   +   +
  |   |   |   |           |   |       |           |       |   |               |   |
  +   +---+   +---+---+---+---+   +   +   +---+---+   +---+   +---+   +---+---+   +
  |       |       |           |   |           |       |   |       |       |       |
  +   +   +---+   +   +   +   +---+---+---+---+   +---+   +---+   +---+---+   +---+
  |   |       |   |   |   |           |           |   |       |           |       |
  +   +---+   +   +   +   +---+---+   +   +---+---+   +   +   +---+---+   +   +   +
  |   |       |   |   |   |       |   |   |           |   |           |   |   |   |
  +   +   +   +   +---+   +---+   +   +   +   +   +---+   +---+---+   +   +   +   +
  |   |   |   |       |   |       |   |   |   |   |       |   |       |   |   |   |
  +   +   +---+---+   +   +   +---+   +   +   +---+   +---+   +   +---+   +---+   +
  |   |           |       |   |       |   |       |           |       |           |
  +   +---+---+   +---+---+   +   +---+   +   +   +---+---+   +---+   +---+---+   +
  |           |       |           |       |   |           |   |   |       |       |
  +---+---+   +---+   +   +---+---+   +---+   +---+---+   +   +   +   +   +   +---+
  |       |   |       |   |           |   |       |       |       |   |   |       |
  +   +---+   +   +---+   +---+---+   +   +---+   +   +---+---+   +   +---+---+   +
  |           |                       |           |               |               |
  +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+

See also: mazingame (https://github.com/samisalkosuo/mazingame)

License
-------

The MIT license for my own code. 

Original Ruby code::
  
  #---
  # Excerpted from "Mazes for Programmers",
  # published by The Pragmatic Bookshelf.
  # Copyrights apply to this code. It may not be used to create training material, 
  # courses, books, articles, and the like. Contact us if you are in doubt.
  # We make no guarantees that this code is fit for any purpose. 
  # Visit http://www.pragmaticprogrammer.com/titles/jbmaze for more book information.
  #--- 