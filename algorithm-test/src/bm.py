from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    for i in range(len(pattern) - 1):
        table[pattern[i]] = len(pattern) - i - 1
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        assert len(c) == 1
        return self.table.get(c, len(self.pattern))

    def search(self) -> int:
        m = len(self.pattern)
        n = len(self.text)
        i = 0

        while i <= n - m:
            mismatch_idx = self.match_at(i)
            if mismatch_idx == -1:
                return i

            slide_width = self.decide_slide_width(
                self.text[i + mismatch_idx])
            i = i + mismatch_idx + slide_width - (m - 1)

        return -1

    def match_at(self, i) -> int:
        """
        match_at returns -1 if the pattern matches at i.
        Otherwise returns the index in the pattern where the mismatch happens.
        """
        m = len(self.pattern)
        for j in reversed(range(m)):
            if self.text[i + j] != self.pattern[j]:
                return j
        return -1
