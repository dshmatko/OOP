from random import randint
from exceptions import EnemyDown
from exceptions import GameOver
from settings import LIVES


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return int(randint(1, 3))

    def decrease_lives(self):
        self.lives = self.lives - 1
        if self.lives == 0:
            raise EnemyDown()


class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.lives = LIVES
        self.score = 0

    @staticmethod
    def fight(attack, defense):
        res = None
        if attack == defense:
            res = 0
        elif attack == 1 and defense == 3:
            res = -1
        elif attack == 1 and defense == 2:
            res = 1
        elif attack == 2 and defense == 1:
            res = -1
        elif attack == 2 and defense == 3:
            res = 1
        elif attack == 3 and defense == 2:
            res = -1
        elif attack == 3 and defense == 1:
            res = 1
        return res

    def decrease_lives(self):
        self.lives = self.lives - 1
        if self.lives == 0:
            raise GameOver()

    def attack(self, enemy_obj):
        player_choise = input("Attack! Make a choise [1-3] : ")
        enemy_attack = Enemy.select_attack()
        if Player.fight(player_choise, enemy_attack) == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
        elif Player.fight(player_choise, enemy_attack) == -1:
            print("You missed!")
        else:
            print("It's a draw!")

    def defence(self, enemy_obj):
        player_choise = input("Defence! Make a choise [1-3] : ")
        enemy_attack = enemy_obj.select_attack()
        if Player.fight(enemy_attack, player_choise) == 1:
            print("Enemy attacked successfully!")
            self.decrease_lives()
        elif Player.fight(enemy_attack, player_choise) == -1:
            print("Enemy missed!")
        else:
            print("It's a draw!")
