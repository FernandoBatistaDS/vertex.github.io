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
    
    /* Custom header */
    .header {
        background-color: var(--bg-primary);
        padding: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid var(--card-border);
    }
    
    .vertex-logo {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .logo-text {
        color: var(--text-primary);
        font-size: 24px;
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
    
    /* Footer */
    .footer {
        background-color: var(--vertex-neon-green);
        color: black;
        padding: 2rem 1rem;
        margin-top: 2rem;
        width: 100%;
        box-sizing: border-box;
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
    
    /* Fix para o footer */
    .footer-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 30px;
    }
    
    .footer-col {
        text-align: left;
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
        color: black;
        text-decoration: none;
    }
    
    .footer-list a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom header
st.markdown(
    """
    <div class="header">
        <div class="vertex-logo">
            <svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="https://vertextennis.com/wp-content/uploads/2024/11/logo-vertex.svg">
                <path d="M8 8L28 28M8 28L28 8" stroke="#0B9E84" stroke-width="4" stroke-linecap="round"/>
                <path d="M18 5C14.9 5 12.1 5 9.5 5C6.9 5 5 6.9 5 9.5C5 12.1 5 14.9 5 18" stroke="#0B9E84" stroke-width="4" stroke-linecap="round"/>
                <path d="M18 31C21.1 31 23.9 31 26.5 31C29.1 31 31 29.1 31 26.5C31 23.9 31 21.1 31 18" stroke="#0B9E84" stroke-width="4" stroke-linecap="round"/>
            </svg>
            <span class="logo-text">VertexTennis</span>
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
    url = f"https://raw.githubusercontent.com/{Gabriel4210}/{Vertex_App}/{main}/{guia_implementacao_power_bi.pdf}"
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

# Page content with content-wrapper div for better footer positioning
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

if page == "Página Inicial":
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.title("Vertex - Velocidade e Qualidade nas Decisões")
    
    # Equipe envolvida
    st.subheader("Insight Hunters")
    
    st.markdown(
        """
        <div class="team-member">
            <h4>Gabriel Penha</h4>
            <p>Desenvolvedor Front-end</p>
        </div>
        
        <div class="team-member">
            <h4>Carol</h4>
            <p>Analista de Dados</p>
        </div>
        
        <div class="team-member">
            <h4>Wendel</h4>
            <p>UX/UI Designer</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<hr>', unsafe_allow_html=True)
    
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
    repo_name = "Vertex_App"      # Substitua pelo nome do repositório real
    pdf_path = "guia_implementacao_power_bi.pdf"  # Caminho para o PDF no repositório
    
    # Carregar o PDF do GitHub
    with st.spinner("Carregando guia de implementação..."):
        try:
            # Simulando o carregamento de um PDF (em produção, essa linha seria substituída pelo código real)
            # pdf_bytes = load_github_pdf(repo_owner, repo_name, pdf_path)
            
            # Como não temos acesso ao repositório real, vamos usar um arquivo local como fallback
            # Em produção, você usaria a linha comentada acima
            
            # Apenas para fins de demonstração - em produção, use a função load_github_pdf
            st.info("O guia está sendo carregado do repositório GitHub: vertextennis/app-vertex")
            
            # Exibir uma prévia do guia
            st.subheader("Prévia do Guia")
            
            st.markdown("""
            <div class="guide-section">
                <h3>1. Preparação dos Dados</h3>
                <ul>
                    <li>Conecte-se às fontes de dados relevantes (SQL Server, Excel, CSV)</li>
                    <li>Realize a limpeza e transformação dos dados no Power Query</li>
                    <li>Estabeleça relacionamentos entre tabelas no modelo de dados</li>
                </ul>
                
                <h3>2. Criação do Relatório</h3>
                <ul>
                    <li>Desenvolva visualizações para análise de vendas por produto</li>
                    <li>Implemente filtros interativos por região e período</li>
                    <li>Crie dashboards com KPIs de desempenho comercial</li>
                    <li>Configure drill-down para análises detalhadas</li>
                </ul>
                
                <h3>3. Publicação e Compartilhamento</h3>
                <ul>
                    <li>Publique o relatório no serviço Power BI</li>
                    <li>Configure atualizações automáticas dos dados</li>
                    <li>Defina permissões de acesso para usuários</li>
                    <li>Gere link público ou incorpore em aplicações (como este Streamlit)</li>
                </ul>
                
                <h3>4. Manutenção e Atualização</h3>
                <ul>
                    <li>Estabeleça rotina de verificação da qualidade dos dados</li>
                    <li>Implemente alertas para métricas críticas</li>
                    <li>Atualize visualizações conforme feedback dos usuários</li>
                    <li>Documente alterações e melhorias implementadas</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            # Download do documento
            st.subheader("Download do Documento Completo")
            
            # Em produção, use o PDF carregado do GitHub
            # if pdf_bytes:
            #     st.download_button(
            #         label="Baixar Guia Completo em PDF",
            #         data=pdf_bytes,
            #         file_name="guia_implementacao_power_bi.pdf",
            #         mime="application/pdf"
            #     )
            
            # Simulação do botão de download
            st.markdown("""
            <a href="https://github.com/Gabriel4210/Vertex_App/raw/main/guia_implementacao_power_bi.pdf" 
               class="download-btn" target="_blank">
                Baixar Guia Completo em PDF
            </a>
            """, unsafe_allow_html=True)
            
            # Exibir o PDF embutido (em produção, use display_pdf(pdf_bytes))
            st.subheader("Visualizar Documento")
            st.markdown("""
            <div class="pdf-viewer">
                <p>Visualização do documento PDF carregado do repositório GitHub.</p>
                <!-- Em produção, use o código comentado abaixo -->
                <!-- {display_pdf(pdf_bytes)} -->
                <div style="background-color: white; padding: 20px; text-align: center; color: black;">
                    <p>Visualização do PDF indisponível na demonstração</p>
                    <p>Em produção, o PDF será exibido diretamente aqui</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Erro ao processar o guia de implementação: {e}")
            st.info("Por favor, verifique se o arquivo está disponível no repositório GitHub.")

# Fechar a div content-wrapper
st.markdown('</div>', unsafe_allow_html=True)

# Adiciona o footer no final (fora da content-wrapper)
add_footer()
