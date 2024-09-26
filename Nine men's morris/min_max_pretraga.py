from hashmap import HashMap
from stanje import Stanje


class Min_max_pretraga(object):

    def __init__(self):
        self.mapaVecPronadjenih = HashMap(100)

    def maxScore(self, state, depth, alfa, beta, faza):
        if state.da_li_je_kraj_igre():
            if faza=="Faza1":
                return state.heuristika()
            else:
                return state.heuristika_faza2()

        if depth <= 0:
            if faza=="Faza1":
                return state.heuristika()
            else:
                return state.heuristika_faza2()

        next_states = state.next_states('C', self.mapaVecPronadjenih, faza)
        for sledeceStanje in next_states:
            score = self.minScore(sledeceStanje, depth - 1, alfa, beta, faza)
            alfa = max(alfa, score)
            if alfa >= beta:
                return beta
        return alfa

    def minScore(self, state, depth, alpha, beta, faza):
        if state.da_li_je_kraj_igre():
            if faza=="Faza1":
                return state.heuristika()
            else:
                return state.heuristika_faza2()

        if depth <= 0:
            if faza=="Faza1":
                return state.heuristika()
            else:
                return state.heuristika_faza2()

        next_states = state.next_states('B', self.mapaVecPronadjenih, faza)

        for sledeceStanje in next_states:
            score = self.maxScore(sledeceStanje, depth - 1, alpha, beta, faza)
            beta = min(beta, score)
            if alpha >= beta:
                return alpha
        return beta

    def next_move(self, state, depth, faza):

        bestMove = None
        alpha = -1000000
        next_states = state.next_states('C', self.mapaVecPronadjenih, faza)

        if next_states is None:
            print("nema dalje stanja")
        if len(next_states) == 0:
            print('prazna lista')

        for sledeceStanje in next_states:
            result = self.minScore(sledeceStanje, depth - 1, alpha, 1000000, faza)
            if result > alpha:
                alpha = result
                bestMove = sledeceStanje  # next - state.move()
            if alpha >= 1000000:
                break
        if bestMove is None:
            print('end fgame')
            return None
        return bestMove

