#!/usr/bin/env python3
# labyrinth_game/main.py
from .constants import ROOMS
from .utils import describe_current_room
from .player_actions import get_input

def main():
    game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0 # Количество шагов
    }

    print("\nДобро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state=game_state)

    while not game_state["game_over"]:
        user_cmd = get_input()  # Считываем команду от пользователя
        

if __name__ == "__main__":
    main()