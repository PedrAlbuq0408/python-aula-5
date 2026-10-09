def gerar_relatorio(validos, invalidos):
    total = len(validos) + len(invalidos)
    taxa = (len(validos) / total * 100) if total else 0

    linhas = []
    linhas.append("=" * 70)
    linhas.append(f"{'RELATÓRIO DE ANÁLISE DE DADOS':^70}")
    linhas.append("=" * 70)

    linhas.append("\n>>> REGISTROS VÁLIDOS")
    linhas.append("-" * 70)
    if validos:
        for reg in validos:
            linhas.append(f"{reg['nome']:<15} | {reg['email']:<28} | {reg['cpf']:<14}")
    else:
        linhas.append("Nenhum registro válido.")

    linhas.append("\n>>> REGISTROS INVÁLIDOS")
    linhas.append("-" * 70)
    if invalidos:
        for numero, nome, motivo in invalidos:
            linhas.append(f"Linha {numero:<3} | {nome:<15} | {motivo}")
    else:
        linhas.append("Nenhum registro inválido.")

    linhas.append("\n>>> ESTATÍSTICAS")
    linhas.append("-" * 70)
    linhas.append(f"Total de registros : {total}")
    linhas.append(f"Válidos            : {len(validos)}")
    linhas.append(f"Inválidos          : {len(invalidos)}")
    linhas.append(f"Taxa de aprovação  : {taxa:.1f}%")
    linhas.append("=" * 70)

    return "\n".join(linhas)