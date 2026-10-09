import csv
import sys

from excecoes import FormatoInvalidoError, IdadeInvalidaError
from validadores import (
    validar_email,
    validar_cpf,
    validar_telefone,
    validar_data,
    validar_idade,
)
from relatorio import gerar_relatorio

COLUNAS_OBRIGATORIAS = ["nome", "email", "cpf", "telefone", "data_nascimento"]


def validar_registro(linha):
    """Valida todos os campos de uma linha. Lança exceção se algo estiver errado."""
    validar_email(linha["email"] or "")
    validar_cpf(linha["cpf"] or "")
    validar_telefone(linha["telefone"] or "")
    data = validar_data(linha["data_nascimento"] or "")
    validar_idade(data)


def processar_arquivo(caminho):
    validos = []
    invalidos = []
    arquivo = None

    try:
        arquivo = open(caminho, encoding="utf-8", newline="")
        leitor = csv.DictReader(arquivo)

        faltando = [c for c in COLUNAS_OBRIGATORIAS if c not in (leitor.fieldnames or [])]
        if faltando:
            raise KeyError(f"Coluna(s) ausente(s) no CSV: {', '.join(faltando)}")

        for numero, linha in enumerate(leitor, start=2):  # linha 1 é o cabeçalho
            try:
                validar_registro(linha)
            except (FormatoInvalidoError, IdadeInvalidaError) as erro:
                invalidos.append((numero, linha["nome"], str(erro)))
            else:
                validos.append(linha)

    except FileNotFoundError:
        print(f"[ERRO] Arquivo '{caminho}' não encontrado.")
        return None
    except KeyError as erro:
        print(f"[ERRO] {erro.args[0]}")
        return None
    except ValueError as erro:
        print(f"[ERRO] Valor inválido ao converter dados: {erro}")
        return None
    else:
        print(f"[OK] Arquivo '{caminho}' lido com sucesso.")
    finally:
        if arquivo:
            arquivo.close()
        print("[INFO] Leitura finalizada.\n")

    return validos, invalidos


def main():
    caminho = sys.argv[1] if len(sys.argv) > 1 else "dados.csv"

    resultado = processar_arquivo(caminho)
    if resultado is None:
        return

    validos, invalidos = resultado
    print(gerar_relatorio(validos, invalidos))


if __name__ == "__main__":
    main()