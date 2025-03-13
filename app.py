import streamlit as st

# Configurações iniciais do app
st.set_page_config(page_title="App VertexTennis", layout="wide")

# Script para toggle de tema (claro/escuro)
theme_script = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Verificar se já existe uma preferência armazenada
    const currentTheme = localStorage.getItem('theme') || 'dark';
    document.body.setAttribute('data-theme', currentTheme);
    
    // Função para alternar o tema
    window.toggleTheme = function() {
        const currentTheme = document.body.getAttribute('data-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        document.body.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
    }
});
</script>
"""

st.components.v1.html(theme_script)

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
    
    /* Sistema de temas (claro/escuro) */
    :root {
        --vertex-brand-green: #0B9E84;
        --vertex-neon-green: #9AFF02;
        --vertex-teal: #007273;
        --vertex-red: #C44D30;
        
        /* Cores variáveis que mudam com o tema */
        --bg-primary: #FFFFFF;
        --bg-secondary: #F5F5F5;
        --bg-tertiary: #E8E8E8;
        --text-primary: #1E1E1E;
        --text-secondary: #555555;
        --card-bg: #FFFFFF;
        --card-border: #E0E0E0;
        --sidebar-bg: #1E1E1E;
        --sidebar-text: #FFFFFF;
        --highlight-bg: #0B9E84;
        --highlight-text: #FFFFFF;
        --button-primary: #0B9E84;
        --button-hover: #089077;
        --nav-border: #E0E0E0;
    }
    
    /* Tema escuro */
    [data-theme="dark"] {
        --bg-primary: #1E1E1E;
        --bg-secondary: #2D2D2D;
        --bg-tertiary: #383838;
        --text-primary: #FFFFFF;
        --text-secondary: #CCCCCC;
        --card-bg: #2D2D2D;
        --card-border: #3D3D3D;
        --sidebar-bg: #121212;
        --sidebar-text: #FFFFFF;
        --highlight-bg: #0B9E84;
        --highlight-text: #FFFFFF;
        --button-primary: #0B9E84;
        --button-hover: #089077;
        --nav-border: #3D3D3D;
    }
    
    /* Estilos Gerais */
    body {
        background-color: var(--bg-primary);
        color: var(--text-primary);
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        transition: background-color 0.3s, color 0.3s;
    }
    
    .main .block-container {
        padding-top: 0;
        max-width: 100%;
        padding-left: 0;
        padding-right: 0;
        background-color: var(--bg-primary);
    }
    
    /* Cabeçalho principal */
    .stApp header {
        background-color: var(--bg-primary);
        border-bottom: 1px solid var(--nav-border);
        padding: 0.8rem 2rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    
    /* Logo estilo */
    .vertex-logo {
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .logo-text {
        font-size: 24px;
        font-weight: bold;
        color: var(--text-primary);
        text-transform: uppercase;
    }
    
    /* Navegação principal */
    .main-nav {
        display: flex;
        gap: 2rem;
    }
    
    .nav-item {
        text-transform: uppercase;
        font-weight: 500;
        font-size: 16px;
        color: var(--text-primary);
        text-decoration: none;
        transition: color 0.2s;
    }
    
    .nav-item:hover {
        color: var(--vertex-brand-green);
    }
    
    /* Theme toggle */
    .theme-toggle {
        background: none;
        border: none;
        color: var(--text-primary);
        cursor: pointer;
        font-size: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background-color: var(--bg-tertiary);
    }
    
    /* Seção de conteúdo */
    .content-section {
        background-color: var(--bg-primary);
        color: var(--text-primary);
        padding: 2rem;
        min-height: calc(100vh - 60px);
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary);
    }
    
    /* Área do relatório de Power BI */
    .powerbi-container {
        background-color: var(--bg-secondary);
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 30px;
        height: 500px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: var(--text-secondary);
    }
    
    /* Cards de análise */
    .analysis-section {
        background-color: var(--bg-primary);
        padding: 20px 0;
    }
    
    .analysis-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
        color: var(--text-primary);
    }
    
    .analysis-card {
        background-color: var(--highlight-bg);
        color: var(--highlight-text);
        padding: 12px 16px;
        margin-bottom: 12px;
        border-radius: 4px;
    }
    
    /* Exibição de produtos */
    .products-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        padding: 20px 0;
    }
    
    .product-card {
        background-color: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 8px;
        overflow: hidden;
        width: calc(25% - 15px);
        display: flex;
        flex-direction: column;
    }
    
    .product-image {
        height: 200px;
        position: relative;
    }
    
    .product-info {
        padding: 16px;
        display: flex;
        flex-direction: column;
        flex-grow: 1;
    }
    
    .product-title {
        font-size: 18px;
        font-weight: 500;
        margin-bottom: 8px;
        color: var(--text-primary);
    }
    
    .product-link {
        text-decoration: none;
        color: var(--vertex-brand-green);
        font-weight: 500;
        margin-top: auto;
    }
    
    /* Footer */
    .footer {
        background-color: var(--vertex-neon-green);
        color: #000000;
        padding: 40px 0;
    }
    
    .footer-content {
        display: flex;
        flex-wrap: wrap;
        gap: 40px;
        justify-content: space-between;
        padding: 0 40px;
    }
    
    .footer-logo {
        margin-bottom: 30px;
    }
    
    .footer-section {
        min-width: 200px;
    }
    
    .footer-heading {
        font-weight: bold;
        font-size: 16px;
        margin-bottom: 16px;
        color: #000000;
    }
    
    .footer-links {
        list-style: none;
    }
    
    .footer-links li {
        margin-bottom: 8px;
    }
    
    .footer-links a {
        color: #000000;
        text-decoration: none;
    }
    
    .footer-links a:hover {
        text-decoration: underline;
    }
    
    /* Barra lateral customizada */
    .css-1d391kg, .css-1lcbmhc, .css-1oe6wy4 {
        background-color: var(--sidebar-bg);
    }
    
    .sidebar .sidebar-content {
        background-color: var(--sidebar-bg);
        color: var(--sidebar-text);
    }
    
    /* Radio buttons na sidebar */
    .st-cc {
        color: var(--sidebar-text) !important;
    }
    
    .st-cd {
        background-color: var(--vertex-brand-green) !important;
    }
    
    /* Escondendo header padrão do Streamlit */
    #MainMenu, header, footer {
        visibility: hidden;
    }
    
    /* Botões customizados */
    .stButton>button {
        background-color: var(--button-primary);
        color: white;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: background-color 0.3s;
    }
    
    .stButton>button:hover {
        background-color: var(--button-hover);
    }
    
    /* Linha divisória */
    .divider {
        height: 1px;
        background-color: var(--nav-border);
        margin: 30px 0;
    }
    
    /* Ver todos os produtos link */
    .see-all-link {
        display: block;
        color: var(--vertex-brand-green);
        text-decoration: none;
        margin: 20px 0;
        font-weight: 500;
    }
    
    /* Responsividade */
    @media (max-width: 768px) {
        .product-card {
            width: calc(50% - 10px);
        }
        
        .main-nav {
            display: none;
        }
    }
    
    @media (max-width: 480px) {
        .product-card {
            width: 100%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar customizada
st.sidebar.markdown(
    """
    <div style="padding: 16px; color: var(--sidebar-text);">
        <h3 style="color: var(--sidebar-text);">Navegação</h3>
    </div>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio("", ("Apresentação", "Power BI", "Guia de Implementação"))

# Header customizado com logo e botão de tema
st.markdown(
    """
    <header style="position: fixed; top: 0; left: 0; right: 0; z-index: 999; background-color: var(--bg-primary); border-bottom: 1px solid var(--nav-border); display: flex; justify-content: space-between; padding: 12px 24px; align-items: center;">
        <div class="vertex-logo">
            <svg width="36" height="36" viewBox="0 0 36 36" fill="none">
                <path d="M8 8L28 28M8 28L28 8" stroke="#0B9E84" stroke-width="4" stroke-linecap="round"/>
                <path d="M18 5C14.9 5 12.1 5 9.5 5C6.9 5 5 6.9 5 9.5C5 12.1 5 14.9 5 18" stroke="#0B9E84" stroke-width="4" stroke-linecap="round"/>
                <path d="M18 31C21.1 31 23.9 31 26.5 31C29.1 31 31 29.1 31 26.5C31 23.9 31 21.1 31 18" stroke="#0B9E84" stroke-width="4" stroke-linecap="round"/>
            </svg>
            <span class="logo-text">VertexTennis</span>
        </div>
        <div class="main-nav">
            <a href="#" class="nav-item">Raquetes</a>
            <a href="#" class="nav-item">Equipamentos</a>
            <a href="#" class="nav-item">Vestuário</a>
            <a href="#" class="nav-item">Sobre</a>
        </div>
        <button class="theme-toggle" onclick="toggleTheme()">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M12 16C14.2091 16 16 14.2091 16 12C16 9.79086 14.2091 8 12 8C9.79086 8 8 9.79086 8 12C8 14.2091 9.79086 16 12 16Z" stroke="currentColor" stroke-width="2"/>
                <path d="M12 2V4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                <path d="M12 20V22" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                <path d="M4 12H2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                <path d="M22 12H20" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                <path d="M6.34315 6.34315L4.92893 4.92893" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                <path d="M19.0711 19.0711L17.6569 17.6569" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                <path d="M6.34315 17.6569L4.92893 19.0711" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                <path d="M19.0711 4.92893L17.6569 6.34315" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
        </button>
    </header>
    <div style="height: 60px;"></div> <!-- Espaço para compensar o header fixo -->
    """,
    unsafe_allow_html=True
)

# Conteúdo principal baseado na página selecionada
if page == "Apresentação":
    st.markdown(
        """
        <div class="content-section">
            <h2>Apresentação da Entrega</h2>
            <div style="margin-top: 20px;">
                <h3>Equipe Envolvida</h3>
                <ul style="list-style-type: disc; margin-left: 20px; margin-top: 10px;">
                    <li style="margin-bottom: 8px;">Pessoa 1</li>
                    <li style="margin-bottom: 8px;">Pessoa 2</li>
                    <li style="margin-bottom: 8px;">Pessoa 3</li>
                </ul>
            </div>
            
            <div class="divider"></div>
            
            <h3>Vídeo de Apresentação</h3>
            <div style="background-color: var(--bg-secondary); height: 400px; border-radius: 8px; margin-top: 20px; display: flex; align-items: center; justify-content: center; color: var(--text-secondary);">
                Vídeo de apresentação será exibido aqui
            </div>
            
            <div style="margin-top: 40px;">
                <h2>Produtos em Destaque</h2>
                <div class="products-container">
                    <div class="product-card">
                        <div class="product-image" style="background-color: #9AFF02; display: flex; align-items: center; justify-content: center;">
                            <svg width="100" height="100" viewBox="0 0 36 36" fill="none">
                                <path d="M8 8L28 28M8 28L28 8" stroke="white" stroke-width="4" stroke-linecap="round"/>
                            </svg>
                        </div>
                        <div class="product-info">
                            <div class="product-title">Titan Core Preto</div>
                            <a href="#" class="product-link">Ver produto</a>
                        </div>
                    </div>
                    
                    <div class="product-card">
                        <div class="product-image" style="background-color: #007273; display: flex; align-items: center; justify-content: center;">
                            <svg width="100" height="100" viewBox="0 0 36 36" fill="none">
                                <path d="M8 8L28 28M8 28L28 8" stroke="white" stroke-width="4" stroke-linecap="round"/>
                            </svg>
                        </div>
                        <div class="product-info">
                            <div class="product-title">Supreme Flex Cinza</div>
                            <a href="#" class="product-link">Ver produto</a>
                        </div>
                    </div>
                    
                    <div class="product-card">
                        <div class="product-image" style="background-color: #C44D30; display: flex; align-items: center; justify-content: center;">
                            <svg width="100" height="100" viewBox="0 0 36 36" fill="none">
                                <path d="M8 8L28 28M8 28L28 8" stroke="white" stroke-width="4" stroke-linecap="round"/>
                            </svg>
                        </div>
                        <div class="product-info">
                            <div class="product-title">Prime Gut</div>
                            <a href="#" class="product-link">Ver produto</a>
                        </div>
                    </div>
                    
                    <div class="product-card">
                        <div class="product-image" style="background-color: #9AFF02; display: flex; align-items: center; justify-content: center;">
                            <svg width="100" height="100" viewBox="0 0 36 36" fill="none">
                                <path d="M8 8L28 28M8 28L28 8" stroke="white" stroke-width="4" stroke-linecap="round"/>
                            </svg>
                        </div>
                        <div class="product-info">
                            <div class="product-title">Iron Spin Verde Neon</div>
                            <a href="#" class="product-link">Ver produto</a>
                        </div>
                    </div>
                </div>
                
                <a href="#" class="see-all-link">Ver todas as cordas »</a>
            </div>
        </div>
        
        <!-- Footer -->
        <div class="footer">
            <div class="footer-content">
                <div class="footer-section">
                    <div class="footer-logo">
                        <svg width="120" height="50" viewBox="0 0 120 50" fill="none">
                            <path d="M20 15L40 35M20 35L40 15" stroke="#000000" stroke-width="4" stroke-linecap="round"/>
                            <path fill="#000000" d="M50 25 L115 25 L115 30 L50 30 Z"></path>
                            <text x="50" y="20" fill="#000000" style="font-size: 14px; font-weight: bold;">VERTEX</text>
                            <text x="85" y="20" fill="#000000" style="font-size: 14px;">TENNIS</text>
                        </svg>
                    </div>
                </div>
                
                <div class="footer-section">
                    <h4 class="footer-heading">Raquetes</h4>
                    <ul class="footer-links">
                        <li><a href="#">Raquetes Profissionais</a></li>
                        <li><a href="#">Raquetes Iniciantes e Recreativas</a></li>
                        <li><a href="#">Raquetes Junior</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h4 class="footer-heading">Raqueteiros</h4>
                    <ul class="footer-links">
                        <li><a href="#">Mochilas</a></li>
                        <li><a href="#">Bolsas</a></li>
                        <li><a href="#">Grips</a></li>
                        <li><a href="#">Overgrips</a></li>
                        <li><a href="#">Fitas Protetoras</a></li>
                        <li><a href="#">Cordas</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h4 class="footer-heading">Vestuário</h4>
                    <ul class="footer-links">
                        <li><a href="#">Camisas e Polos</a></li>
                        <li><a href="#">Chapéus e Viseiras</a></li>
                        <li><a href="#">Faixas e Munhequeiras</a></li>
                        <li><a href="#">Tênis</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h4 class="footer-heading">Sobre nós</h4>
                    <ul class="footer-links">
                        <li><a href="#">Quem somos</a></li>
                        <li><a href="#">Contato</a></li>
                        <li><a href="#">Blog</a></li>
                    </ul>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
elif page == "Power BI":
    st.markdown(
        """
        <div class="content-section">
            <h2>Relatório Power BI</h2>
            
            <div class="powerbi-container">
                Aqui será exibido o relatório do Power BI
            </div>
            
            <div class="analysis-section">
                <h3 class="analysis-title">Análises Extraídas</h3>
                
                <div class="analysis-card">
                    <strong>Análise 1:</strong> Insight sobre o desempenho dos jogadores.
                </div>
                
                <div class="analysis-card">
                    <strong>Análise 2:</strong> Dados de performance em torneios.
                </div>
                
                <div class="analysis-card">
                    <strong>Análise 3:</strong> Considerações sobre evolução dos rankings.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
elif page == "Guia de Implementação":
    st.markdown(
        """
        <div class="content-section">
            <h2>Guia de Implementação do Power BI</h2>
            
            <div style="background-color: var(--card-bg); padding: 24px; border-radius: 8px; margin-top: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <h3 style="margin-bottom: 16px;">Passo a Passo</h3>
                <ol style="margin-left: 20px; margin-bottom: 24px;">
                    <li style="margin-bottom: 12px;"><strong>Configuração do Ambiente:</strong> Prepare os recursos necessários.</li>
                    <li style="margin-bottom: 12px;"><strong>Publicação do Relatório:</strong> Utilize o 'Publish to Web' ou Power BI Embedded.</li>
                    <li style="margin-bottom: 12px;"><strong>Integração:</strong> Incorpore o relatório no app.</li>
                    <li><strong>Validação:</strong> Teste e valide as informações apresentadas.</li>
                </ol>
                <p>Este guia tem o objetivo de orientar na implementação do Power BI de forma prática e eficiente.</p>
            </div>
            
            <div class="divider"></div>
            
            <h3>Download do Guia</h3>
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
