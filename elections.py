"""
Given an array of the numbers of votes given to each of the candidates so far,
and an integer k equal to the number of voters who haven't cast their vote yet,
find the number of candidates who still have a chance to win the election.
The winner of the election must secure strictly more votes than any other candidate.
If two or more candidates receive the same(maximum) number of votes,
assume there is no winner at all.

Example
For votes = [2, 3, 5, 2] and k = 3, the output should be 2
"""

"""
# мое решение

def elections_winners(votes, k):
    current_winner = max(votes)
    if k == 0 and current_winner == sum(votes)/len(votes):
        return 0
    if votes.count(current_winner) > 1 and k == 0:
        return 0
    if k == 0:
        k = 1
    have_chance_to_win = 0
    for vote in votes:
        if vote + k > current_winner:
            have_chance_to_win += 1
    return have_chance_to_win
"""

def elections_winners(votes, k):
    """
    best practices
    """
    m = max(votes)
    return sum(x + k > m for x in votes) or votes.count(m) == 1

print(elections_winners([2, 3, 5, 2], 3))
print(elections_winners([5, 1, 3, 4, 1], 0))
print(elections_winners([1, 3, 3, 1, 1], 0))
print(elections_winners([1, 1, 1, 1], 1))
print(elections_winners([3, 1, 1, 3, 1], 2))
