endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500], # /login
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

# FUNÇÃO que verifica se UM código http é sucesso ou não
# 200 --> True
# 401 --> False
def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# FUNÇÃO que verifica se tem 2 erros seguidos
# na lista de requsições (codigo http) de UM endpoint
# [200, 200, 401, 200, 500] --> False -> requisicoes
# [201, 500, 502, 201, 500] --> True
def erros_seguidos(requisicoes):
    for i in range(len(requisicoes) - 1):
        codigo_atual = requisicoes[i]
        prox_codigo = requisicoes[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

# [200, 200, 401, 200, 500] (requisicoes)
# [201, 500, 502, 201, 500]
def analisar_endpoint(requisicoes):
    qtd_sucessos = 0
    for codigo in requisicoes:
        if eh_sucesso(codigo):
            qtd_sucessos += 1

    qtd_total_req = len(requisicoes)
    qtd_erros = qtd_total_req - qtd_sucessos
    percentual_sucesso = (qtd_sucessos / qtd_total_req) * 100

    tem_erros_seguidos = erros_seguidos(requisicoes)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif percentual_sucesso >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return (qtd_sucessos, qtd_erros, percentual_sucesso, classificacao)

# PERCORRENDO TODA A MATRIZ
qtd_maior_erro = -1
endpoint_maior_erro = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    requisicoes_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(requisicoes_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Requisições: {requisicoes_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"% de sucesso: {percentual}")
    print(f"Classificação: {classificacao}")
    print("-" * 30)
    print()

    if erros > qtd_maior_erro:
        qtd_maior_erro = erros
        endpoint_maior_erro = nome_endpoint

print(f"Endpoint + erros: {endpoint_maior_erro} ({qtd_maior_erro})")