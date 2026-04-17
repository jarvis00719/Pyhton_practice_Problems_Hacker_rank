import matplotlib.pyplot as plt

def breaking_records(score):

    for i,s in enumerate(score):

        return




#Input Statements!!
no_of_games = int(input())
scores = list(map(int, input().split()))




##Score Visulaization!!
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
games = list(range(1, len(scores)+1))

plt.plot(games, scores, marker='o', label='Scores')
plt.xlabel("Game")
plt.ylabel("Points")
plt.title("Breaking Records Visualization")

plt.legend()
plt.show()
