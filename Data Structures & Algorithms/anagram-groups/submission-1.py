class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}

        for i in strs:
            palavra = "".join(sorted(i))
            if palavra not in dicts:
                dicts[palavra] = [i]
                continue
            elif palavra in dicts:
                dicts[palavra].append(i)
        
        resultado = [i for i in dicts.values()]

        return resultado

