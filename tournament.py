#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
#v1 Guru Shetti 5/25/15 Original submission
#v2 Guru Shetti 5/26/15 Assessment feedback on Code Quality and Documentation

# import psycopg2 for db-api for postgres
import psycopg2
# import bleach for sql injection detection and clean
import bleach


#v2 Function to connect to DB for operations
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try: 
        conn = psycopg2.connect("dbname=tournament")
        return conn
    except psycopg2.Error as e:
      print e



def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute( "DELETE FROM matches")
    DB.commit()
    DB.close()
# closing DB

def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute( "DELETE FROM players")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect() 
    cursor = DB.cursor()
    cursor.execute( "SELECT COUNT(*) as num FROM players")
    row = cursor.fetchone()
    
    DB.close()

    return row[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect() 
    cursor = DB.cursor()
    cursor.execute( "INSERT INTO players (player_name) VALUES (%s)", (bleach.clean(name),))
    DB.commit()
    DB.close()
    


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    cursor = DB.cursor()
    cursor.execute(" SELECT players.player_id, players.player_name, SUM(players.player_wins) AS wins, COUNT(matches.player_id) AS played FROM players LEFT OUTER JOIN  matches ON players.player_id = matches.player_id  GROUP BY players.player_id ORDER BY wins ;")
    
    rows = cursor.fetchall()
#    for i, row in enumerate(rows):
#       print "Row", i, "value = ", row[0]
# Uncomment above lines if you want to debug
    DB.close()
# returns the set with players with ost wins at the top
    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    
    DB = connect() 
    cursor = DB.cursor()
# inserting winner    
    cursor.execute( "INSERT INTO matches (tournament_id, player_id, player_standings) VALUES (1, %s, 'won')", (bleach.clean(winner), ))
# for the sake of the this project we are hardcodng the value of tournamanet_id as 1. This can be extended for additional tournaments    
# insert losing player
    cursor.execute( "INSERT INTO matches (tournament_id, player_id, player_standings) VALUES (1, %s, 'lost')", (bleach.clean(loser), ))
# Also updating the number of wins for the winner. This makes the program more efficient by denormalizing.    
    cursor.execute( "UPDATE players SET player_wins = player_wins + 1 WHERE player_id = (%s) ", (winner,))
# commiting all the changes    
    DB.commit()
    DB.close()
    
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    DB = connect()
    cursor = DB.cursor()
    cursor.execute(" SELECT player_id, player_name FROM players ORDER BY player_wins DESC")
# initializing an empty tuple list    
    results = []
# get all the rows. Assumes only even number of players    
    rows = cursor.fetchall()
    if len(rows) % 2 == 0:
# initializing id and names for the tuple. This will fail is there are odd number of players. Unfortunately no time to make it bullet proof    
        id1 = 0
        name1 = ""
        id2 = 0
        name2 = ""
# iterate over the rows (only even for now)
        for i, row in enumerate(rows):
        
# iteration starts with 0. So modulo 2 will set the first tuple in pair      
            if (i % 2) == 0:
                id1 = (row[0])
                name1 = (row[1])

# iteration starts with 0. So modulo 2 if not 0 will set the second tuple in pair. Quick and dirty solution         
            if (i % 2) != 0:
                id2 = (row[0])
                name2 = (row[1])
                result = id1, name1, id2, name2

                results.append(result)
    else:
        print "Players are not even. Unsupported functionality. Contact support"
                      
    DB.close()

    
    return results
