class Solution:
    def numberToWords(self, num: int) -> str:
        ones = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        tens = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
        anomalies = {0: "Ten", 1: "Eleven", 2: "Twelve", 3: "Thirteen", 4: "Fourteen", 5: "Fifteen", 6: "Sixteen", 7: "Seventeen", 8: "Eighteen", 9: "Nineteen"}
        length = {3: "Billion", 2: "Million", 1: "Thousand", 0: ""}
        arr, temp = [], []   
        numstring = str(num)
        for i in range(len(numstring)-1, -1, -1):
            if len(temp) == 3:
                arr.append("".join(temp[::-1]))
                temp = []
            temp.append(numstring[i])
        arr.append("".join(temp[::-1]))

        if len(arr) == 1 and arr[-1] == '0':
            return "Zero"
        result, single = [], []
        for i in range(len(arr)):
            if len(arr[i]) >= 2:
                if len(arr[i]) == 3:
                    if arr[i][-3] != '0':
                        single.append(ones[int(arr[i][-3])])
                        single.append("Hundred")
                if arr[i][-2] == '1':
                    single.append(anomalies[int(arr[i][-1])])
                else:
                    if arr[i][-2] != '0':
                        single.append(tens[int(arr[i][-2])])
                    if arr[i][-1] != '0':
                        single.append(ones[int(arr[i][-1])])
            if len(arr[i]) == 1:
                single.append(ones[int(arr[-1])])
            if int(arr[i]) != 0:
                single.append(length[i])
                result.append(" ".join(single))
            single = []

        return " ".join(result[::-1]).strip()