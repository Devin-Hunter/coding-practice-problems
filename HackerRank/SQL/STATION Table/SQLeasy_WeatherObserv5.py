# Query the two cities in STATION with the shortest and longest CITY names, as well as their
# respective lengths (i.e.: number of characters in the name).
#
# If there is more than one smallest or largest city, choose the one that comes first when
# ordered alphabetically.


"""
SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY CHAR_LENGTH(CITY), CITY
LIMIT 1;

SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY CHAR_LENGTH(CITY) DESC, CITY
LIMIT 1;
"""

# Originally I tried to use the MIN/MAX functions using a single query, but those didn't account for
# city names that include spaces for the longest name and it didn't give the correct city name with the
# shortest name.
#
# So instead, I have 2 queries. Each will select all city names, order them in ascending
# or decending order, then order that again by ABC order, then choose the 1st one
