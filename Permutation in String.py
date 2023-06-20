class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_dict = {}
        for i in s1:
            if i not in freq_dict:
                freq_dict[i] = 1
            else:
                freq_dict[i] += 1
        if len(s1) > len(s2):
            return False

        for i in range(len(s2)-len(s1)+1):
            freq_dict2 = {}
            for j in range(i, i+len(s1)):
                if s2[j] not in freq_dict2:
                    freq_dict2[s2[j]] = 1
                else:
                    freq_dict2[s2[j]] += 1
            flag = True
            print(freq_dict, freq_dict2)
            for s in freq_dict2.keys():
                if not freq_dict2.get(s, -1) == freq_dict.get(s, -1):
                    flag = False
                    break
            for s in freq_dict.keys():
                if not freq_dict2.get(s, -1) == freq_dict.get(s, -1):
                    flag = False
                    break
            if flag:
                print(freq_dict2)
                return True
        return False

s1 = "adc"
s2 = "dcda"
print(Solution().checkInclusion(s1,s2))




