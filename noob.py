import matplotlib.pyplot as plt

scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
games = list(range(1, len(scores)+1))

plt.plot(games, scores, marker='o', label='Scores')
plt.xlabel("Game")
plt.ylabel("Points")
plt.title("Breaking Records Visualization")


plt.legend()
plt.show()
