import csv
import datetime
import matplotlib.pyplot as plt

ARQUIVO = "Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv"

COLUNAS = ['data', 'precip', 'maxima', 'minima', 'temp_media']


# função para carregar e tratar os dados

def carregar_dados(nome_arquivo):
    dados = []

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            leitor = csv.reader(f)
            next(leitor)  # ignora o cabeçalho

            for linha in leitor:
                if len(linha) < 6:
                    continue  # pula linhas incompletas

                data_str = linha[0].strip()

                try:
                    dia, mes, ano = map(int, data_str.split("/"))
                except:
                    continue  # pula datas inválidas

                registro = {
                    "data": data_str,
                    "mes": mes,
                    "ano": ano,
                    "precip": converter_float(linha[1]),
                    "maxima": converter_float(linha[2]),
                    "minima": converter_float(linha[3]),
                    "temp_media": converter_float(linha[5])
                }

                dados.append(registro)

        print(f"Arquivo carregado com sucesso! {len(dados)} registros lidos.\n")
        return dados

    except FileNotFoundError:
        print(f"ERRO: Arquivo '{nome_arquivo}' não encontrado.")
        return []


def converter_float(valor):
    try:
        return float(valor)
    except:
        return None


# Visualização textual dos dados
def validar_mes_ano():
    while True:
        try:
            mes = int(input("Digite o mês (1-12): "))
            ano = int(input("Digite o ano (YYYY): "))
            datetime.date(ano, mes, 1)
            return mes, ano
        except:
            print("Data inválida. Tente novamente.\n")


def visualizar_intervalo(dados):
    print("\n--- VISUALIZAÇÃO DE INTERVALO ---")
    print("Informe período inicial:")
    imes, iano = validar_mes_ano()

    print("\nInforme período final:")
    fmes, fano = validar_mes_ano()

    if (iano, imes) > (fano, fmes):
        print("ERRO: período inicial maior que o final.")
        return

    print("\nEscolha os dados que deseja visualizar:")
    print("1 - Todos")
    print("2 - Somente precipitação")
    print("3 - Somente temperaturas (máx / mín / média)")
    opcao = input("Opção: ")

    print("\nRESULTADOS:")


    for reg in dados:
        if (reg["ano"], reg["mes"]) < (iano, imes): continue
        if (reg["ano"], reg["mes"]) > (fano, fmes): continue

        if opcao == "1":
            print(f"{reg['data']} | Prec: {reg['precip']} | Max: {reg['maxima']} | "
                  f"Min: {reg['minima']} | Med: {reg['temp_media']}")

        elif opcao == "2":
            print(f"{reg['data']} | Prec: {reg['precip']}")

        elif opcao == "3":
            print(f"{reg['data']} | Max: {reg['maxima']} | Min: {reg['minima']} | Med: {reg['temp_media']}")

        else:
            print("Opção inválida.")
            return


# Mês mais chuvoso
def mes_mais_chuvoso(dados):
    chuva_mensal = {}

    for reg in dados:
        if reg["precip"] is None:
            continue

        chave = f"{reg['mes']:02d}/{reg['ano']}"
        chuva_mensal[chave] = chuva_mensal.get(chave, 0) + reg["precip"]

    mais_chuvoso = max(chuva_mensal, key=chuva_mensal.get)
    total = chuva_mensal[mais_chuvoso]

    print("\n--- MÊS MAIS CHUVOSO ---")
    print(f"Mês/Ano: {mais_chuvoso}")
    print(f"Precipitação total: {total:.2f} mm")


# Média de temperatura mínima
def medias_temp_min(dados, mes_alvo):
    resultados = {}

    for ano in range(2006, 2016 + 1):
        temp = [reg["minima"] for reg in dados
                if reg["ano"] == ano and reg["mes"] == mes_alvo and reg["minima"] is not None]

        if temp:
            resultados[f"{mes_alvo:02d}/{ano}"] = sum(temp) / len(temp)
        else:
            resultados[f"{mes_alvo:02d}/{ano}"] = None

    return resultados


def media_geral(medias):
    valores = [v for v in medias.values() if v is not None]
    if valores:
        print(f"Média geral do período: {sum(valores) / len(valores):.2f} °C")
    else:
        print("Sem dados válidos.")


#Gráfico
def grafico_medias(medias, mes):
    anos = []
    valores = []

    for chave, valor in medias.items():
        if valor is not None:
            anos.append(chave[-4:])
            valores.append(valor)

    plt.figure(figsize=(10, 5))
    plt.bar(anos, valores, color="royalblue")
    plt.title(f"Média da Temperatura Mínima - Mês {mes:02d} (2006–2016)")
    plt.xlabel("Ano")
    plt.ylabel("Temperatura mínima média (°C)")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()

 # Menu do programa

def main():
    dados = carregar_dados(ARQUIVO)
    if not dados:
        return

    while True:
        print("\n=========== MENU ===========")
        print("1 - Visualizar intervalo")
        print("2 - Mês mais chuvoso")
        print("3 - Médias de temperatura mínima 2006–2016")
        print("4 - Gráfico das médias 2006–2016")
        print("0 - Sair")

        opc = input("Escolha: ")

        if opc == "1":
            visualizar_intervalo(dados)

        elif opc == "2":
            mes_mais_chuvoso(dados)

        elif opc == "3":
            mes = int(input("Mês 1-12: "))
            medias = medias_temp_min(dados, mes)
            print("\n--- RESULTADOS ---")
            for k, v in medias.items():
                print(k, "=", v)
            media_geral(medias)

        elif opc == "4":
            mes = int(input("Mês 1-12: "))
            medias = medias_temp_min(dados, mes)
            grafico_medias(medias, mes)

        elif opc == "0":
            print("Encerrando")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
1
