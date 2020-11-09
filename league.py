# Problem L. Low Effort League
# Source file name: league.c, league.cpp, league.java, league.py
# Input: Standard
# Output: Standard
# The teams in your local rugby league aren’t particularly good, but they make
# up for it in enthusiasm. We are going to organise a single-elimination knockout
# tournament between them, where the 2
# n
# teams play n rounds. In each round, the
# 2i+ 1th remaining team pairs up with the 2i+ 2th team and one or the other team
# is eliminated.
# Team1=1
# Team2=2
# Team3=3
# Team4=4
# Team5=8
# Team6=7
# Team7=6
# Team8=5
# Team1 +1
# 2
# Team3 +1
# 2
# Team6 +12
# Team8 +12
# Team1 +2
# 2
# Team8 +22
# Team1 +42
# Each team has a scalar skill level. In the normal course of things, a team with
# higher skill level will always beat a team with lower skill level. However, training
# plays a part too: if one team studies another, learns its techniques, and trains
# against them, it can win.
# The number of hours a team with skill a must train to beat a team with skill b (where a ≤ b) is |b − a|
# 2
# .
# This training only affects that one game (it does not transfer to other teams).
# You would quite like your favourite team to win the tournament. If you take complete control over how
# every team trains, you can always make this happen. What is the minimum number of hours needed, in
# total across all teams, in order for your team (team 1) to win?
rounds = int(input())
teamLevels = [int(n) for n in input().split()]
hours = 0

for i in range(rounds):
    for j in range(int(len(teamLevels)/2)):
        dif = 0
        result = 0
        if j == 0:
            if teamLevels[0] <= teamLevels[1]:
                dif = teamLevels[1]-teamLevels[0]
                hours += dif*dif
            result = teamLevels[0]
        else:
            if teamLevels[0] <= teamLevels[1]:
                dif = teamLevels[1]-teamLevels[0]
                hours += dif*dif
                result = teamLevels[0]
            else:
                dif = teamLevels[0] - teamLevels[1]
                hours += dif * dif
                result = teamLevels[1]
        teamLevels.pop(0)
        teamLevels.pop(0)
        teamLevels.append(result)
print(hours)