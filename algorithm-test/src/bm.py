from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    raise Exception("TODO")
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        # self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        assert len(c) == 1
        raise Exception("TODO")
        return -1

    def search(self) -> int:
        m = len(self.pattern)
        n = len(self.text)
        assert m > 0 and n > 0 and n >= m
        
        i = 0
        while i < n - m + 1:
            if self.match_at(i) == -1:
                return i
            i += 1

        return -1
    
    """
    match_at returns -1 if the pattern matches at i.
    Otherwise returns the index in the pattern where the mismatch happens.
    """
    def match_at(self, i) -> int:
        m = len(self.pattern)
        for j in reversed(range(m)):
            if self.text[i + j] != self.pattern[j]:
                return j
        return -1
