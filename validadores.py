import re
from datetime import datetime, date

from excecoes import FormatoInvalidoError, IdadeInvalidaError

# Padrões regex
REGEX_EMAIL = r"^\w+([.\-]\w+)*@\w+([.\-]\w+)*\.[a-zA-Z]{2,}$"
REGEX_CPF = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
REGEX_TELEFONE = r"^(\(?\d{2}\)?\s?)?9?\d{4}-?\d{4}$"
REGEX_DATA = r"^\d{2}/\d{2}/\d{4}$"


def validar_email(valor):
    if not re.match(REGEX_EMAIL, valor):
        raise FormatoInvalidoError("e-mail", valor)
    return valor


def validar_cpf(valor):
    if not re.match(REGEX_CPF, valor):
        raise FormatoInvalidoError("CPF", valor)
    return valor


def validar_telefone(valor):
    if not re.match(REGEX_TELEFONE, valor):
        raise FormatoInvalidoError("telefone", valor)
    return valor


def validar_data(valor):
    """Valida o formato dd/mm/aaaa e se a data realmente existe."""
    if not re.match(REGEX_DATA, valor):
        raise FormatoInvalidoError("data", valor)
    try:
        return datetime.strptime(valor, "%d/%m/%Y").date()
    except ValueError:
        # Passou no regex, mas a data não existe (ex: 31/02/1990)
        raise FormatoInvalidoError("data", valor)


def validar_idade(data_nascimento):
    """Regra de negócio: idade entre 0 e 120 anos."""
    hoje = date.today()
    idade = hoje.year - data_nascimento.year - (
        (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)
    )
    if idade < 0 or idade > 120:
        raise IdadeInvalidaError(idade)
    return idade