#%%
import pandas as pd

url = "https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_popula%C3%A7%C3%A3o?utm_source=chatgpt.com"

df = pd.read_html(url,storage_options={"User-Agent": "Mozilla/5.0"})
uf = df[1]
uf.dtypes
# %%
def str_to_int(coluna):
    coluna = coluna.replace(".","")
    coluna = coluna.replace(" ","")
    coluna = coluna.replace("\xa0","")
    return int(coluna)      

# %%
#tirando a coluna total com filtro

filtro = uf["Unidade federativa","Unidade federativa"] != "Total"

uf = uf[filtro]
uf

#%%
#Conversao para int
uf["População[3][4]","2025 (est.)"] = uf["População[3][4]","2025 (est.)"].apply(str_to_int)

uf["População[3][4]","2022"] = uf["População[3][4]","2022"].apply(str_to_int)

uf["Variação (2010-2022)[3]","Abs."] = uf["Variação (2010-2022)[3]","Abs."].apply(str_to_int)

# Mostrar os 10 estados mais populosos pela estimativa de 2025
uf.sort_values(by=("População[3][4]","2025 (est.)"),ascending=False).head(10) 

# %%

#Mostrar estados com população acima de 10 milhões pela estimativa de 2025

pop_mais_10_milhões = uf["População[3][4]","2025 (est.)"] > 10000000
uf[pop_mais_10_milhões]


# %%

# Mostrar apenas estados do Nordeste
filtro_nordeste = uf["Unidade federativa","Unidade federativa"].isin(["Bahia","Pernambuco","Ceará","Maranhão","Paraíba","Rio Grande do Norte","Piauí","Alagoas","Sergipe"])
uf[filtro_nordeste]

# %%
# Encontrar o estado mais populoso pela estimativa de 2025

mais_populoso  =  uf["População[3][4]","2025 (est.)"] == uf["População[3][4]","2025 (est.)"].max()
uf[mais_populoso]

# %%
# menos populoso pela estimativa de 2025
menos_populoso  =  uf["População[3][4]","2025 (est.)"] == uf["População[3][4]","2025 (est.)"].min()
uf[menos_populoso]
# %%
#Criar coluna de classificação populacional
#Exemplo:
#acima de 15 milhões → “Muito Populoso”
#acima de 5 milhões → “Populoso”
#resto → “Menor População”

lista = []

for pop in uf["População[3][4]","2025 (est.)"]: 
    if pop > 15000000:
        lista.append("Muito Populoso")

    elif pop > 5000000:
        lista.append("Populoso")

    else:
        lista.append("Menor População")

uf["classificação populacional"] = lista
uf
# %%

url_pib = "https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_PIB"

tabelas_pib = pd.read_html(url_pib, storage_options={"User-Agent": "Mozilla/5.0"})

pib = tabelas_pib[1]
#ainda e dataframe
#%%
#tirando o a linha total da tabela
filtro = pib["Unidade federativa","Unidade federativa"] != "Total"
pib = pib[filtro]

#ainda e dtaframe
# %%

pib["PIB (R$ 1.000)","PIB (R$ 1.000)"] = pib["PIB (R$ 1.000)","PIB (R$ 1.000)"].apply(str_to_int)
#ainda e dataframe

# %%
## Estados com PIB acima de 500000000000
filtro = pib["PIB (R$ 1.000)","PIB (R$ 1.000)"] > 500000000
pib[filtro]

#ainda e dataframe
# %%
## Top 10 maiores PIBs
pib.sort_values(by=("PIB (R$ 1.000)","PIB (R$ 1.000)"),ascending=False).head(10) 


# %%
## Top 10 menores PIBs
pib.sort_values(by=("PIB (R$ 1.000)","PIB (R$ 1.000)"),ascending=True).head(10) 


# %%
#
# Criar classificação econômica:
# acima de 1000000000000 -> "Economia muito grande"
# acima de 300000000000 -> "Economia grande"
# resto -> "Economia menor"
#
#

lista_pib = []

for pibs in pib["PIB (R$ 1.000)", "PIB (R$ 1.000)"]:

    if pibs > 1000000000:
        lista_pib.append("Economia muito grande")

    elif pibs > 300000000:
        lista_pib.append("Economia grande")

    else:
        lista_pib.append("Economia menor")

pib["classificação econômica"] = lista_pib
# %%
pib
# %%
