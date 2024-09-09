## Desafio de Programação

### Desafio 1: Cálculo da Soma

**Enunciado:**
Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?

**Solução:**

indice = 13
soma = 0
k = 0
for k in range(1, indice+1):
    soma += k
print(soma)


### Desafio 2: Sequência de Fibonacci

**Enunciado:**
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

**Solução:**

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    return b == n

"""True fibonacci sequence"""
testing = fibonacci(13)
"""False fibonacci sequence"""
testing2 = fibonacci(14)

print(testing)
print(testing2)

### Desafio 3: Calcular faturamento

**Enunciado:**
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:

a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

**Solução:**

def calcFaturamento(faturamento: str):
    with open(faturamento, "r") as teste:
        dados = json.load(teste)
    faturamento_diario = []
    for chave, valor in dados.items():
        if isinstance(valor, list):
            faturamento_diario.extend(valor)

    menor = min(faturamento_diario)
    maior = max(faturamento_diario)
    media = round(sum(faturamento_diario) / len(faturamento_diario), 2)
    dias_acima_media = sum(valor > media for valor in faturamento_diario)


    return f"menor: {menor}, maior: {maior}, media: {media} e dias acima da média: {dias_acima_media}"

print(calcFaturamento("faturamento.json"))

### Desafio 4: Calcular faturamento por estado

**Enunciado:**
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

**Solução:**


def calc_faturamento(faturamento: dict):
    total = sum(faturamento.values())
    percentual = {estado: round((valor / total) * 100, 2) for estado,valor in faturamento.items()}
    return percentual

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

print(calc_faturamento(faturamento))
```markdown
### Desafio 5: Inverter String

**Enunciado:**
Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

**Solução:**
def inverte_no_dedo(string:str):
    aux = ""
    p = 1
    k = 0
    """
    0(k) + 1(p) = 1 | len(string) - 1 = 5
    1(k) + 1(p) = 2 | len(string) - 2 = 4
    2(k) + 1(p) = 3 | len(string) - 3 = 3

    """
    for i in range(len(string)):
        k += p
        temp = len(string) - k
        aux += string[temp]
        p = 1

    return aux

print(inverte_string("string"))
print(inverte_no_dedo("string"))

## Observações

- **Linguagem:** Os códigos foram implementados em Python.

## Autor

Márcio Paulo de Almeida Lima
marciopaulolima21@edu.unifor.br

## Data

09/09/24

