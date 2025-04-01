import streamlit as st
import requests
import base64

# Configuração do app
st.set_page_config(page_title="App VertexTennis", layout="wide")

# CSS com variáveis de identidade, ajustes e background para o conteúdo
st.markdown(
    """
    <style>
    /* Variáveis de cores e identidade visual */
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
    
    .stApp {
        background-color: var(--bg-primary);
    }
    
    /* Header */
    .header {
        background: linear-gradient(135deg, var(--vertex-brand-green), #004f3a);
        padding: 1.5rem 2rem;
        display: flex;
        align-items: center;
        border-bottom: 2px solid var(--card-border);
        width: 100%;
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
    
    /* Seções de conteúdo padrão */
    .content-section {
        padding: 2rem 1rem;
        background-color: var(--bg-primary);
    }
    
    h1, h2, h3, h4, h5 {
        color: var(--text-primary);
    }
    
    /* Seção específica para Relatório Power BI */
    .pbi-section {
        background-color: #FFFFFF; /* Fundo branco */
        color: #000000;            /* Fonte preta */
        padding: 2rem 1rem;
        border-radius: 8px;
        margin: 20px 0;
    }
    
    /* Vídeo */
    .video-container {
        background-color: var(--card-bg);
        border-radius: 8px;
        padding: 20px;
        margin: 20px 0;
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
    
    /* Equipe */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 10px;
        margin-top: 20px;
    }
    
    .team-member {
        background-color: var(--card-bg);
        padding: 10px;
        border-radius: 8px;
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
    
    /* Guia de Implementação */
    .guide-section {
        background-color: var(--card-bg);
        padding: 20px;
        border-radius: 8px;
        margin: 20px 0;
    }
    
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
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown(
    """
    <div class="header">
        <div class="vertex-logo">
            <img src="https://vertextennis.com/wp-content/uploads/2024/11/logo-vertex.svg" alt="Logo VertexTennis">
            <h4> Implantação PBI Comercial - Vertex </h4>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Container principal para todo o conteúdo
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# ──────────────── Seção 1: Introdução (mantém o background padrão) ────────────────
st.markdown('<div class="content-section" id="introducao">', unsafe_allow_html=True)
st.title("Transformando seus Dados em Decisões")
st.subheader("Introdução")
st.markdown("""
Na Vertex Tennis, dados se tornam decisões estratégicas que impulsionam o desempenho e a inovação.  
Com o objetivo de darmos mais um passo e melhorar ainda mais essa realidade, estamos implementando o Power BI como uma nova ferramenta no fluxo.

## Estrutura do Site  

Nesse site você encontrará as principais informações sobre uso, insights, manutenção e governança, organizado nos seguintes módulos:  

- **Introdução**: Uma breve descrição do objetivo da implantação com um vídeo explicativo.  
- **Dashboard**: Exibe informações principais e métricas relevantes, além de apresentar uma lista de insights logo abaixo.  
- **Guia de Implementação**: Toda a explicação relacionada às licenças necessárias, suporte e manutenção da ferramenta.  

No caso de alguma dúvida específica, não hesite em entrar em contato com nossa equipe.
""")
st.markdown('</div>', unsafe_allow_html=True)

# ──────────────── Seção 2: Relatório Power BI (fundo branco e fonte preta) ────────────────
st.markdown('<div class="pbi-section" id="pbi">', unsafe_allow_html=True)
st.title("Relatório Power BI")
st.subheader("Faça suas análises")
st.markdown(
    """
    <div style="background-color: var(--card-bg); padding: 20px; border-radius: 8px; margin: 20px 0;">
        <iframe width="100%" height="600" 
            src="https://app.powerbi.com/view?r=eyJrIjoiOGIzOGI0ZjEtMDM2Mi00OWIyLTkxNDgtOWE5YmMyYzM0NGNlIiwidCI6ImRmNzFmNmJiLWUzY2MtNGY1Yi1iNTMyLTc5ZGUyNjFiNTFhMiJ9" 
            frameborder="0" 
            allowFullScreen="true">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)
st.subheader("Insights Extraídos")
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
st.markdown('</div>', unsafe_allow_html=True)

# ──────────────── Seção 3: Guia de Implementação ────────────────
st.markdown('<div class="content-section" id="guia">', unsafe_allow_html=True)
st.title("Guia de Implementação")

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

repo_owner = "Gabriel4210"
repo_name = "Vertex_App"
pdf_path = "guia_implementacao_power_bi.pdf"

st.subheader("Visualizar Documento")
try:
    pdf_bytes = load_github_pdf(repo_owner, repo_name, pdf_path)
    if pdf_bytes:
        st.markdown(display_pdf(pdf_bytes), unsafe_allow_html=True)
    else:
        st.info("PDF indisponível no momento.")
except Exception as e:
    st.error(f"Erro ao processar o guia de implementação: {e}")
    st.info("Por favor, verifique se o arquivo está disponível no repositório GitHub.")

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

st.markdown('</div>', unsafe_allow_html=True)
