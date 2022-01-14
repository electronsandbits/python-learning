"""
dateOFEaster.py
---------------
Easter is celebrated on the Sunday immediately after the first full moon following the
spring equinox. Because its date includes a lunar component, Easter does not have
a fixed date in the Gregorian calendar. Instead, it can occur on any date between
March 22 and April 25. The month and day for Easter can be computed for a given
year using the Anonymous Gregorian Computus algorithm, which is shown below.

Set a equal to the remainder when year is divided by 19
Set b equal to the floor of year divided by 100
Set c equal to the remainder when year is divided by 100
Set d equal to the floor of b divided by 4
Set e equal to the remainder when b is divided by 4

Set f equal to the floor of  b + 8 / 25
Set g equal to the floor of b − f + 1 / 3
Set h equal to the remainder when 19a + b − d − g + 15 is divided by 30
Set i equal to the floor of c divided by 4
Set k equal to the remainder when c is divided by 4
Set l equal to the remainder when 32 + 2e + 2i − h − k is divided by 7
Set m equal to the floor of a + 11h + 22l / 451
Set month equal to the floor of  h + l − 7m + 114 / 31
Set day equal to one plus the remainder when h + l − 7m + 114 is divided by 31

Write a program that implements the Anonymous Gregorian Computus algorithm
to compute the date of Easter. Your program should read the year from the user and
then display a appropriate message that includes the date of Easter in that year.
"""