class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts = {}

        for i in nums:
            if i not in dicts:
                dicts[i] = 1
                continue
            elif i in dicts:
                dicts[i] += 1
        
        
        lista = dict(sorted(dicts.items(), key=lambda x: x[1], reverse=True))

        resultado = [i for i in lista.keys()][:k]

        return resultado