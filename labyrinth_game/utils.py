from .constants import ROOMS


def describe_current_room(game_state):
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
