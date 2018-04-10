import random


class SpyBot(object):

    def __init__(self, vocab, game_board, p_id):
        pass

    def update(self, is_my_turn, clue_word, clue_num_guesses, guesses):
        pass

    def getClue(self, invalid_words):
        pass


# example of how to write a bot
class RandomBot(SpyBot):

    def __init__(self, vocab, game_board, p_id):
        self.vocab = set(vocab)

    def getClue(self, invalid_words):
        return random.choice(list(self.vocab.difference(invalid_words))), 2

