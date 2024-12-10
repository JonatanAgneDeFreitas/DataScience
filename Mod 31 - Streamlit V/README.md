**Por:** [Jonatan Agne de Freitas](https://www.linkedin.com/in/jonatan-agne-de-freitas/)<br>

---

#### **Descrição:**
Segmentação de clientes utilizando o RFV.
RFV significa recência, frequência, valor e é utilizado para segmentação de clientes baseado no comportamento
de compras dos clientes e agrupa eles em clusters parecidos. Utilizando esse tipo de agrupamento podemos realizar 
ações de marketing e CRM melhores direcionadas, ajudando assim na personalização do conteúdo e até a retenção de clientes.

Para cada cliente é preciso calcular as componentes abaixo:

- Recência (R): Quantidade de dias desde a última compra.
- Frenquência (F): Quantidade total de compras no período.
- Valor (V): Total de dinheiro gasto nas compras do período.

#### Link para a aplicação (*Deploy* do modelo/streamlit)


[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=Streamlit&logoColor=white)](https://deployrfvjaf.streamlit.app/)

---

#### [Requisitos](https://github.com/JonatanAgneDeFreitas/DataScience/blob/main/Mod%2031%20-%20Streamlit%20V/requirements.txt)
```bash
numpy==1.26.4
pandas==2.2.2
streamlit==1.35.0
XlsxWriter==3.2.0
```

#### Instalação
```bash
pip install -r requirements.txt
```

#### *Imports*
```python
import numpy     as np
import pandas    as pd
import streamlit as st

from datetime    import datetime
from PIL         import Image
from io          import BytesIO
```

---
