import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def scrape_dados_b3(ticker):
    """Extrai dados financeiros de uma empresa da B3.

    Args:
        ticker (str): Código do ativo na B3.

    Returns:
        dict: Dicionário com os dados extraídos.
    """

    url = f"https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/consultas/empresas/empresas-listadas/Paginas/ResumoEmpresa.aspx?codigoAtivo={ticker}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Adaptar os seletores CSS para a estrutura atual do site da B3
    ativo_circulante = soup.select_one("#ctl00_ContentPlaceHolder1_grdDemonstracoesFinanceiras_ctl01_lblAtivoCirculante")
    passivo_circulante = soup.select_one("#ctl00_ContentPlaceHolder1_grdDemonstracoesFinanceiras_ctl01_lblPassivoCirculante")

    # ... extrair outros dados ...

    return {
        "Ativo Circulante": float(ativo_circulante.replace(",", ".")),
        "Passivo Circulante": float(passivo_circulante.replace(",", ".")),
        # ... outros dados ...
        }

def calcular_indicadores(df):
    """Calcula indicadores financeiros.

    Args:
        df (pd.DataFrame): DataFrame com os dados financeiros.

    Returns:
        pd.DataFrame: DataFrame com os indicadores calculados.
    """

    df['Current Ratio'] = df['Ativo Circulante'] / df['Passivo Circulante']
    # ... calcular outros indicadores ...
    return df

# Lista de tickers
tickers = ['PETR4', 'VALE3', 'SAPR4', 'TAEE11', 'BBAS3' ]

# Coletar dados
dados = []
for ticker in tickers:
    dados.append(scrape_dados_b3(ticker))

# Criar DataFrame
df = pd.DataFrame(dados)

# Calcular indicadores
df = calcular_indicadores(df)

# Visualizar resultados
plt.bar(df.index, df['Current Ratio'])
plt.xlabel('Empresas')
plt.ylabel('Current Ratio')
plt.title('Current Ratio por Empresa')
plt.show()

-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -


# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Função para calcular os indicadores
def calcular_indicadores(dre, balanco):
  # Cálculo dos indicadores
  liquidez_imediata = balanco['Ativo Circulante'] / balanco['Passivo Circulante']
  liquidez_reduzida = (balanco['Ativo Circulante'] - balanco['Estoques']) / balanco['Passivo Circulante']
  liquidez_corrente = balanco['Ativo Circulante'] / balanco['Passivo Circulante']
  endividamento_total = balanco['Passivo Total'] / balanco['Ativo Total']
  rentabilidade_ativo = dre['Lucro Líquido'] / balanco['Ativo Total']

  # Retorno dos indicadores
  return liquidez_imediata, liquidez_reduzida, liquidez_corrente, endividamento_total, rentabilidade_ativo

# Função para gerar o relatório
def gerar_relatorio(empresa, indicadores):
  # Criação do relatório
  relatorio = f"Relatório de Análise Financeira - {empresa}\n\n"
  relatorio += f"Indicadores:\n"
  relatorio += f"Liquidez Imediata: {indicadores[0]:.2f}\n"
  relatorio += f"Liquidez Reduzida: {indicadores[1]:.2f}\n"
  relatorio += f"Liquidez Corrente: {indicadores[2]:.2f}\n"
  relatorio += f"Endividamento Total: {indicadores[3]:.2f}\n"
  relatorio += f"Rentabilidade do Ativo: {indicadores[4]:.2f}\n\n"

  # Interpretação dos resultados
  relatorio += "Interpretação:\n"
  # ... (Adicione aqui a interpretação dos resultados)

  # Retorno do relatório
  return relatorio

# Exemplo de uso
empresa = "Nome da empresa"
dre = pd.DataFrame(...) # Dados da DRE
balanco = pd.DataFrame(...) # Dados do Balanço Patrimonial

indicadores = calcular_indicadores(dre, balanco)
relatorio = gerar_relatorio(empresa, indicadores)

print(relatorio)

# Geração de gráficos
plt.plot(...) # Gráfico dos indicadores
plt.show()