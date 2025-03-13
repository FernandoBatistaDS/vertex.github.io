import streamlit as st
import requests
import io
import base64
from pathlib import Path

# App configuration
st.set_page_config(page_title="App VertexTennis", layout="wide")

# CSS com o estilo da VertexTennis
st.markdown(
    """
    <style>
    /* Custom colors */
    :root {
        --vertex-brand-green: #0B9E84;
        --vertex-neon-green: #9AFF02;
        --vertex-teal: #007273;
        --vertex-red: #C44D30;
        --bg-primary: #1E1E1E;
        --bg-secondary: #2D2D2D;
        --text-primary: #FFFFFF;
        --text-secondary: #CCCCCC;
        --card-bg: #2D2D2D;
        --card-border: #3D3D3D;
    }
    
    /* Base styles */
    .main {
        background-color: var(--bg-primary);
        color: var(--text-primary);
    }
    
    .stApp {
        background-color: var(--bg-primary);
    }
    
    /* HEADER */
    .header {
        /* Pode manter var(--bg-primary) ou usar um gradiente leve */
        background: linear-gradient(135deg, var(--bg-primary), #333);
        padding: 1rem 2rem;
        display: flex;
        align-items: center;
        border-bottom: 1px solid var(--card-border);
    }
    
    /* Logo e título */
    .header .vertex-logo {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .header .vertex-logo img {
        width: 48px;
        height: 48px;
        object-fit: contain;
    }
    .header .logo-text {
        color: var(--text-primary);
        font-size: 28px;
        font-weight: bold;
    }
   
    /* Content styles */
    .content-section {
        padding: 2rem 1rem;
        background-color: var(--bg-primary);
    }
    
    h1, h2, h3, h4, h5 {
        color: var(--text-primary);
    }
    
    /* Analysis cards */
    .analysis-card {
        background-color: var(--card-bg);
        border-left: 4px solid var(--vertex-brand-green);
        color: var(--text-primary);
        padding: 1rem;
        border-radius: 4px;
        margin-bottom: 1rem;
    }
    
    /* FOOTER */
    .footer {
        /* Se quiser manter o neon verde, podemos suavizar com um gradiente */
        background: linear-gradient(135deg, var(--vertex-neon-green), #c0ff77);
        color: #000;
        padding: 2rem 0;
        margin-top: 2rem;
        width: 100%;
        box-sizing: border-box;
    }
    
    /* Grid interno do footer */
    .footer-grid {
        max-width: 1200px;       /* Para limitar a largura máxima e centralizar */
        margin: 0 auto;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 30px;
        padding: 0 1rem;         /* Espaçamento lateral */
    }
    
    /* Colunas e listas */
    .footer-col h4 {
        margin-bottom: 10px;
    }
    .footer-list {
        list-style-type: none;
        padding: 0;
        margin: 0;
    }
    .footer-list li {
        margin-bottom: 8px;
    }
    .footer-list a {
        color: #000;
        text-decoration: none;
    }
    .footer-list a:hover {
        text-decoration: underline;
    }
    
    /* Hide Streamlit elements */
    #MainMenu, footer {
        visibility: hidden;
    }
    
    div.block-container {
        padding-top: 1rem;
    }

    /* Video container */
    .video-container {
        background-color: var(--card-bg);
        border-radius: 8px;
        padding: 20px;
        margin: 20px 0;
    }

    /* Team members */
    .team-member {
        background-color: var(--card-bg);
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
        border-left: 4px solid var(--vertex-brand-green);
    }

    /* Guide section */
    .guide-section {
        background-color: var(--card-bg);
        padding: 20px;
        border-radius: 8px;
        margin: 20px 0;
    }
    
    /* Code blocks */
    pre {
        background-color: #1A1A1A;
        border-radius: 4px;
        padding: 15px;
        overflow-x: auto;
        margin: 15px 0;
        border: 1px solid var(--card-border);
    }
    
    code {
        font-family: 'Courier New', monospace;
        color: #E0E0E0;
    }

    /* Download button */
    .download-btn {
        background-color: var(--vertex-brand-green);
        color: white;
        padding: 10px 15px;
        border-radius: 4px;
        text-decoration: none;
        display: inline-block;
        margin-top: 20px;
    }
    
    /* PDF viewer */
    .pdf-viewer {
        background-color: var(--card-bg);
        border-radius: 8px;
        padding: 20px;
        margin: 20px 0;
        width: 100%;
        box-sizing: border-box;
    }
    
    iframe.pdf-frame {
        width: 100%;
        height: 600px;
        border: none;
        background-color: white;
    }
    
    /* Fix for footer spacing */
    .stApp {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
    }
    
    .content-wrapper {
        flex: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom header
st.markdown(
    """
    <div class="header">
        <div class="header">
            <div class="vertex-logo">
                <img src="https://vertextennis.com/wp-content/uploads/2024/11/logo-vertex.svg" width="36" height="36" alt="Logo VertexTennis">
                <span class="logo-text">VertexTennis</span>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation
st.sidebar.title("Navegação")
page = st.sidebar.radio("", ("Página Inicial", "Power BI", "Guia de Implementação"))

# Função para carregar PDF do GitHub
def load_github_pdf(repo_owner, repo_name, path_to_pdf, branch="main"):
    """Carrega PDF diretamente do GitHub"""
    url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{path_to_pdf}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.content
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao carregar arquivo do GitHub: {e}")
        return None

# Função para exibir PDF em iframe
def display_pdf(pdf_bytes):
    """Exibe um PDF usando um iframe"""
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    pdf_display = f'<iframe class="pdf-frame" src="data:application/pdf;base64,{base64_pdf}" type="application/pdf"></iframe>'
    return pdf_display

# Footer function - Fixed version
def add_footer():
    st.markdown(
        """
        <div class="footer">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>VertexTennis</h4>
                    <p>Soluções inovadoras para tênis</p>
                </div>
                
                <div class="footer-col">
                    <h4>Contato</h4>
                    <p>contato@vertextennis.com</p>
                    <p>+55 11 5555-5555</p>
                </div>
                
                <div class="footer-col">
                    <h4>Sobre nós</h4>
                    <ul class="footer-list">
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

# Page content com content-wrapper para melhor posicionamento do footer
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

if page == "Página Inicial":
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.title("Velocidade e Qualidade nas Decisões")
    
    # Vídeo incorporado
    st.subheader("Vídeo de Apresentação")
    st.markdown(
        """
        <div class="video-container">
            <iframe width="100%" height="400" 
                src="https://www.youtube.com/embed/dQw4w9WgXcQ" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
            </iframe>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown('<hr>', unsafe_allow_html=True)
    
    # Equipe envolvida
    st.subheader("Insight Hunters")
    st.markdown(
        """
        <style>
            .grid-container {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 20px;
                margin-top: 20px;
            }
            .team-member {
                border: 1px solid #ccc;
                padding: 15px;
                border-radius: 8px;
                text-align: center;
                background: #2D2D2D; 
                color: #ffffff;
            }
            .team-member img {
                width: 100px;
                height: 100px;
                border-radius: 50%;
                object-fit: cover;
            }
            .team-member h4 {
                margin: 10px 0 5px;
            }
            .team-member a {
                text-decoration: none;
                color: #0077b5; /* Azul do LinkedIn */
            }
        </style>
        
        <div class="grid-container">
            <div class="team-member">
                <img src="https://lh3.googleusercontent.com/a/AGNmyxZ6qSVDtB856uLoGdIQJoPKY712zFFxXm9oj-xZ1g=s96-c" alt="Gabriel Penha">
                <h4>Gabriel Penha</h4>
                <p><a href="https://www.linkedin.com/in/gabriel4210" target="_blank">LinkedIn</a></p>
                <p>Telefone: (71) 99210-9164</p>
            </div>
            <div class="team-member">
                <img src="https://via.placeholder.com/100" alt="Nome 2">
                <h4>Nome 2</h4>
                <p><a href="https://www.linkedin.com/in/nome2" target="_blank">LinkedIn</a></p>
                <p>Telefone: (00) 00000-0000</p>
            </div>
            <div class="team-member">
                <img src="https://via.placeholder.com/100" alt="Nome 3">
                <h4>Nome 3</h4>
                <p><a href="https://www.linkedin.com/in/nome3" target="_blank">LinkedIn</a></p>
                <p>Telefone: (00) 00000-0000</p>
            </div>
            <div class="team-member">
                <img src="https://via.placeholder.com/100" alt="Nome 4">
                <h4>Nome 4</h4>
                <p><a href="https://www.linkedin.com/in/nome4" target="_blank">LinkedIn</a></p>
                <p>Telefone: (00) 00000-0000</p>
            </div>
            <div class="team-member">
                <img src="https://via.placeholder.com/100" alt="Nome 5">
                <h4>Nome 5</h4>
                <p><a href="https://www.linkedin.com/in/nome5" target="_blank">LinkedIn</a></p>
                <p>Telefone: (00) 00000-0000</p>
            </div>
            <div class="team-member">
                <img src="https://via.placeholder.com/100" alt="Nome 6">
                <h4>Nome 6</h4>
                <p><a href="https://www.linkedin.com/in/nome6" target="_blank">LinkedIn</a></p>
                <p>Telefone: (00) 00000-0000</p>
            </div>
            <div class="team-member">
                <img src="https://via.placeholder.com/100" alt="Nome 7">
                <h4>Nome 7</h4>
                <p><a href="https://www.linkedin.com/in/nome7" target="_blank">LinkedIn</a></p>
                <p>Telefone: (00) 00000-0000</p>
            </div>
            <div class="team-member">
                <img src="https://via.placeholder.com/100" alt="Nome 8">
                <h4>Nome 8</h4>
                <p><a href="https://www.linkedin.com/in/nome8" target="_blank">LinkedIn</a></p>
                <p>Telefone: (00) 00000-0000</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

elif page == "Power BI":
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.title("Relatório Power BI")
    
    # Link público do Power BI
    st.subheader("Dashboard Interativo")
    st.markdown(
        """
        <div style="background-color: #2D2D2D; padding: 20px; border-radius: 8px; margin: 20px 0;">
            <iframe width="100%" height="600" 
                src="https://app.powerbi.com/view?r=eyJrIjoiZTRlNzE0NGUtYTdhMi00OWVlLWEzZWEtNzg4YmZlN2JhZDRi" 
                frameborder="0" 
                allowFullScreen="true">
            </iframe>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Análises extraídas
    st.subheader("Análises Extraídas")
    st.markdown(
        """
        <div class="analysis-card">
            <h4>Desempenho por Categoria de Equipamento</h4>
            <p>As cordas da linha Titan Core apresentaram um crescimento de vendas de 27% no último trimestre, superando todas as outras categorias de produtos.</p>
        </div>
        
        <div class="analysis-card">
            <h4>Perfil dos Consumidores</h4>
            <p>O segmento de tenistas intermediários (handicap entre 3.5-4.5) representa 62% do nosso mercado, com preferência por produtos da linha Supreme Flex.</p>
        </div>
        
        <div class="analysis-card">
            <h4>Sazonalidade de Vendas</h4>
            <p>Identificamos um pico de vendas de 35% acima da média durante os meses de torneios Grand Slam, especialmente para raquetes da categoria profissional.</p>
        </div>
        
        <div class="analysis-card">
            <h4>Distribuição Geográfica</h4>
            <p>As regiões Sul e Sudeste concentram 78% das vendas, com São Paulo representando 42% do faturamento total da empresa.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

elif page == "Guia de Implementação":
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.title("Guia de Implementação do Power BI")
    
    # Parâmetros do repositório GitHub
    repo_owner = "Gabriel4210"  # Substitua pelo nome do usuário/organização real
    repo_name = "Vertex_App"     # Substitua pelo nome do repositório real
    pdf_path = "guia_implementacao_power_bi.pdf"  # Caminho para o PDF no repositório
    
    # Exibir PDF embutido
    try:
        pdf_bytes = load_github_pdf(repo_owner, repo_name, pdf_path)
        st.subheader("Visualizar Documento")
        if pdf_bytes:
            st.markdown(display_pdf(pdf_bytes), unsafe_allow_html=True)
        else:
            st.info("PDF indisponível no momento.")
    except Exception as e:
        st.error(f"Erro ao processar o guia de implementação: {e}")
        st.info("Por favor, verifique se o arquivo está disponível no repositório GitHub.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Carregar o PDF do GitHub com spinner para download
    with st.spinner("Carregando guia de implementação..."):
        try:
            pdf_bytes = load_github_pdf(repo_owner, repo_name, pdf_path)
            st.subheader("Download do Documento Completo")
            if pdf_bytes:
                st.download_button(
                    label="Baixar Guia Completo em PDF",
                    data=pdf_bytes,
                    file_name="guia_implementacao_power_bi.pdf",
                    mime="application/pdf"
                )
        except Exception as e:
            st.error(f"Erro ao carregar o PDF: {e}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Fechar a div content-wrapper
st.markdown('</div>', unsafe_allow_html=True)

# Adiciona o footer no final (fora da content-wrapper)
add_footer()
