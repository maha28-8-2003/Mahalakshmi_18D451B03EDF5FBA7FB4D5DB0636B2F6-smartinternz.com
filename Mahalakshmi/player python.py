class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def increase_score(self, points):
        if points > 0:
            self.score += points
            print(f"{self.name} earned {points} points. Total score: {self.score}")
        else:
            print("Invalid points value. Score not updated.")

    def display_player_info(self):
        print(f"Player: {self.name}, Score: {self.score}")


# Example usage:
# Create players and manipulate scores
player1 = Player("Alice")
player2 = Player("Bob")

player1.increase_score(10)
player2.increase_score(5)

player1.display_player_info()
player2.display_player_info()