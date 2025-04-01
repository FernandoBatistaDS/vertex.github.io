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
    
    /* Seções de conteúdo */
    .content-section {
        padding: 2rem 1rem;
        background-color: var(--bg-primary);
    }
    
    h1, h2, h3, h4, h5 {
        color: var(--text-primary);
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

# ──────────────── Seção 1: Introdução ────────────────
st.markdown('<div class="content-section" id="introducao">', unsafe_allow_html=True)
st.title("Transformando seus Dados em Decisões")
st.subheader("Introdução")
st.markdown("""
Na Vertex Tennis, dados se tornam decisões estratégicas que impulsionam o desempenho e a inovação. Isso não é novidade.
Com o objetivo de darmos mais um passo e melhorar ainda mais essa realidade, estamos implementando o Power BI como uma nova ferramenta no fluxo.  

## Estrutura do Site  

Nesse site você encontrará as principáis informações sobre uso, insights, manutenção e governança, organizado nos seguintes módulos:  

- **Introdução**: Uma breve descrição do objetivo da implantação com um vídeo explicativo.  
- **Dashboard**: Exibe informações principais e métricas relevantes. Além de apresentar uma lista de insghts logo abaixo.  
- **Guia de Implementação**: Toda a explicação relacionada as licenças necessárias, suporte e manutenção da ferramenta.  

No caso de alguma dúvida específica, não exite em entrar em contato com nossa equipe.
""")

# Vídeo incorporado
st.subheader("Resumo e Apresentação")
st.markdown("""
Veja aqui como é o funcionamento do relatório em Power Bi e como ele irá sanar algumas das suas principáis dores do cotidiano. 
Além disso, conheça a equipe da Insight Hunters, que estará atuando em parceria com a Vertex nessa etapa de implementação: 
""")
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

# Equipe Insight Hunters
st.subheader("Insight Hunters - Conheça nosso time:")
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
            <img src="https://github.com/Gabriel4210/Vertex_App/blob/main/Photos/felipe.jpeg?raw=true" alt="Felipe Acauã">
            <h4>Felipe Acauã</h4>
            <p><a href="http://www.linkedin.com/in/felipe-acau%C3%A3-88101021b" target="_blank">LinkedIn</a></p>
            <p>Telefone: (14) 99603-9135</p>
        </div>
        <div class="team-member">
            <img src="https://media.licdn.com/dms/image/v2/D4D03AQFrJJGgZBPrQg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1708985390534?e=1749081600&v=beta&t=XfwgWyu_AGypXeYIC8WZb6zqotvDnz9vxMXCd2GfAiQ" alt="Wendell Pedra">
            <h4>Wendell Pedra</h4>
            <p><a href="https://www.linkedin.com/in/wendellgpedra/" target="_blank">LinkedIn</a></p>
            <p>Telefone: (11) 99421-5743</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# ──────────────── Seção 2: PBI e Análises ────────────────
st.markdown('<div class="content-section" id="pbi-analises">', unsafe_allow_html=True)
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
st.subheader("Insghts Extraídos")
st.markdown(
    """
    Abaixo estão algumas das análises destacadas pelo time da Insight Hunters:
    """,
    unsafe_allow_html=True
)
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
