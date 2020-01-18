"""
exceptions for game
"""


class GameOver(Exception):
    def __init__(self, objects):
        super().__init__()
        self.player_name = str(objects.player_name)
        self.player_score = str(objects.score)


class EnemyDown(Exception):
    pass
