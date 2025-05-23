import numpy as np
import string
import os

class CriptografiaMatriz:
    def __init__(self):
        self.alfabeto = string.ascii_lowercase + string.ascii_uppercase + string.digits + " .,!?;:"
        self.tamanho_alfabeto = len(self.alfabeto)
        self.chave = np.array([[3, 2], [5, 7]], dtype=int)
        self.chave_inversa = self._calcular_inversa_modular()
    
    def _calcular_inversa_modular(self):
        det = int(np.linalg.det(self.chave)) % self.tamanho_alfabeto
        det_inv = self._inverso_modular(det, self.tamanho_alfabeto)
        adj = np.array([[self.chave[1,1], -self.chave[0,1]], [-self.chave[1,0], self.chave[0,0]]], dtype=int)
        inversa = (det_inv * adj) % self.tamanho_alfabeto
        return inversa
    
    def _inverso_modular(self, a, m):
        def euclidiano_estendido(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = euclidiano_estendido(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y
        
        gcd, x, _ = euclidiano_estendido(a % m, m)
        if gcd != 1:
            raise ValueError("Inverso modular não existe")
        return (x % m + m) % m
    
    def _texto_para_numeros(self, texto):
        numeros = []
        for char in texto:
            if char in self.alfabeto:
                numeros.append(self.alfabeto.index(char))
            else:
                numeros.append(self.alfabeto.index(' '))
        return numeros
    
    def _numeros_para_texto(self, numeros):
        texto = ""
        for num in numeros:
            texto += self.alfabeto[num % self.tamanho_alfabeto]
        return texto
    
    def _preparar_texto(self, texto):
        numeros = self._texto_para_numeros(texto)
        if len(numeros) % 2 != 0:
            numeros.append(self.alfabeto.index(' '))
        return numeros
    
    def criptografar(self, texto):
        numeros = self._preparar_texto(texto)
        texto_criptografado = []
        for i in range(0, len(numeros), 2):
            par = np.array([numeros[i], numeros[i+1]])
            par_criptografado = np.dot(self.chave, par) % self.tamanho_alfabeto
            texto_criptografado.extend(par_criptografado)
        return self._numeros_para_texto(texto_criptografado)
    
    def descriptografar(self, texto_criptografado):
        numeros = self._texto_para_numeros(texto_criptografado)
        texto_descriptografado = []
        for i in range(0, len(numeros), 2):
            par = np.array([numeros[i], numeros[i+1]])
            par_original = np.dot(self.chave_inversa, par) % self.tamanho_alfabeto
            texto_descriptografado.extend(par_original)
        return self._numeros_para_texto(texto_descriptografado).rstrip()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

cripto = CriptografiaMatriz()

while True:
    limpar_tela()
    print("=== CRIPTOGRAFIA COM MATRIZES ===")
    print("1 - Criptografar")
    print("2 - Descriptografar")
    print("3 - Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        texto = input("Digite o texto para criptografar: ")
        resultado = cripto.criptografar(texto)
        print(f"Texto criptografado: {resultado}")
        input("\nPressione Enter para continuar...")
        
    elif opcao == "2":
        texto = input("Digite o texto para descriptografar: ")
        resultado = cripto.descriptografar(texto)
        print(f"Texto descriptografado: {resultado}")
        input("\nPressione Enter para continuar...")
        
    elif opcao == "3":
        limpar_tela()
        print("Saindo...")
        break
        
    else:
        print("Opção inválida!")
        input("\nPressione Enter para continuar...")