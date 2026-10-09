
## Por que validei assim

Usei o módulo regex para conferir o formato de cada campo:

- E-mail: precisa ter texto, um @ e um domínio com final como ".com" ou ".com.br". Por isso "bruno.lima@gmail" é inválido.
- CPF: precisa ter 11 números. Os pontos e o traço são opcionais, então "123.456.789-09" e "12345678909" são aceitos.
- Telefone: aceita fixo e celular, com ou sem DDD, parênteses e hífen.
- Data: precisa estar no formato dd/mm/aaaa. Depois do regex, o Python confere se a data existe de verdade (31/02 não existe).
- Idade: é uma regra extra. A idade calculada precisa ficar entre 0 e 120 anos.

O CPF é validado só pelo formato. Os dígitos verificadores não são calculados.

## Exceções tratadas

- FileNotFoundError: acontece quando o arquivo não existe. O programa avisa e encerra sem travar.
- KeyError: acontece quando falta uma coluna no CSV. O programa mostra qual coluna sumiu.
- ValueError: acontece quando a data não pode ser convertida (ex: 31/02/1990). O registro vai para a lista de inválidos.
- FormatoInvalidoError (criada por mim): acontece quando um campo está no formato errado.
- IdadeInvalidaError (criada por mim): acontece quando a idade está fora de 0 a 120 anos.

## Exemplo de entrada (dados.csv)

csv:
nome,email,cpf,telefone,data_nascimento
Ana Souza,ana.souza@email.com,123.456.789-09,(98) 98765-4321,15/03/1995
Bruno Lima,bruno.lima@gmail,111.222.333-44,98 91234-5678,22/07/1988
Carla Dias,carla_dias@empresa.com.br,12345678909,(11) 3456-7890,01/01/2000
Diego Alves,diego@@email.com,123.456.789-0,(21) 99999-0000,31/02/1990
Elisa Rocha,elisa.rocha@email.com,987.654.321-00,(85) 98888-7777,10/10/2030
Fabio Nunes,fabio.nunes@email.com,321.654.987-91,(98) 3232-4545,05/12/1975


## Exemplo de saída (relatório)

text
[OK] Arquivo 'dados.csv' lido com sucesso.
[INFO] Leitura finalizada.
                    RELATÓRIO DE ANÁLISE DE DADOS                     

REGISTROS VÁLIDOS:

Ana Souza       | ana.souza@email.com          | 123.456.789-09
Carla Dias      | carla_dias@empresa.com.br    | 12345678909   
Fabio Nunes     | fabio.nunes@email.com        | 321.654.987-91

REGISTROS INVÁLIDOS:

Linha 3   | Bruno Lima      | Formato inválido para e-mail: 'bruno.lima@gmail'
Linha 5   | Diego Alves     | Formato inválido para e-mail: 'diego@@email.com'
Linha 6   | Elisa Rocha     | Idade inválida: -5 anos (permitido: 0 a 120)

ESTATÍSTICAS:

Total de registros : 6
Válidos            : 3
Inválidos          : 3
Taxa de aprovação  : 50.0%
