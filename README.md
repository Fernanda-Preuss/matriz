🔐 Criptografia com Matrizes
Sistema de criptografia e descriptografia usando multiplicação matricial em Python.
📋 Descrição
Este programa implementa uma cifra baseada em matrizes matemáticas, onde o texto é convertido em números e criptografado através de operações matriciais modulares. A segurança é baseada na dificuldade de descobrir a matriz chave sem conhecimento prévio.
⚙️ Como Funciona

Conversão: Texto → Números (baseado no alfabeto)
Agrupamento: Números organizados em pares
Criptografia: Multiplicação pela matriz chave 2×2
Operação Modular: Resultado módulo tamanho do alfabeto
Conversão: Números → Texto criptografado

🛠️ Tecnologias

Python 3.x
NumPy - Operações matriciais
OS - Limpeza de tela

🚀 Instalação
bash# Clone ou baixe o arquivo
# Instale o NumPy
pip install numpy

# Execute o programa
python criptografia_matriz.py
💻 Como Usar

Execute o programa
Escolha uma opção no menu:

1 - Criptografar texto
2 - Descriptografar texto
3 - Sair


Digite o texto desejado
Veja o resultado na tela

📊 Exemplo de Uso
Texto original: "Ola mundo!"
Texto criptografado: "X7k#mZ@1"
Texto descriptografado: "Ola mundo!"
🔧 Características Técnicas
Matriz Chave
[3  2]
[5  7]
Alfabeto Suportado

Letras minúsculas (a-z)
Letras maiúsculas (A-Z)
Números (0-9)
Símbolos: espaço, ponto, vírgula, exclamação, interrogação, ponto e vírgula, dois pontos

Segurança

Matriz Invertível: Determinante ≠ 0
Aritmética Modular: Operações mod 68 (tamanho do alfabeto)
Padding Automático: Adiciona espaço se texto tiver comprimento ímpar

🧮 Matemática Por Trás
Criptografia
[c1] = [3  2] × [p1] (mod 68)
[c2]   [5  7]   [p2]
Descriptografia
[p1] = [inv_matrix] × [c1] (mod 68)
[p2]                  [c2]
Onde inv_matrix é a matriz inversa modular da chave.
🔍 Estrutura do Código
CriptografiaMatriz/
├── __init__()                 # Inicializa alfabeto e matrizes
├── _calcular_inversa_modular() # Calcula matriz inversa
├── _inverso_modular()         # Algoritmo euclidiano estendido
├── _texto_para_numeros()      # Converte texto → números
├── _numeros_para_texto()      # Converte números → texto
├── _preparar_texto()          # Adiciona padding se necessário
├── criptografar()             # Função principal de criptografia
└── descriptografar()          # Função principal de descriptografia
⚠️ Limitações

Matriz Fixa: Usa sempre a mesma matriz chave
Alfabeto Limitado: Caracteres não suportados viram espaço
Segurança Básica: Para fins educacionais
Padding Visível: Pode adicionar espaço extra no final

🎓 Uso Educacional
Ideal para aprender sobre:

Álgebra linear aplicada
Criptografia clássica
Aritmética modular
Operações matriciais
Programação em Python

🤝 Melhorias Possíveis

 Matriz chave configurável
 Suporte a matrizes maiores (3×3, 4×4)
 Interface gráfica
 Múltiplos alfabetos
 Análise de frequência
 Testes automatizados

📄 Licença
Código livre para uso educacional e pessoal.

Desenvolvido para fins educacionais - Criptografia com Matrizes 🔐