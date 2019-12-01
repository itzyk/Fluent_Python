# coding=utf-8
import collections
from random import choice
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FranchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades,diamonds,clubs,hearts'.split(',')

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


# 排序函数，rank值乘4加上花色代表的值
def spades_high(card):
    rank_value = FranchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print beer_card

    deck = FranchDeck()
    print len(FranchDeck())

    print deck[0]
    print deck[-1]

    print choice(deck)

    print deck[:3]
    print deck[12::13]

    # 因为实现了__getitem__方法，所以对象deck可迭代，可支持切片
    for item in deck:
        print item

    print Card('Q', 'diamonds') in deck

    for card in sorted(deck, key=spades_high):
        print card
