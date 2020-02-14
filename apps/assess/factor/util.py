from typing import List

class Reason:
    def __init__(self, detail: str, point: float):
        self.point = point
        self.detail = detail

class Score:
    def __init__(self, title: str):
        self.title = title
        self.reasons: List[Reason] = []
        self.total = 0

    # sum of the score should under 1
    def addReason(self, reason: Reason):
        self.total += reason.point
        self.reasons.append(reason)

class Vec:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

