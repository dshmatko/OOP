"""
runner for game
"""
from exceptions import EnemyDown
from exceptions import GameOver
from models import Enemy
from models import Player


def play():
    """
    method play
    """
    player_name = input("Please, enter your name : ")
    player = Player(player_name)
    level = 1
    enemy = Enemy(1)

    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown:
            level += 1
            player.score += 5
            enemy = Enemy(level)


def main():
    """
    method main
    """
    try:
        play()
    except GameOver as game_over:
        print("YouLose")
        score_file = open('scores.txt', 'a')
        score_file.write(game_over.player_name, game_over.player_score + '\n')
        score_file.close
    except KeyboardInterrupt:
        pass
    finally:
        print("GoodBye!")


if __name__ == "__main__":
    main()
