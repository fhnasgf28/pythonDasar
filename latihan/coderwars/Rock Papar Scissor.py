def rock_paper_scissor(p1, p2):
    # daftar aturan permainan
    rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

    # periksa hasil pertandingan berdasarkan pilihan kedua pemain

    if p1 == p2:
        return 'Draw!'
    elif rules[p1] == p2:
        return 'Player 1 Won!'
    else:
        return 'Player 2 won!'

print(rock_paper_scissor('scissors', 'paper'))
print(rock_paper_scissor('scissors', 'rock'))
print(rock_paper_scissor('paper', 'paper'))

def rps1(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif p1 == 'rock' and p2 == 'scissors':
        return 'Player 1 won!'
    elif p1 == 'scissors' and p2 == 'paper':
        return 'Player 1 won!'
    elif p1 == 'paper' and p2 == 'rock':
        return 'Player 1 won!'
    else:
        return 'Player 2 won'

print(rps1('scissors', 'paper'))
print(rps1('scissors', 'rock'))
print(rps1('paper', 'paper'))