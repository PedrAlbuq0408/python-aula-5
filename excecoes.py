class FormatoInvalidoError(Exception):
    """Lançada quando um campo não segue o formato esperado."""

    def __init__(self, campo, valor):
        self.campo = campo
        self.valor = valor
        super().__init__(f"Formato inválido para {campo}: '{valor}'")


class IdadeInvalidaError(Exception):
    """Lançada quando a idade calculada foge da regra de negócio."""

    def __init__(self, idade):
        self.idade = idade
        super().__init__(f"Idade inválida: {idade} anos (permitido: 0 a 120)")