class InfitiLineUp:
    def __init__(self, players):
        self.players = players

    def lineup(self):
        lineup_max = len(self.players)
        idx = 0

        while True:
            if idx < lineup_max:
                yield self.players[idx]
            else:
                idx = 0
                yield self.players[idx]

            idx += 1

    def __repr__(self):
        return f'InfiniteLineup({self.players})'

    def __str__(self):
        return f'InfiniteLineUp with the players: {self.players}'


astros = [
    'Springer',
    'Bregman',
    'Altuve',
    'Correa',
    'Reddick'
    'Gonzalez',
    'MacCann'
    'Davis',
    'Tucker'
]

full_lineup = InfitiLineUp(astros)
astros_lineup = full_lineup.lineup()

print(repr(full_lineup))

print(str(full_lineup))


print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
