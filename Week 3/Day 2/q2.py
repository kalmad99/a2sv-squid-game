class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        ctr, possible = 0, set()
        while ctr <= 31:
            possible.add("".join(sorted(list(str(2**ctr)))))
            ctr += 1
        if "".join(sorted(list(str(n)))) in possible:
            return True
        return False