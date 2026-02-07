import random
import time

class RussianRouletteGame:
    def __init__(self, player1, player2, time_limit=5):
        self.players = [player1, player2]
        self.current_player = 0
        self.time_limit = time_limit

        self.chambers = [0, 0, 0, 0, 0, 1]
        random.shuffle(self.chambers)

        self.current_index = 0
        self.is_game_over = False
        self.last_move_time = time.time()
        self.loser = None

    def shoot(self):
        if self.is_game_over:
            return "Игра уже окончена"

        # проверка времени
        if time.time() - self.last_move_time > self.time_limit:
            self.loser = self.players[self.current_player]
            self.is_game_over = True
            return f"⏰ {self.loser} не успел нажать кнопку!"

        result = self.chambers[self.current_index]
        self.current_index += 1
        self.last_move_time = time.time()

        if result == 1:
            self.loser = self.players[self.current_player]
            self.is_game_over = True
            return f"💥 BOOM! {self.loser} получил пулю!"

        self.current_player = 1 - self.current_player
        return f"🔫 click… Ход переходит к {self.players[self.current_player]}"

    def stop(self):
        self.loser = self.players[self.current_player]
        self.is_game_over = True

    def get_result(self):
        winner = self.players[1 - self.players.index(self.loser)]
        return (
            "🏁 ИГРА ОКОНЧЕНА\n\n"
            f"❌ Проиграл: {self.loser}\n"
            f"🏆 Победил: {winner}"
        )
