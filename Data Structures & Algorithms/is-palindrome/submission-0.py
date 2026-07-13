class Solution:
    def isPalindrome(self, s: str) -> bool:
        listaTexto = [i.lower() for i in s if i.isalpha() or i.isnumeric()]
        listaTextoReverse = [i.lower() for i in reversed(s) if i.isalpha() or i.isnumeric()]
        texto = "".join(listaTexto)
        textoReverse = "".join(listaTextoReverse)

        if texto == textoReverse:
            return True
        else:
            return False
