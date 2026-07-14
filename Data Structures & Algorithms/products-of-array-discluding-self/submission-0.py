class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lista = []
        pontadorIndex = 0
        pontadorContas = 0
        conta = 1

        while len(lista) != len(nums):
            if pontadorContas >= len(nums):
                pontadorContas = 0
                pontadorIndex += 1
                lista.append(conta)
                conta = 1
                
            if pontadorContas == pontadorIndex:
                pontadorContas += 1
                if pontadorContas >= len(nums):
                    continue
            
            conta *= nums[pontadorContas]
            
            pontadorContas += 1
        
        return lista


