from .constants import ROOMS


def describe_current_room(game_state: dict) -> None:
    """
    Печатает описание текущей комнаты, включая доступные выходы и предметы.
    """
    current_room_key = game_state['current_room']

    current_room_info = ROOMS.get(current_room_key)  # Получаем данные о комнате из константы ROOMS

    print(f"== {current_room_key.upper()} ==")  # Выводим название комнаты
    
    print(current_room_info['description'])  # Описание комнаты
    
    # Список предметов
    if current_room_info.get('items'):
        print("Заметные предметы:", ", ".join(current_room_info['items']))
    
    print("Выходы:", ", ".join(current_room_info.get('exits', [])))  # Доступные выходы
    
    # Проверка на загадку
    if current_room_info.get('puzzle'):
        print("Кажется, здесь есть загадка (используйте команду solve).")
    else:
        print("Загадок здесь нет.")

#Функция решения загадки
def solve_puzzle(game_state: dict) -> None:
    from .player_actions import get_input
    room = ROOMS[game_state['current_room']]
    if room.get('puzzle') is None:
        print("Загадок здесь нет.")
        return
    question, answer = room['puzzle'][:2]
    print(question)
    user_answer = get_input('Ваш ответ: ')
    if user_answer == answer:
        print('Вы успешно решили загадку!')
        room['puzzle'] = None
        reward = room.get('reward')
        if reward:
            game_state['player_inventory'].append(reward)
    else:
        print('Неверно. Попробуйте снова.')

def attempt_open_treasure(game_state: dict) -> None:
    """
    Попытка открыть сундук в комнате сокровищ.
    """
    if "treasure_key" in game_state['player_inventory']:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        ROOMS[game_state['current_room']]['items'].remove('treasure_chest')
        print(f"В сундуке сокровище! Вы победили за {game_state['steps_taken']} шагов!")
        game_state['game_over'] = True
    else:
        users_answer = input("Сундук заперт. ... Ввести код? (да/нет) ")
    
        if users_answer.lower() == "да":
            users_code = input("Введние код: ")
      
            if users_code == ROOMS[game_state['current_room']]['puzzle'][1]:
                print("Вы правильно вводите код, и замок щёлкает. Сундук открыт!")
                print(f"В сундуке сокровище! Вы победили за {game_state['steps_taken']} шагов!")
                game_state['game_over'] = True
      
            else:
                print("Вы ввели неверный код, попробуйте еще раз.")
        
        else:
            print("Вы отступаете от сундука.")


# labyrinth_game/utils.py
def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")