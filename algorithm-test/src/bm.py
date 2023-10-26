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
        if m == 0 or n == 0 or n < m:
            return -1
        
        for i in range(n - m + 1):
            if self.match_at(i):
                return i            

        return -1
    
    def match_at(self, i) -> bool:
        m = len(self.pattern)
        for j in range(m):
            if self.text[i + j] != self.pattern[j]:
                return False            
        return True
