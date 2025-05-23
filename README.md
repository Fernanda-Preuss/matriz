
# 🔐 Criptografia com Matrizes

Um sistema simples de criptografia e descriptografia usando **álgebra linear** com matrizes e o módulo `numpy`.  
Baseado na ideia do **Hill Cipher**, este projeto transforma texto em números, aplica operações matriciais, e retorna o texto codificado.

---

## 🚀 Funcionalidades

- Criptografa e descriptografa textos usando uma matriz chave
- Sistema de menu simples no terminal
- Suporte a letras, números e pontuação básica
- Compatível com Windows, Linux e MacOS

---

## 📦 Requisitos

- Python 3.10+
- `numpy`

Instale com:

```bash
pip install numpy
```

---

## ⚙️ Como rodar

### 1. Clone ou baixe o projeto

```bash
git clone https://github.com/seu-usuario/criptografia-matriz.git
cd criptografia-matriz
```

### 2. (Opcional) Crie e ative um ambiente virtual

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 3. Rode o script

```bash
python matriz.py
```

---

## 🖥️ Menu do programa

```
=== CRIPTOGRAFIA COM MATRIZES ===
1 - Criptografar
2 - Descriptografar
3 - Sair
```

---

## 🧠 Como funciona?

- Usa uma **matriz 2x2 como chave** para encriptar pares de caracteres.
- Cada caractere é convertido em um número com base em um alfabeto customizado.
- Usa a **inversa modular da matriz** para descriptografar.
- O texto é processado em pares; se o número de caracteres for ímpar, um espaço é adicionado.

---

## 🛠️ Arquivos

- `matriz.py`: script principal com toda a lógica de criptografia.
- Alfabeto suportado:  
  Letras maiúsculas e minúsculas, números, e caracteres: `. , ! ? ; :`

---

## 🔐 Segurança

Esse sistema é **educacional** e não deve ser usado para proteger dados reais.  
Serve como uma ótima introdução à criptografia com Python e matrizes!

---

## 🤝 Contribuição

Sinta-se à vontade para fazer um fork, abrir PRs ou sugerir melhorias.

---

## 📜 Licença

Este projeto é livre para uso e modificação. Sem frescura. Só não vai usar pra coisa errada. 😅

---

## ✍️ Autor

Feito por [Seu Nome Aqui] com 🧠, `numpy` e umas boas ideias.
