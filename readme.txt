Documentation
=============

Versions:

5/25/2015 : Original submission
5/26/2015 : re-submission after review. Table names and column names were renamed according to standards

Project: 

This is project is Project P2: Tournament Results

This project uses Postgres database and Python. DB access is via DB-API psycopg2 library. The entire environment is a vagrant enviroment running linux

Project contains:

This project assumes that database tournament already exists. Therefore, you need to DROP DATABASE tournament; first in case of any tournament database existed already. Next you need to CREATE DATABASE tournament; and go into the database for creating tables i.e. /c tournament

1. tournament.sql which contains all the scripts required to setup the tables for the tournament. Please note database tournament needs to be created initially using psql

2. tournament.py contains the following functions:

connect(): Connect to the PostgreSQL database.  Returns a database connection.

deleteMatches(): Remove all the match records from the database.

deletePlayers(): Remove all the player records from the database.

countPlayers(): Returns the number of players currently registered."""

registerPlayer(name): Adds a player to the tournament database.
  
playerStandings(): Returns a list of the players and their win records, sorted by wins.

   
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
   
reportMatch(winner, loser): Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
 
swissPairings(): Returns a list of pairs of players for the next round of a match.
  
    
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name


3. tournament_test.py is supplied by Udacity to test the project. If all goes well you should see the following output:

To run use:$ python tournament_test.py

        vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
        1. Old matches can be deleted.
        2. Player records can be deleted.
        3. After deleting, countPlayers() returns zero.
        4. After registering a player, countPlayers() returns 1.
        5. Players can be registered and deleted.
        6. Newly registered players appear in the standings with no matches.
        7. After a match, players have updated standings.
        [(28, 'Fluttershy', 27, 'Twilight Sparkle'), (29, 'Applejack', 30, 'Pinkie Pie')]
        8. After one match, players with one win are paired.
        Success!  All tests pass!



Copyright and licensing information: Under MIT licenings

To Run: Copy the tournament.py and tournament.sql along with the tournament_test.py into the tournament vagrant directory.

first run tournament.sql then tournamanet_test.py

Latest version of github.com/gurugithub
