class Gamestatus():
    def __init__(self, settings):
        self.game_active = False
        self.score = 0
        self.ship_num = settings.ship_total_num
        self.alien_move_x = True