import streamlit as st

# Configurações iniciais do app
st.set_page_config(page_title="App VertexTennis", layout="wide")

# Injetando CSS customizado para simular o layout do VertexTennis
st.markdown(
    """
    <style>
    /* Define a fonte e cor de fundo */
    body {
        background-color: #ffffff;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    /* Container principal do app */
    .reportview-container {
        background: #ffffff;
    }
    /* Cabeçalho (header) customizado */
    header {
        background-color: #000000;
        color: #ffffff;
        padding: 1rem;
        text-align: center;
    }
    /* Customização da barra lateral */
    .sidebar .sidebar-content {
        background-color: #000000;
        color: #ffffff;
    }
    /* Ajuste de títulos */
    h1, h2, h3, h4, h5, h6 {
        color: #000000;
    }
    /* Espaçamentos dos blocos de conteúdo */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Exemplo de cabeçalho (pode ser adaptado conforme a estrutura do seu app)
st.markdown("<header><h1>VertexTennis App</h1></header>", unsafe_allow_html=True)

# Aqui você pode incluir a navegação entre páginas (por exemplo, com st.sidebar.radio)
page = st.sidebar.radio("Navegação", ("Apresentação", "Power BI", "Guia de Implementação"))

if page == "Apresentação":
    st.header("Apresentação da Entrega")
    st.subheader("Equipe Envolvida")
    st.write("""
    - Pessoa 1  
    - Pessoa 2  
    - Pessoa 3  
    """)
    st.markdown("---")
    st.subheader("Vídeo de Apresentação")
    # Substitua pela URL do vídeo desejado
    st.video("https://www.youtube.com/watch?v=VIDEO_ID")

elif page == "Power BI":
    st.header("Relatório Power BI")
    st.write("Veja abaixo o relatório do Power BI:")
    powerbi_url = "https://app.powerbi.com/view?r=PUBLIC_LINK"  # Substitua pelo link real
    st.components.v1.iframe(powerbi_url, height=600, scrolling=True)
    st.markdown("---")
    st.subheader("Análises Extraídas")
    st.write("""
    **Análise 1:** Insight sobre o desempenho dos jogadores.  
    **Análise 2:** Dados de performance em torneios.  
    **Análise 3:** Considerações sobre evolução dos rankings.
    """)

elif page == "Guia de Implementação":
    st.header("Guia de Implementação do Power BI")
    st.markdown("""
    ### Passo a Passo
    1. **Configuração do Ambiente:** Prepare os recursos necessários.
    2. **Publicação do Relatório:** Utilize o 'Publish to Web' ou Power BI Embedded.
    3. **Integração:** Incorpore o relatório no app.
    4. **Validação:** Teste e valide as informações apresentadas.
    
    Este guia tem o objetivo de orientar na implementação do Power BI de forma prática e eficiente.
    """)
    st.markdown("---")
    st.subheader("Download do Guia")
    try:
        with open("guia_implementacao.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="Baixar Guia em PDF",
            data=PDFbyte,
            file_name="guia_implementacao.pdf",
            mime="application/pdf"
        )
    except FileNotFoundError:
        st.error("Arquivo PDF não encontrado. Certifique-se de que 'guia_implementacao.pdf' está na pasta do app.")
