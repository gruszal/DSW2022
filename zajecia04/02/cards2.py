suits = ['\u2660', '\u2663', '\u2665', '\u2666']
ranks = [str(x) for x in range(2, 11)] + ['J', 'Q', 'K', 'A']

cards = [y + x for x in suits for y in ranks]

print(cards)
