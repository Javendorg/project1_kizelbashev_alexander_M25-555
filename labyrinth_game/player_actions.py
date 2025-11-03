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