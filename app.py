import streamlit as st

# Configurações iniciais do app
st.set_page_config(page_title="App VertexTennis", layout="wide")

# Injetando CSS customizado para simular o layout do VertexTennis
st.markdown(
    """
    <style>
    /* Reset e estilos base */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Definindo cores do Vertex Tennis */
    :root {
        --vertex-dark: #1E1E1E;
        --vertex-green: #0B9E84;
        --vertex-white: #FFFFFF;
        --vertex-light-gray: #F5F5F5;
    }
    
    /* Estilos gerais */
    .main .block-container {
        padding-top: 0;
        max-width: 100%;
        padding-left: 0;
        padding-right: 0;
    }
    
    /* Cabeçalho principal */
    .stApp header {
        background-color: var(--vertex-white);
        border-bottom: 1px solid #e0e0e0;
        padding: 0.8rem 2rem;
        display: flex;
        align-items: center;
    }
    
    /* Logo estilo */
    .vertex-logo {
        font-size: 24px;
        font-weight: bold;
        color: var(--vertex-dark);
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .vertex-logo-symbol {
        color: var(--vertex-green);
        font-size: 28px;
    }
    
    /* Navegação principal */
    .main-nav {
        display: flex;
        gap: 2rem;
        margin-left: 3rem;
    }
    
    .nav-item {
        text-transform: uppercase;
        font-weight: 500;
        font-size: 16px;
        color: var(--vertex-dark);
        text-decoration: none;
    }
    
    /* Hero section */
    .hero-section {
        background-color: var(--vertex-dark);
        color: var(--vertex-white);
        padding: 3rem 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1544298621-35a764850d0b');
        background-size: cover;
        background-position: center;
        height: 300px;
        justify-content: center;
    }
    
    .hero-title {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        max-width: 600px;
        margin: 0 auto;
    }
    
    /* Cards de conteúdo */
    .content-cards {
        display: flex;
        gap: 2rem;
        padding: 2rem;
        flex-wrap: wrap;
    }
    
    .content-card {
        background-color: var(--vertex-white);
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        flex: 1;
        min-width: 300px;
    }
    
    .card-image {
        height: 200px;
        background-size: cover;
        background-position: center;
    }
    
    .card-content {
        padding: 1.5rem;
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        color: var(--vertex-dark);
    }
    
    .card-text {
        color: #666;
        margin-bottom: 1rem;
    }
    
    .card-link {
        display: inline-block;
        color: var(--vertex-green);
        font-weight: 500;
        text-decoration: none;
    }
    
    /* Barra lateral customizada */
    .css-1d391kg, .css-1lcbmhc {
        background-color: var(--vertex-dark);
    }
    
    .sidebar .sidebar-content {
        background-color: var(--vertex-dark);
        color: var(--vertex-white);
    }
    
    /* Escondendo header padrão do Streamlit */
    #MainMenu, header, footer {
        visibility: hidden;
    }
    
    /* Botões customizados */
    .stButton>button {
        background-color: var(--vertex-green);
        color: white;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }
    
    .stButton>button:hover {
        background-color: #097a69;
    }
    
    /* Video placeholder */
    .video-placeholder {
        background-color: #333;
        height: 400px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #888;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar customizada
st.sidebar.markdown(
    """
    <div style="padding: 16px; color: white;">
        <h3 style="color: white;">Navegação</h3>
    </div>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio("", ("Apresentação", "Power BI", "Guia de Implementação"))

# Header customizado
st.markdown(
    """
    <header style="position: fixed; top: 0; left: 0; right: 0; z-index: 999; background-color: white; border-bottom: 1px solid #e0e0e0; display: flex; justify-content: space-between; padding: 12px 24px; align-items: center;">
        <div class="vertex-logo">
            <span class="vertex-logo-symbol">✓</span> VertexTennis
        </div>
        <div class="main-nav">
            <a href="#" class="nav-item">Raquetes</a>
            <a href="#" class="nav-item">Equipamentos</a>
            <a href="#" class="nav-item">Vestuário</a>
            <a href="#" class="nav-item">Sobre</a>
        </div>
    </header>
    <div style="height: 60px;"></div> <!-- Espaço para compensar o header fixo -->
    """,
    unsafe_allow_html=True
)

# Conteúdo principal baseado na página selecionada
if page == "Apresentação":
    # Hero section
    st.markdown(
        """
        <div class="hero-section">
            <div class="hero-title">VertexTennis App</div>
            <div class="hero-subtitle">Onde qualidade e desempenho jogam no mesmo time.</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<h2 style='padding: 20px 0 10px 24px;'>Apresentação da Entrega</h2>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="padding: 0 24px;">
            <h3 style="margin-bottom: 20px;">Equipe Envolvida</h3>
            <ul style="list-style-type: disc; margin-left: 20px;">
                <li style="margin-bottom: 8px;">Pessoa 1</li>
                <li style="margin-bottom: 8px;">Pessoa 2</li>
                <li style="margin-bottom: 8px;">Pessoa 3</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<hr style='margin: 30px 24px;'>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="padding: 0 24px;">
            <h3 style="margin-bottom: 20px;">Vídeo de Apresentação</h3>
            <div class="video-placeholder">Vídeo de apresentação será exibido aqui</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Cards de conteúdo similares ao site
    st.markdown(
        """
        <div style="padding: 30px 24px;">
            <h2 style="margin-bottom: 20px;">Conheça Nossos Produtos</h2>
            <div class="content-cards">
                <div class="content-card">
                    <div class="card-image" style="background-image: url('https://images.unsplash.com/photo-1622279457486-28f280ae9d7a');"></div>
                    <div class="card-content">
                        <h3 class="card-title">Saiba mais sobre a Vertex</h3>
                        <p class="card-text">Conheça nossa história, valores e compromisso com a qualidade.</p>
                        <a href="#" class="card-link">Sobre nós »</a>
                    </div>
                </div>
                <div class="content-card">
                    <div class="card-image" style="background-image: url('https://images.unsplash.com/photo-1617399966459-cf30c19e0337');"></div>
                    <div class="card-content">
                        <h3 class="card-title">Máxima qualidade e desempenho</h3>
                        <p class="card-text">Descubra nossa linha Profissional de raquetes.</p>
                        <a href="#" class="card-link">Conhecer »</a>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
elif page == "Power BI":
    st.markdown(
        """
        <div style="padding: 24px;">
            <h2 style="margin-bottom: 20px;">Relatório Power BI</h2>
            <p style="margin-bottom: 20px;">Veja abaixo o relatório do Power BI:</p>
            <div style="background-color: #f5f5f5; padding: 20px; border-radius: 8px; height: 600px; display: flex; align-items: center; justify-content: center; color: #888; font-size: 18px;">
                Aqui será exibido o relatório do Power BI
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<hr style='margin: 30px 24px;'>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="padding: 0 24px;">
            <h3 style="margin-bottom: 20px;">Análises Extraídas</h3>
            <div style="background-color: white; padding: 24px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="margin-bottom: 16px;"><strong>Análise 1:</strong> Insight sobre o desempenho dos jogadores.</p>
                <p style="margin-bottom: 16px;"><strong>Análise 2:</strong> Dados de performance em torneios.</p>
                <p><strong>Análise 3:</strong> Considerações sobre evolução dos rankings.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
elif page == "Guia de Implementação":
    st.markdown(
        """
        <div style="padding: 24px;">
            <h2 style="margin-bottom: 20px;">Guia de Implementação do Power BI</h2>
            <div style="background-color: white; padding: 24px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <h3 style="margin-bottom: 16px;">Passo a Passo</h3>
                <ol style="margin-left: 20px; margin-bottom: 24px;">
                    <li style="margin-bottom: 12px;"><strong>Configuração do Ambiente:</strong> Prepare os recursos necessários.</li>
                    <li style="margin-bottom: 12px;"><strong>Publicação do Relatório:</strong> Utilize o 'Publish to Web' ou Power BI Embedded.</li>
                    <li style="margin-bottom: 12px;"><strong>Integração:</strong> Incorpore o relatório no app.</li>
                    <li><strong>Validação:</strong> Teste e valide as informações apresentadas.</li>
                </ol>
                <p>Este guia tem o objetivo de orientar na implementação do Power BI de forma prática e eficiente.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<hr style='margin: 30px 24px;'>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="padding: 0 24px;">
            <h3 style="margin-bottom: 20px;">Download do Guia</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Botão de download
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
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
