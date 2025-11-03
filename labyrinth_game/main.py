#!/usr/bin/env python3
# labyrinth_game/main.py
from .constants import ROOMS
from .utils import describe_current_room, attempt_open_treasure, show_help
from .player_actions import get_input, move_player, show_inventory, take_item, use_item

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
        process_command(game_state=game_state, command=user_cmd)
        
def process_command(game_state: dict, command: str) -> None:
    """
    Обрабатывает команду пользователя и обновляет состояние игры.
    """
    parts = command.split(maxsplit=1)
    action = parts[0].lower()
    arg = parts[1].lower() if len(parts) > 1 else None

    directions = {"north", "south", "east", "west"}

    if action in directions and arg is None:
        move_player(game_state, action)
        return

    match action:
        case "look":
            describe_current_room(game_state)

        case "use":
            if arg:
                use_item(game_state, arg)
            else:
                print("Укажите предмет для использования (например: use torch)")

        case "solve":
            current_room = game_state.get('current_room')
            room = ROOMS.get(current_room, {})
            if current_room == 'treasure_room':
                attempt_open_treasure(game_state)
                if game_state.get('game_over'):
                    print('Поздравляем! Вы открыли сундук с сокровищами и победили!')
            elif room.get('puzzle'):
                from .utils import solve_puzzle
                solve_puzzle(game_state)
            else:
                print('Здесь нечего решать.')

        case "go":
            if arg:
                move_player(game_state, arg)
            else:
                print("Укажите направление (например: go north)")

        case "take":
            if arg:
                take_item(game_state, arg)
            else:
                print("Укажите предмет (например: take torch)")

        case "inventory":
            show_inventory(game_state)

        case "quit" | "exit":
            game_state["game_over"] = True

        case "help":
            show_help()

        case _:
            print(f"Неизвестная команда: {action}")

if __name__ == "__main__":
    main()