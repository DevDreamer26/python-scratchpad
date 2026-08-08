
# Solution to group anagram problem, solved on 13/07/2026 @00:26

strs = ["eat","tea","tan","ate","nat","bat"]

groups = {}

for word in strs:
    signature = "".join(sorted(word))
    if signature in groups:
        groups[signature].append(word)
    else:
        groups[signature]=[word]

print(list(groups.values()))   

