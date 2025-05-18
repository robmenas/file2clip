# 📋 file2clip

> Exibe e copia o conteúdo de um arquivo como bloco de código — perfeito para colar em Markdown, issues, comentários ou chats!

## ✨ O que é?

Um script utilitário feito com [Typer](https://typer.tiangolo.com/) para facilitar o compartilhamento de arquivos de texto ou código. Ele:

- Exibe o conteúdo de um arquivo.
- Opcionalmente inclui o nome do arquivo comentado no topo.
- Formata como bloco de código Markdown.
- Copia automaticamente para a área de transferência.

## 🚀 Instalação

### 1. Clonando e rodando direto

```bash
git clone https://github.com/robmenas/file2clip.git
cd file2clip
pip install -r requirements.txt
python main.py arquivo.py
```

### 2. Ou instale como CLI com Typer

```bash
pip install typer[all] clipboard
```

Com `typer`, você pode criar um comando global:

```bash
typer main.py utils file2clip
```

Depois disso, use:

```bash
file2clip script.py
```

## 🛠️ Uso

```bash
python main.py [OPTIONS] FILEPATH
```

### Argumentos

| Nome       | Descrição                               |
| ---------- | --------------------------------------- |
| `filepath` | Caminho para o arquivo a ser processado |

### Opções

| Flag              | Descrição                                                      |
| ----------------- | -------------------------------------------------------------- |
| `--no-filename`   | Não inclui o nome do arquivo como comentário no topo           |
| `--no-clipboard`  | Não copia para a área de transferência                         |
| `--no-markdown`   | Não formata como bloco de código Markdown                      |
| `--language TEXT` | Linguagem para syntax highlight (ex: `python`, `json`, `bash`) |

## 📌 Exemplos

### Copiar `main.py` com formatação Markdown e linguagem Python:

```bash
file2clip main.py --language python
```

Resultado (copiado para a área de transferência e exibido):

````markdown
```python
# main.py
def hello():
    print("Olá, mundo!")
```
````

### Somente exibir, sem copiar:

```bash
file2clip script.py --no-clipboard
```

### Exibir puro, sem nome de arquivo nem markdown:

```bash
file2clip script.py --no-markdown --no-filename
```

## ✅ Requisitos

* Python 3.8 ou superior
* [clipboard](https://pypi.org/project/clipboard/)
* [typer](https://pypi.org/project/typer/) (para uso CLI completo)

Instale via:

```bash
pip install clipboard typer[all]
```

## 📄 Licença

MIT — use, modifique, compartilhe e contribua! 🤘
