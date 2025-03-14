import streamlit as st
import requests
import io
import base64
from pathlib import Path

# Configuração do app
st.set_page_config(page_title="App VertexTennis", layout="wide")

# CSS atualizado conforme o Guia de Identidade Visual da Vertex
st.markdown(
    """
    <style>
    /* Variáveis de cores, fontes e identidade visual */
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
        --font-family: 'Montserrat', sans-serif;
    }
    
    body, html, .stApp {
        font-family: var(--font-family);
    }
    
    .main {
        background-color: var(--bg-primary);
        color: var(--text-primary);
    }
    
    .stApp {
        background-color: var(--bg-primary);
    }
    
    /* Header com navegação integrada */
    .header {
        background: linear-gradient(135deg, var(--vertex-brand-green), #004f3a);
        padding: 1.5rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid var(--card-border);
    }
    
    .vertex-logo {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .vertex-logo img {
        width: 48px;
        height: 48px;
        object-fit: contain;
    }
    
    .logo-text {
        color: var(--text-primary);
        font-size: 28px;
        font-weight: 700;
    }
    
    /* Navegação no header */
    .nav-menu {
        display: flex;
        gap: 2rem;
    }
    
    .nav-menu a {
        color: var(--text-primary);
        font-size: 16px;
        text-decoration: none;
        font-weight: 600;
        transition: color 0.2s;
    }
    
    .nav-menu a:hover {
        color: var(--vertex-neon-green);
    }
    
    /* Conteúdo */
    .content-section {
        padding: 2rem 1rem;
        background-color: var(--bg-primary);
    }
    
    h1, h2, h3, h4, h5 {
        color: var(--text-primary);
    }
    
    /* Cartões de análise */
    .analysis-card {
        background-color: var(--card-bg);
        border-left: 4px solid var(--vertex-brand-green);
        color: var(--text-primary);
        padding: 1rem;
        border-radius: 4px;
        margin-bottom: 1rem;
        transition: transform 0.2s;
    }
    
    .analysis-card:hover {
        transform: scale(1.02);
    }
    
    /* Footer */
    .footer {
        background: linear-gradient(135deg, var(--vertex-brand-green), #80d0c7);
        color: #000;
        padding: 2rem 0;
        margin-top: 2rem;
        width: 100%;
        box-sizing: border-box;
    }
    
    .footer-grid {
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 30px;
        padding: 0 1rem;
    }
    
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
    
    /* Container de vídeo */
    .video-container {
        background-color: var(--card-bg);
        border-radius: 8px;
        padding: 20px;
        margin: 20px 0;
    }
    
    /* Membros da equipe */
    .team-member {
        background-color: var(--card-bg);
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
        border-left: 4px solid var(--vertex-brand-green);
        text-align: center;
        transition: transform 0.2s;
        color: var(--text-primary);
    }
    
    .team-member:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
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
        color: #0077b5;
    }
    
    /* Seção do guia */
    .guide-section {
        background-color: var(--card-bg);
        padding: 20px;
        border-radius: 8px;
        margin: 20px 0;
    }
    
    /* Blocos de código */
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
    
    /* Botão de download */
    .download-btn {
        background-color: var(--vertex-brand-green);
        color: white;
        padding: 10px 15px;
        border-radius: 4px;
        text-decoration: none;
        display: inline-block;
        margin-top: 20px;
    }
    
    /* Visualizador de PDF */
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
    
    /* Layout geral para posicionamento do footer */
    .stApp {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
    }
    
    .content-wrapper {
        flex: 1;
    }
    
    /* Grade responsiva para a seção da Equipe */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header com navegação integrada
# Utilizamos colunas para posicionar o logo e o menu de navegação
col_logo, col_nav = st.columns([2,6])
with col_logo:
    st.markdown(
        """
        <div class="vertex-logo">
            <img src="https://vertextennis.com/wp-content/uploads/2024/11/logo-vertex.svg" alt="Logo VertexTennis">
            <span class="logo-text">VertexTennis</span>
        </div>
        """,
        unsafe_allow_html=True
    )
with col_nav:
    # Criamos o menu de navegação usando botões horizontais; o valor selecionado é armazenado em session_state
    if "page" not in st.session_state:
        st.session_state.page = "Página Inicial"
    nav = st.radio("", options=["Página Inicial", "Power BI", "Guia de Implementação"], index=["Página Inicial", "Power BI", "Guia de Implementação"].index(st.session_state.page), horizontal=True)
    st.session_state.page = nav

# Removemos a navegação lateral, pois agora ela está integrada no header

# Função para carregar PDF do GitHub
def load_github_pdf(repo_owner, repo_name, path_to_pdf, branch="main"):
    url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{path_to_pdf}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao carregar arquivo do GitHub: {e}")
        return None

# Função para exibir PDF em iframe
def display_pdf(pdf_bytes):
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    pdf_display = f'<iframe class="pdf-frame" src="data:application/pdf;base64,{base64_pdf}" type="application/pdf"></iframe>'
    return pdf_display

# Função para adicionar o footer com o novo texto
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
                    <p>Na Vertex Tennis, tudo começa com o compromisso de entender e atender as necessidades dos nossos clientes e parceiros.</p>
                    <p>Desenvolvemos nossos produtos com um foco absoluto na qualidade, tecnologia e acessibilidade, criando soluções que alavancam negócios e ampliam o alcance do tênis no Brasil.</p>
                    <p>A identidade visual da Vertex Tennis é a expressão de nossa essência: qualidade, inovação e paixão pelo tênis. Cada elemento — das cores à tipografia — foi pensado para reforçar nossa presença no mercado e garantir uma comunicação clara e impactante. A consistência no uso dessa identidade fortalece a marca e a torna reconhecível em qualquer contexto.</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Container principal para conteúdo (para melhor posicionamento do footer)
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Renderização de páginas com base na navegação integrada
if st.session_state.page == "Página Inicial":
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.title("Velocidade e Qualidade nas Decisões")
    
    # Seção de Introdução com Storytelling
    st.subheader("Introdução")
    st.markdown(
        """
        Na Vertex Tennis, transformamos dados em decisões estratégicas que impulsionam o desempenho e a inovação. Nosso compromisso com a qualidade se reflete em cada aspecto deste app – uma ferramenta desenvolvida para oferecer insights poderosos e uma experiência de navegação intuitiva.
        """
    )
    
    # Tour interativo (explicação passo a passo)
    with st.expander("Tour do App"):
        st.markdown(
            """
            **Bem-vindo ao Tour do App!**  
            Explore as seções abaixo:
            - **Página Inicial:** Resumo e apresentação geral da nova ferramenta.
            - **Dashboard Power BI:** Visualização interativa dos dados e algumas das análises provenientes dele.
            - **Guia de Implementação:** Documentação completa para impulsionar a adoção da solução e descrever os processos de governança.
            
            Navegue por cada seção e descubra como seus dados podem impulsionar seu negócio!
            """
        )
    
    # Vídeo incorporado
    st.subheader("Resumo e Apresentação")
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
    
    # Seção de Equipe Insight Hunters
    st.subheader("Equipe da Insight Hunters")
    st.markdown(
        """
        <div class="grid-container">
            <div class="team-member">
                <img src="https://lh3.googleusercontent.com/a/AGNmyxZ6qSVDtB856uLoGdIQJoPKY712zFFxXm9oj-xZ1g=s96-c" alt="Gabriel Penha">
                <h4>Gabriel Penha</h4>
                <p><a href="https://www.linkedin.com/in/gabriel4210" target="_blank">LinkedIn</a></p>
                <p>Telefone: (71) 99210-9164</p>
            </div>
            <div class="team-member">
                <img src="https://github.com/Gabriel4210/Vertex_App/blob/main/Photos/carol.jpeg?raw=true" alt="Carolina Diniz">
                <h4>Carolina Diniz</h4>
                <p><a href="https://www.linkedin.com/in/carolina-diniz-2b80701a4" target="_blank">LinkedIn</a></p>
                <p>Telefone: (31) 99238-0507</p>
            </div>
            <div class="team-member">
                <img src="https://github.com/Gabriel4210/Vertex_App/blob/main/Photos/fernando.jpeg?raw=true" alt="Fernando Batista">
                <h4>Fernando Batista</h4>
                <p><a href="https://www.linkedin.com/in/fernandobatistads" target="_blank">LinkedIn</a></p>
                <p>Telefone: (11) 98410-1047</p>
            </div>
            <div class="team-member">
                <img src="https://github.com/Gabriel4210/Vertex_App/blob/main/Photos/antonio.jpeg?raw=true" alt="Antônio Brandenberger">
                <h4>Antônio Brandenberger</h4>
                <p><a href="https://www.linkedin.com/in/antonio-brandenberger" target="_blank">LinkedIn</a></p>
                <p>Telefone: (21) 99252-2552</p>
            </div>
            <div class="team-member">
                <img src="https://github.com/Gabriel4210/Vertex_App/blob/main/Photos/matheus.jpeg?raw=true" alt="Matheus Marques">
                <h4>Matheus Marques</h4>
                <p><a href="https://www.linkedin.com/in/matheus-marques-rodrigues" target="_blank">LinkedIn</a></p>
                <p>Telefone: (31) 99172-3497</p>
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

elif st.session_state.page == "Power BI":
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.title("Relatório Power BI")
    
    # Dashboard interativo
    st.subheader("Dashboard Interativo")
    st.markdown(
        """
        <div style="background-color: var(--card-bg); padding: 20px; border-radius: 8px; margin: 20px 0;">
            <iframe width="100%" height="600" 
                src="https://app.powerbi.com/view?r=eyJrIjoiZTRlNzE0NGUtYTdhMi00OWVlLWEzZWEtNzg4YmZlN2JhZDRi" 
                frameborder="0" 
                allowFullScreen="true">
            </iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
    
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

elif st.session_state.page == "Guia de Implementação":
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.title("Guia de Implementação do Power BI")
    
    # Parâmetros do repositório GitHub
    repo_owner = "Gabriel4210"
    repo_name = "Vertex_App"
    pdf_path = "guia_implementacao_power_bi.pdf"
    
    # Exibição do PDF embutido
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
    
    # Opção de download com indicador de carregamento
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

# Fechar o container principal
st.markdown('</div>', unsafe_allow_html=True)

# Adicionar o footer
add_footer()
