from .constants import ROOMS
from .utils import attempt_open_treasure

def show_inventory(game_state) -> None:
    """Печатает содержимое инвентаря игрока или сообщение, если он пуст.
    """
    if len(game_state['player_inventory']) > 0:
        print(f"Инвентарь игрока: {game_state['player_inventory']}")
    else:
        print("Инвентарь пуст")

def get_input(prompt="> ") -> str:
    """Считывает ввод пользователя с заданным приглашением и возвращает его в нижнем регистре."""
    try:
        return input(prompt).strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"
    
def move_player(game_state: dict, direction: str) -> None:
    """
        Функция перемещения.
    """
    from .utils import describe_current_room

    current_room = ROOMS[game_state['current_room']]
    exits = current_room.get('exits', {})
    
    if direction in exits:
        game_state['current_room'] = exits[direction]   # Обновляем текущую комнату
        
        game_state['steps'] = game_state.get('steps', 0) + 1    # Увеличиваем шаг

        describe_current_room(game_state)   # Описание новой комнаты
    else:
        print("Нельзя пойти в этом направлении.")
    
def take_item(game_state: dict, item_name: str) -> None:
    """
    Функция взятия предмета
    """
    if item_name == 'treasure_chest':
        print('Вы не можете поднять сундук, он слишком тяжелый.')
    elif item_name in ROOMS[game_state['current_room']]['items']:
        game_state['player_inventory'].append(item_name)
        ROOMS[game_state['current_room']]['items'].remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print(f"Такого предмета здесь нет")

def use_item(game_state: dict, item_name: str) -> None:
    """
    Функция использования предмета из инвентаря игрока
    """
    inventory = game_state.get('player_inventory', [])
    if item_name not in inventory:
        print('У вас нет такого предмета.')
        return

    match item_name:
        case 'torch':
            print('Вы зажгли факел. Вокруг стало светлее!')
        case 'sword':
            print('Вы почувствовали прилив уверенности, держа меч в руках.')
        case 'bronze box':
            if 'rusty_key' not in inventory:
                print('Вы открыли бронзовую шкатулку и нашли ржавый ключ!')
                inventory.append('rusty_key')
            else:
                print('Шкатулка пуста.')
        case 'treasure_key':
            if game_state['current_room'] == 'treasure_room':
                attempt_open_treasure(game_state=game_state)
            else:
                print(f"Нельзя использовать {item_name} в этой комнате.")

        case 'easel':
            print('Вы нашли старый мольбрерт, он сохранился в хорошем состоянии.')
        case 'scroll':
            print('Вы развернули свиток и прочитали древнее послание.')
        case 'bones':
            print('Вы изучили кости и нашли на них древние надписи.')
        case 'dagger':
            print('Вы острили кинжал на камне. Он стал острее.')
        case _:
            print('Вы не знаете, как использовать этот предмет.')
    