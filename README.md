# 🖥️ Simulador Bash Web

Um simulador de terminal Bash funcional e interativo via navegador, construído com **HTML**, **CSS**, **JavaScript** e **Python (Flask)**. Permite simular comandos básicos do terminal como `mkdir`, `touch`, `ls`, entre outros.

---

## 🚀 Demonstração

![Preview do Terminal](https://i.imgur.com/frWGd77.png)

---

## 📁 Estrutura do Projeto

```
.
├── /cli
  ├── main.py         # Backend do projeto em Python sem GUI
├── index.html        # Interface do terminal web
├── style.css         # Estilização do terminal e layout
├── script.js         # Lógica de interação e comandos no frontend
├── main.py           # Backend em Flask que processa os comandos
└── README.md         # Documentação do projeto
```

---

## ⚙️ Comandos Suportados

| Comando        | Descrição                                      |
|----------------|------------------------------------------------|
| `mkdir nome`   | Cria um diretório com o nome fornecido         |
| `touch nome`   | Cria um arquivo com o nome fornecido           |
| `ls`           | Lista os arquivos e pastas no diretório atual  |
| `pwd`          | Mostra o caminho do diretório atual            |
| `clear`        | Limpa a tela do terminal (frontend)            |
| `exit` / `quit`| Simula a saída do terminal                     |

---

## 📦 Tecnologias Utilizadas

- **Frontend**:
  - HTML5
  - CSS3 
  - JavaScript 

- **Backend**:
  - Python 3.x
  - Flask 

---

## 🧑‍💻 Como Rodar o Projeto Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/simulador-bash.git
cd simulador-bash
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

### 3. Instale as dependências

```bash
pip install flask flask-cors
```

### 4. Execute o servidor

```bash
python main.py
```

Acesse `http://localhost:5000` no navegador.

---

## 🧠 Observações Técnicas

- Todos os comandos são simulados localmente, sem interação com o sistema real.
- O terminal ignora letras maiúsculas nos comandos (`mkdir`, `MKDIR`, etc. funcionam igual).

---

## 👨‍👩‍👧‍👦 Autores

Projeto desenvolvido nada mais nada menos que os melhores da turma de Redes de Computadores:

- Deyse Cristina  
- Evandro Endi  
- Ilídio Júnior  
- Vinícius Augusto  

---
