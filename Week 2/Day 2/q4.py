class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        idx, result = 0, []
        while idx < len(words):
            temp, ctr = [], 0
            while idx < len(words) and ctr + len(words[idx]) <= maxWidth:
                ctr += len(words[idx]) + 1
                temp.append(words[idx])
                idx += 1
            ctr -= len(temp)
            curr = []
            spaces = maxWidth - ctr
            if idx == len(words):
                result.append(" ".join(temp) + " "*(spaces-len(temp)+1))
                break
            if len(temp)>1:
                remainder = spaces%(len(temp)-1)
                gap = spaces//(len(temp)-1)
                for i in range(len(temp)-1):
                    curr.append(temp[i])
                    curr.append(" "*(gap+min(remainder, 1)))
                    if remainder > 0:
                        remainder -= 1
            curr.append(temp[-1])
            if len(temp) == 1:
                curr.append(" "*spaces)
            result.append("".join(curr))
        return result            