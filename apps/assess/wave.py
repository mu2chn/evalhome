from .factor import Vec, Score, Factor
from typing import List

class Wave:

    BASESCORE = 100

    def __init__(self):
        self.factors: List[MetaFactor] = []
    
    def appendFactor(self, factor: Factor, weight=1):
        meta = MetaFactor(factor)
        meta.weight = weight
        self.factors.append(meta)
        
    
    def evaluate(self, x: float, y: float) -> List[Score]:
        vec2 = Vec(x, y)
        total_score: List[Score] = []
        for meta in self.factors:
            factor = meta.factor
            weight = meta.weight
            score = factor.evaluate(vec2)
            for reason in score.reasons:
                reason.point *= weight*Wave.BASESCORE
            score.total *= weight*Wave.BASESCORE
            total_score.append(score)
        return total_score

class MetaFactor:
    def __init__(self, factor: Factor):
        self.factor = factor
        self.weight = 1