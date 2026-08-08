from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for word in strs:
            signature = "".join(sorted(word))
            if signature in groups:
                groups[signature].append(word)
            else:
                groups[signature]=[word]

        return list(groups.values())





# strs = ["eat", "tea", "tan", "nat", "ate", "bat"]


# new_strs = []

# for i in strs:
#     new_strs.append(i)

# print(f"Here is your new string: {new_strs}")    


