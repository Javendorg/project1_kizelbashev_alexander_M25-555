# labyrinth_game/constants.py
ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта...',
        'exits': {'north': 'hall', 'east': 'trap_room', 'south': 'gallery'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. По центру стоит пьедестал с запечатанным сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room'},
        'items': [],
        'puzzle': ('На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой или словом.', '10'),
        'reward': 'Rew_Hall'
    },
    'trap_room': {
        'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',
        'exits': {'west': 'entrance', 'south': 'dungeon'},
        'items': ['rusty key'],
        'puzzle': ('Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")', 'шаг шаг шаг'),
        'reward': 'Rew_Trap_Room'
    },
    'library': {
        'description': 'Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.',
        'exits': {'east': 'hall', 'north': 'armory'},
        'items': ['ancient book'],
        'puzzle': ('В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)', 'резонанс'),  # намеренно странная загадка: можно сделать альтернативу
        'reward': 'Rew_Library'
    },
    'armory': {
        'description': 'Старая оружейная комната. На стене висит меч, рядом — небольшая бронзовая шкатулка.',
        'exits': {'south': 'library', 'north': 'barracks'},
        'items': ['sword', 'bronze box'],
        'puzzle': None
    },
    'treasure_room': {
        'description': 'Комната, на столе большой сундук. Дверь заперта — нужен особый ключ.',
        'exits': {'south': 'hall', 'east': 'shrine'},
        'items': ['treasure chest'],
        'puzzle': ('Дверь защищена кодом. Введите код (подсказка: это число пятикратного шага, 2*5= ? )', '10'),
        'reward': 'Rew_Treasure_Room'
    },
    # МОИ КОМНАТЫ
    'gallery': { #1
        'description': 'Просторная галерея с потускневшими картинами и скульптурами. В углу стоит пыльный мольберт, на котором лежит старинный свиток.',
        'exits': {'east': 'dungeon', 'north': 'entrance'},
        'items': ['easel', 'scroll'],
        'puzzle': None
    },
    'dungeon': { #2
        'description': 'Мрачная темница с решетчатыми окнами. В углах видны следы цепей, а на полу разбросаны кости.',
        'exits': {'west': 'gallery', 'north': 'trap_room'},
        'items': ['bones'],
        'puzzle': None
    },
    'shrine': { #3
        'description': 'Тихое святилище с мерцающим алтарем. Воздух наполнен ароматом благовоний, а на стенах — загадочные руны.',
        'exits': {'west': 'treasure_room'},
        'items': [],
        'puzzle': ('На алтаре лежит послание: "Я всегда впереди, но никогда не двигаюсь. Кто я?" (ответ одно слово)', 'будущее'),
        'reward': 'Rew_Shrine'
    },
    'barracks': { #4
        'description': 'Изношенное казарменное помещение с рядами пустых койок. Стены украшены боевыми знаменами и ржавыми оружиями.',
        'exits': {'south': 'armory'},
        'items': ['dagger'],
        'puzzle': ('Найдена надпись: "Я не живу, но расту; у меня нет легких, но мне нужен воздух. Что я?" (ответ одно слово)', 'огонь'),
        'reward': 'Rew_Barracks'
    }
}