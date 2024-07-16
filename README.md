# BioInsightsTools

BioInsightsTools é uma aplicação web desenvolvida com Streamlit, focada em oferecer soluções em bioinformática. Com esta ferramenta, você pode realizar alinhamentos de sequências de proteínas e DNA, converter sequências de DNA em proteínas, e verificar a qualidade de primers.

## Funcionalidades

1. **Alinhamento BLOSUM62**: Realiza alinhamentos globais e locais de sequências de proteínas usando a matriz de substituição BLOSUM62.
![image](https://github.com/user-attachments/assets/227bb18d-ea12-4b2a-872d-669e53f21eee)

3. **Alinhamento PAM250**: Realiza alinhamentos globais e locais de sequências de proteínas usando a matriz de substituição PAM250.
![image](https://github.com/user-attachments/assets/e68cd12f-17bf-459c-a97d-80ae6a3324bd)

4. **Alinhamento de DNA**: Realiza alinhamentos globais e locais de sequências de DNA.
![image](https://github.com/user-attachments/assets/41ec4b7e-2402-41f1-8127-8d49d2f5c598)

5. **Converter DNA para Proteína**: Transcreve e traduz sequências de DNA em proteínas.
![image](https://github.com/user-attachments/assets/6c74b1f9-8630-480e-b83c-35d79702aa03)

6. **Primer Check**: Verifica a qualidade de uma sequência de primer, calculando seu tamanho, proporção de GC, proporção de AT, e temperatura de melting (Tm).
![image](https://github.com/user-attachments/assets/b6f3b68a-9585-4b60-b857-16d0e5554d21)



## Como Usar

### Requisitos

- Python 3.8 ou superior
- Bibliotecas: Streamlit, Biopython

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/gregorygustavo80/BioInsightsTools.git
    cd BioInsightsTools
    ```

2. Crie um ambiente virtual:

    ```bash
    python -m venv venv
   venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

### Executando a Aplicação

1. Inicie o servidor Streamlit:

    ```bash
    streamlit run graphical_interface.py
    ```

2. Acesse a aplicação no seu navegador no endereço:

    ```
    http://localhost:8501
    ```

## Estrutura do Projeto

- `BioInsightsTools.ipynb`: Código sem interface gráfica
- `graphical_interface.py`: Contém o código principal da aplicação Streamlit.
- `requirements.txt`: Lista de dependências do projeto.
- `README.md`: Este arquivo.

## Exemplo de Uso

### Alinhamento BLOSUM62

1. Selecione "Alinhamento BLOSUM62" no menu lateral.
2. Insira as duas sequências de proteínas.
3. Clique em "Alinhamento Global" ou "Alinhamento Local" para ver o resultado.


### Converter DNA para Proteína

1. Selecione "Converter DNA para Proteína" no menu lateral.
2. Insira a sequência de DNA.
3. Clique em "Converter DNA para Proteína" para ver a sequência de proteína resultante.


## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades. 

