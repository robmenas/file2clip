"""
Script utilitário para exibir e copiar o conteúdo de um arquivo de texto.

Funcionalidades:
- Exibe o conteúdo de um arquivo especificado.
- Comenta o nome do arquivo no topo do conteúdo (opcional).
- Formata o conteúdo como bloco de código Markdown (opcional).
- Copia o conteúdo para a área de transferência (opcional).

Uso típico:
    python main.py caminho/para/arquivo.py
Ou, usando o comando específico, caso instalado:
    file2clip caminho/para/arquivo.py

Argumentos:
- filepath: Caminho para o arquivo cujo conteúdo será exibido/copiado.

Opções:
- --no-filename: Não inclui o nome do arquivo como comentário no topo.
- --no-clipboard: Não copia o conteúdo para a área de transferência.
- --no-markdown: Não formata como bloco de código Markdown.
- --language TEXT: Define a linguagem do bloco Markdown (requer --markdown).

Exemplos:
    # Copia o conteúdo de script.py como bloco de código Python no formato Markdown
    file2clip script.py --language python

    # Apenas exibe o conteúdo do arquivo sem copiar para a área de transferência
    file2clip script.py --no-clipboard
"""

from pathlib import Path

import clipboard as cb
import typer


def cli(
    filepath: Path = typer.Argument(
        ..., help="File do get content", exists=True, show_default=False
    ),
    filename: bool = typer.Option(
        True, help="Filename commented in top text. Ex.: # main.py"
    ),
    clipboard: bool = typer.Option(True, help="copy to clipboard"),
    markdown: bool = typer.Option(True, help="copy in markdown syntax"),
    language: str | None = typer.Option(None, help="language to markdown label"),
):
    """
    Exibe o conteúdo de um arquivo com opções para copiar, formatar como Markdown e incluir o nome do arquivo.

    - O conteúdo pode ser formatado como um bloco de código Markdown.
    - Pode incluir o nome do arquivo como comentário no topo.
    - Pode ser copiado automaticamente para a área de transferência.
    """

    if language and not markdown:
        typer.Exit("language must be used with markdown")

    text = filepath.read_text().strip()
    if filename:
        text = f"# {filepath.relative_to('.')}\n{text}"
    language = "" if not language else language
    text = text if not markdown else f"```{language}\n{text}\n```"
    typer.echo(text)

    if clipboard:
        cb.copy(text)


def main():
    typer.run(cli)


if __name__ == "__main__":
    main()
