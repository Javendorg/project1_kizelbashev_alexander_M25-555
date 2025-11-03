import math
from .constants import ROOMS, COMMANDS, EVENT_PROBABILITY, EVENT_COUNT, TRAP_DMG_PROBABILITY, EVENT_DEATH_DMG, EVENT_INTENSIVITY


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
    """
    Позволяет игроку попытаться решить загадку в текущей комнате.
    """
    from .player_actions import get_input

    room = ROOMS[game_state['current_room']]
    if room.get('puzzle') is None:
        print("Загадок здесь нет.")
        return

    question, answer = room['puzzle'][:2]
    print(question)
    user_answer = get_input('Ваш ответ: ').strip().lower()

    # Альтернативные варианты ответа
    from .constants import NUMBERS
    valid_answers = {str(answer).strip().lower()}
    if str(answer) in NUMBERS:
        valid_answers.add(NUMBERS[str(answer)])
    for num, word in NUMBERS.items():
        if word == str(answer).strip().lower():
            valid_answers.add(num)

    if user_answer in valid_answers:
        print('Вы успешно решили загадку!')
        room['puzzle'] = None
        reward = room.get('reward')
        if reward:
            game_state['player_inventory'].append(reward)
    else:
        print('Неверно. Попробуйте снова.')
        if game_state['current_room'] == 'trap_room':
            trigger_trap(game_state)

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

def pseudo_random(seed: int, modulo: int) -> int:
    """
    Генерирует псевдослучайное число на основе входного seed и возвращает его по модулю.
    """
    rand_number = math.sin(seed) * 12.9898 * 43758.5453
    rand_number_final = round((rand_number - math.floor(rand_number)) * modulo)

    return rand_number_final

def trigger_trap(game_state: dict) -> None:
    """
    Активирует ловушку в комнате ловушки.
    """
    print("\nЛовушка активирована! Пол стал дрожать...")

    if len(game_state['player_inventory']) > 0:
        rand_item_index = pseudo_random(seed=game_state['steps_taken'], modulo=len(game_state['player_inventory']))
        deleted_item = game_state['player_inventory'].pop(rand_item_index)
        print(f"Вы чудом успеваете отпрыгнуть, как под вашими ногами осыпается плита. В момент прыжка вы потеряли: {deleted_item}.")
    else:
        rand_damage = pseudo_random(seed=game_state['steps_taken'], modulo=TRAP_DMG_PROBABILITY)
        if rand_damage < EVENT_DEATH_DMG:
            print("Вы не успеваете отпрыгнуть и вместе с плитой падаете в пропасть. Игра окончена.")
            game_state['game_over'] = True
        else:
            print("Вы не успеваете отпрыгнуть, но падаете на мягкую землю внизу. Вам повезло избежать серьезных повреждений.")


def random_event(game_state: dict) -> None:
    rand_event_trigger = pseudo_random(seed=game_state['steps_taken'], modulo=EVENT_PROBABILITY)

    if rand_event_trigger < EVENT_INTENSIVITY:
        rand_event_number = pseudo_random(seed=game_state['steps_taken'], modulo=EVENT_COUNT)

        print("\nСобытие:")

        match rand_event_number:
            case 0:
                print("Громкий дзинь! раздаётся над головой. Посмотрев наверх, вы видите блестящую монету, которая падает вам прямо в руки.")
                game_state['player_inventory'].append('coin')

            case 1:
                print("Вы слышите шорох. Обернувшись, вы видите призрачную фигуру, которая смотрит на вас пустыми глазами.")
                if "sword" in game_state['player_inventory']:
                    print("Вы быстро поднимаете меч и разгоняете призрак светом меча.")
            
            case 2:
                if game_state['current_room'] == "trap_room" and ("torch" not in game_state['player_inventory']):
                    trigger_trap(game_state=game_state)


# Вызов help
def show_help(commands: dict = COMMANDS) -> None:
    """
    Печатает список доступных команд.
    """
    print("\nДоступные команды:")
    for command, description in commands.items():
        print(f"{command:<16}{description}")