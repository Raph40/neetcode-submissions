class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        posicaoValor = 0
        posicaoComparacao = posicaoValor + 1
        outputList = []

        while True:
            tamanhoLista = len(nums)

            if posicaoComparacao == tamanhoLista:
                posicaoValor += 1
                posicaoComparacao = posicaoValor + 1
                continue
            
            valorInicial = nums[posicaoValor]
            valorComparacao = nums[posicaoComparacao]

            if valorInicial + valorComparacao == target:
                outputList.append(posicaoValor)
                outputList.append(posicaoComparacao)
                return outputList
            else:
                posicaoComparacao += 1
