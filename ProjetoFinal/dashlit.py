import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt 
import matplotlib.patches as ptc
import math as mt

import os

# Carregar os dados do arquivo CSV

data = pd.read_csv('b1319.csv', sep=';')
# Pegar todas as participações de São Paulo e Fladados1

times = list(data['team'])


#Fazer replace de \xa0 por espaço em branco
times = [x.replace('\xa0', '') for x in times]
data['team'] = [x.replace('\xa0', '') for x in data['team']]

# Remover os valores duplicados
times = list(set(times))

dados = data.values
#fazer replace de \xa0 por espaço em branco
for i in range(len(dados)):
    dados[i][2] = dados[i][2].replace('\xa0', '')

#Para cada elemnto da lista de times, Verificar os indices onde aparecu no array dados

time_idx = [np.where(data['team'] == time)[0] for time in times]

# # Salvar em csv os dados de cada time
# for i in range(len(times)):
#     time = times[i]
#     time_data = dados[time_idx[i]]
#     time_data = pd.DataFrame(time_data, columns=data.columns)
#     time_data.to_csv(time+'.csv', sep=';', index=False)

# ler pasta times, e guardar csvs em lista de dataframes



arquivos = []
for root, dirs, files in os.walk('times'):
    for file in files:
        print("name: ", file)
        arquivos.append(pd.read_csv('times/'+file, sep=';'))
        print('-----------------')

# Função para atualizar os gráficos com base no intervalo de anos selecionado
def update_plots(year_range,dados1,dados2,name1,name2,color1,color2):
        fig, ax = plt.subplots(figsize=(16, 10))  # Tamanho específico para a figura
    
    
    
        fig.patch.set_edgecolor('#393939')  # Cor da borda da moldura
        fig.patch.set_linewidth(4)  # Largura da borda da moldura
        fig.patch.set_facecolor('#f0f0f0')  # Cor de fundo da figura (fora da moldura)

        # Adicionando sombra à moldura
        fig.patch.set_edgecolor('black')
        fig.patch.set_linewidth(2)

        # Adicionando um "HUD" como título
        fig.suptitle(f'Desempenho {name1} X {name2}', fontsize=20, color='white', backgroundcolor='black', va='center', ha='center')

        # Definindo o GridSpec com layout 2x6
        gs = plt.GridSpec(2, 6, figure=fig)  # Definindo o GridSpec com 2 linhas e 6 colunas

        dados1_filtered = dados1[(dados1['year'] >= year_range[0]) & (dados1['year'] <= year_range[1])]
        dados2_filtered = dados2[(dados2['year'] >= year_range[0]) & (dados2['year'] <= year_range[1])]

        # Plotar o gráfico de linha comparando a posição final de Fladados1 e São Paulo ao longo dos anos
        ax1 = fig.add_subplot(gs[0, :3])  # Utilizando as três primeiras colunas na primeira linha
        sns.lineplot(x='year', y='position', data=dados1_filtered, label=name1, marker='o', color=color1, ax=ax1)
        sns.lineplot(x='year', y='position', data=dados2_filtered, label=name2, marker='o', color=color2, ax=ax1)
        ax1.set_xlabel('Ano')
        ax1.set_ylabel('Posição Final')
        ax1.set_title(f'Posição Final de {name1} e {name2} ao Longo dos Anos')
        ax1.legend()
        ax1.grid(True)
        ax1.set_xticks(range(year_range[0], year_range[1] + 1, 1))
        ax1.invert_yaxis()

        # Plotar gráfico de barras sobrepostas para comparar a quantidade de pontos de Fladados1 e São Paulo ao longo dos anos
        ax2 = fig.add_subplot(gs[0, 3:])  # Utilizando as três últimas colunas na primeira linha
        sns.barplot(x='year', y='points', data=dados1_filtered, color=color1, alpha=0.7, label=name1, ax=ax2)
        sns.barplot(x='year', y='points', data=dados2_filtered, color=color2, alpha=0.7, label=name2, ax=ax2)
        ax2.set_xlabel('Ano')
        ax2.set_ylabel('Pontos')
        ax2.set_title(f'Pontos de {name1} e {name2} ao Longo dos Anos')
        ax2.legend()
        ax2.grid(True)
        plt.xticks(rotation=45)

        # Para o restante das colunas, fazer gráfico de setor para comparar os valores
        columns = dados1.columns[3:-2]  # Selecionando as colunas relevantes
        for i, column in enumerate(columns, start=0):  # Começando a partir da primeira posição
            if i < 6:  # Garantindo que não exceda o número de colunas definidas no GridSpec
                ax3 = fig.add_subplot(gs[1, i])  # Ajustando a posição do subplot
                dados1_total = dados1_filtered[column].sum()
                dados2_total = dados2_filtered[column].sum()
                sizes = [dados1_total, dados2_total]
                labels = [name1, name2]
                colors = [color1, color2]
                explode = (0.1, 0)  # Explodir a primeira fatia
                ax3.pie(sizes, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 12, 'color': 'white'})
                ax3.legend(labels, loc='upper right', bbox_to_anchor=(0.75, 0.55, 0.5, 0.5))
                ax3.set_title(f'Distribuição de {column.capitalize()}')
        
        # Personalizando a borda da figura para se assemelhar a uma moldura
        for spine in ax.spines.values():
            spine.set_visible(False)  # Esconde as bordas padrão
        ax.figure.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1)  # Ajusta o layout da figura



        # Desativar números da imagem (eixo x e y)
        ax.axis('off')

        st.pyplot(fig)  # Exibe o gráfico no Streamlit

# # Carregue seus DataFrames 'dados1' e 'dados2'
# dados1 = arquivos[18]
# dados2 = arquivos[41]

# Array com todas as cores dos times brasileiros em hexadecimal
cores_times = [
    '#000000',  # Paysandu
    '#009BDA',  # Botafogo
    '#FFFFFF',  # Náutico
    '#0000FF',  # Grêmio Barueri
    '#FDF200',  # Brasiliense
    '#EF0029',  # Atlético Paranaense
    '#008E49',  # CSA
    '#0D75BA',  # Cruzeiro
    '#000080',  # Vasco da Gama
    '#1E2C5B',  # São Caetano
    '#0073E6',  # Bahia
    '#FFA500',  # Ponte Preta
    '#FFFFFF',  # Santos
    '#000000',  # Paraná
    '#0C2340',  # América de Natal
    '#000000',  # Athletico Paranaense
    '#0000CD',  # América Mineiro
    '#EE0000',  # Santa Cruz
    '#1B7742',  # Grêmio
    '#006400',  # Palmeiras
    '#8B0000',  # Atlético Goianiense
    '#AF002A',  # Fluminense
    '#FFD700',  # Guarani
    '#000000',  # São Paulo
    '#FFD700',  # Ipatinga
    '#FF0000',  # Flamengo
    '#FF6600',  # Vitória
    '#003399',  # Grêmio Prudente
    '#0000FF',  # Figueirense
    '#6B8E23',  # Chapecoense
    '#000000',  # Atlético Mineiro
    '#1E90FF',  # Avaí
    '#FFD700',  # Criciúma
    '#FF4500',  # Sport
    '#7700FF',  # Juventude
    '#FF6600',  # Joinville
    '#000000',  # Fortaleza
    '#006600',  # Goiás
    '#000000',  # Corinthians
    '#FF6F00',  # Internacional
    '#00008B',  # Ceará
    '#7F462C',  # Coritiba
    '#D1212D',  # Portuguesa
    '#000000'   # Santo André
]



# Título do aplicativo
st.title('Desempenho de Clubes de Futebol')

# Descrição do aplicativo
st.write("Este dashboard compara o desempenho de dois clubes de futebol ao longo dos anos.")

# Criando a barra deslizante interativa para o período
year_range = st.slider('Selecione o período de anos:', min_value=2003, max_value=2019, value=(2003, 2019))

# Adicione o cabeçalho da seção
st.header('Comparação de Desempenho')

# Adicione uma descrição da seção
st.write("Aqui você pode comparar o desempenho de dois clubes de futebol ao longo dos anos.")

# Seleção dos clubes a serem comparados
name1 = st.selectbox('Selecione o primeiro clube:', options=times)  # 'times' é uma lista com os nomes dos clubes
name2 = st.selectbox('Selecione o segundo clube:', options=times)  # 'times' é uma lista com os nomes dos clubes

# selecionar a cor do time dentre as opções da lista 'cores_times'
color1 = cores_times[times.index(name1)]
color1 = st.color_picker('Escolha a cor do primeiro clube', color1)
color2 = cores_times[times.index(name2)]
color2 = st.color_picker('Escolha a cor do segundo clube', color2)

dados1 = arquivos[times.index(name1)]
dados2 = arquivos[times.index(name2)]

# Atualização dos gráficos com base nas seleções do usuário
update_plots(year_range, dados1, dados2, name1, name2, color1, color2)
