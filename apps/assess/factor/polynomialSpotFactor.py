from . import Factor, Vec, Score, Reason
from typing import List

class EachSpot:
    def __init__(self, name: str, vec2: Vec, pri):
        self.name = name
        self.vec2 = vec2
        self.pri = pri

class PolynomialSpotFactor(Factor):

    def __init__(self, title, grad=1, n=1):
        self.eachSpotList: List[EachSpot] = []
        self.title = title
        self.grad = grad
        self.n = n

    def appendData(self, name: str, x: float, y: float, pri=1.0):
        self.eachSpotList.append(EachSpot(name, Vec(x, y), pri))
    
    def evaluate(self, vec2: Vec) -> Score:
        score = Score(self.title)
        for spot in self.eachSpotList:
            deltaX = abs(spot.vec2.x-vec2.x)
            deltaY = abs(spot.vec2.y-vec2.y)
            length = deltaX + deltaY
            if 1 >= length > 0:
                point = 1 - length
            else:
                point = 0
            reason = Reason(spot.name, point*spot.pri)
            score.addReason(reason)

        return score

