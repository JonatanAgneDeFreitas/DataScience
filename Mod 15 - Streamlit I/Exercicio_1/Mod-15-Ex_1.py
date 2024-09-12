import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('Streamlit')
st.header('Cabeçalho')

st.subheader('Elemento de texto')
st.write('Permite escrever texto em vários estilos.')
st.text('Texto simples.')
st.markdown('**Markdown** texo.')

st.subheader('Exibição de DataFrame')
df = pd.DataFrame({
    'Primeira coluna': [1, 2, 3, 4],
    'Segunda Coluna': [10, 20, 30, 40]
})
st.write('Exibindo um DataFrame:')
st.write(df)

st.subheader('Gráfico de linha')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

st.subheader('Gráfico de barras')
bar_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['X', 'Y', 'Z']
)
st.bar_chart(bar_data)

st.subheader('Map')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

st.subheader('Widgets interativos')

st.write('Slider:')
x = st.slider('Selecione um valor', 0, 100, 50)
st.write('Selecione um valor:', x)

st.write('Input:')
name = st.text_input('Digite o seu Nome', 'Jonatan Freitas')
st.write(f'Olá, {name}!')

st.write('Checkbox:')
if st.checkbox('Mostrar DataFrame'):
    st.write(df)

st.write('Selectbox:')
option = st.selectbox(
    'Qual número você mais gosta?',
    df['Primeira coluna']
)
st.write('Você selecionou:', option)

st.sidebar.header('barra lateral')
sidebar_value = st.sidebar.slider(
    'Controle deslizante da barra lateral', 0, 100, 25)
st.sidebar.write('Valor selecionado da barra lateral:', sidebar_value)

st.subheader('Barra de progresso')
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)

st.subheader('Gráfico plotado')
df2 = pd.DataFrame({
    "Frutas": ["Maçãs", "Laranjas", "Bananas", "Maças", "Laranjas", "Bananas"],
    "Quantia": [4, 1, 2, 2, 4, 5],
    "Cidade": ["São Paulo", "São Paulo", "São Paulo", "Porto Alegre", "Porto Alegre", "Porto Alegre"]
})
fig = px.bar(df2, x="Frutas", y="Quantia", color="Cidade", barmode="group")
st.plotly_chart(fig)

st.subheader('Exemplo Caching')


@st.cache_data
def load_data():
    return pd.DataFrame({
        'A': np.random.randn(1000),
        'B': np.random.randn(1000)
    })


cached_data = load_data()
st.write('Cached DataFrame:')
st.write(cached_data)

st.subheader('Estado da sessão')
if 'counter' not in st.session_state:
    st.session_state.counter = 0

increment = st.button('Contador de incremento')
if increment:
    st.session_state.counter += 1

st.write('Contador:', st.session_state.counter)

st.subheader('Expansor')
with st.expander('Ver explicação'):
    st.write('Esta é uma seção expansível.')

st.subheader('Upload de arquivo')
uploaded_file = st.file_uploader("Escolha um arquivo")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

st.subheader('Colunas')
col1, col2, col3 = st.columns(3)
with col1:
    st.write('Coluna 1')
with col2:
    st.write('Coluna 2')
with col3:
    st.write('Coluna 3')

st.subheader('Exibição de código')
st.code('import streamlit as st\nst.write("Olá, Streamlit!")', language='python')

st.subheader('Mostrar todos os widgets e gráficos')
st.write('Este aplicativo demonstra vários recursos e widgets do Streamlit.')


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
