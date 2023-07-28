# We are given two inputs, the competitions array 
# and the results array. We need to write a function that returns 
# the winner of the tournament, or more specifically, the name of the 
# team that has the most number of points. The competitions array is an array of pairs, 
# representing all of the competitions in the tournament. Inside of these pairs, 
# we have two strings: the first one is the name of the home team and the second 
# one is the name of the away team. The results array represents the winner of each of these competitions.
# Inside the results array, a 1 means that the home team won and a 0 means the away team won. 
# The results array is the same length as the competitions array, and the indices in the results 
# array correspond with the indices in the competitions array.

def tournamentWinner(competitions, result):
    winning_team = ''
    winner_track = {winning_team :0}
    for competition in range(len(competitions)):
        if competitions[competition][result[competition] - 1] not in winner_track.keys():
            winner_track[competitions[competition][result[competition] - 1]] = 1
        else:
            winner_track[competitions[competition][result[competition] - 1]] +=1
        if winner_track[winning_team] < winner_track[competitions[competition][result[competition] - 1]]:
            winning_team = competitions[competition][result[competition] - 1]
    return winning_team

if __name__ == "__main__":
    competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"],
  ["C#","HTML"]
]
    results = [0, 0, 1, 1]
    print(tournamentWinner(competitions, results))
