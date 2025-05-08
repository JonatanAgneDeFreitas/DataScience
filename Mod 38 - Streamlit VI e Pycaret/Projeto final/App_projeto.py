import streamlit as st
import pandas as pd
import pickle
from sklearn.base import BaseEstimator, TransformerMixin

# Classe customizada usada no pipeline salvo
class AplicarPCA(BaseEstimator, TransformerMixin):
    def __init__(self, n_components=5):
        self.n_components = n_components

    def fit(self, X, y=None):
        from sklearn.decomposition import PCA
        self.pca = PCA(n_components=self.n_components)
        self.pca.fit(X)
        return self

    def transform(self, X):
        return self.pca.transform(X)

@st.cache_resource
def load_model():
    with open('model_final.pkl', 'rb') as f:
        return pickle.load(f)

def main():
    st.title("Credit Scoring - Aplicação do Modelo")

    st.write("Faça upload de um arquivo CSV para escoragem:")
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Pré-visualização dos dados carregados:")
        st.dataframe(data.head())

        model = load_model()

        try:
            scores = model.predict_proba(data)[:, 1]
            data['score'] = scores

            st.write("Resultado da escoragem:")
            st.dataframe(data[['score']].head())

            csv = data.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Baixar resultados como CSV",
                data=csv,
                file_name='resultado_escoragem.csv',
                mime='text/csv'
            )
        except Exception as e:
            st.error(f"Erro ao aplicar o modelo: {e}")

if __name__ == '__main__':
    main()
