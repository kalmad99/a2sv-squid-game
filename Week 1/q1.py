class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        prefix, result = [0], float('inf')
        for i in range(len(blocks)):
            if blocks[i] == 'B':
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])
        for i in range(k, len(prefix)):
            result = min(result, k - (prefix[i]-prefix[i-k]))
        return result