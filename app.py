import streamlit as st
import io
from reportlab.pdfgen import canvas

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
    </style>
    """,
    unsafe_allow_html=True
)

# Custom header
st.markdown(
    """
    <div class="header">
        <div class="vertex-logo">
            <svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
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
page = st.sidebar.radio("", ("Apresentação da Entrega", "Power BI", "Guia de Implementação"))

# Footer function
def add_footer():
    st.markdown(
        """
        <div class="footer">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 30px;">
                <div>
                    <h4>VertexTennis</h4>
                    <p>Soluções inovadoras para tênis</p>
                </div>
                
                <div>
                    <h4>Contato</h4>
                    <p>contato@vertextennis.com</p>
                    <p>+55 11 5555-5555</p>
                </div>
                
                <div>
                    <h4>Sobre nós</h4>
                    <ul style="list-style-type: none; padding: 0;">
                        <li><a href="#" style="color: black; text-decoration: none;">Quem somos</a></li>
                        <li><a href="#" style="color: black; text-decoration: none;">Contato</a></li>
                        <li><a href="#" style="color: black; text-decoration: none;">Blog</a></li>
                    </ul>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Page content
if page == "Apresentação da Entrega":
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.title("Apresentação da Entrega")
    
    # Equipe envolvida
    st.subheader("Equipe Envolvida")
    
    st.markdown(
        """
        <div class="team-member">
            <h4>João Silva</h4>
            <p>Desenvolvedor Front-end</p>
        </div>
        
        <div class="team-member">
            <h4>Maria Oliveira</h4>
            <p>Analista de Dados</p>
        </div>
        
        <div class="team-member">
            <h4>Carlos Santos</h4>
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
    
    # Adiciona o footer
    add_footer()
    
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
    
    # Adiciona o footer
    add_footer()
    
elif page == "Guia de Implementação":
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.title("Guia de Implementação do Power BI")
    
    # Guia em markdown
    st.markdown("## Passo a Passo para Implementação")
    
    # Usando o st.code para exibir o código HTML corretamente
    st.code("""<h1>1. Preparação dos Dados</h1>
<ul>
    <li>Conecte-se às fontes de dados relevantes (SQL Server, Excel, CSV)</li>
    <li>Realize a limpeza e transformação dos dados no Power Query</li>
    <li>Estabeleça relacionamentos entre tabelas no modelo de dados</li>
</ul>

<h2>2. Criação do Relatório</h2>
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

<h4>4. Manutenção e Atualização</h4>
<ul>
    <li>Estabeleça rotina de verificação da qualidade dos dados</li>
    <li>Implemente alertas para métricas críticas</li>
    <li>Atualize visualizações conforme feedback dos usuários</li>
    <li>Documente alterações e melhorias implementadas</li>
</ul>""", language="html")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Download do arquivo PDF
    st.subheader("Download do Guia Completo")
    
    # Cria um PDF simples para download
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont("Helvetica", 12)
    
    # Título
    p.setFont("Helvetica-Bold", 18)
    p.drawString(50, 800, "Guia de Implementação do Power BI - VertexTennis")
    p.setFont("Helvetica", 12)
    
    # Conteúdo
    y_position = 750
    
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, y_position, "1. Preparação dos Dados")
    y_position -= 20
    p.setFont("Helvetica", 12)
    
    for item in ["• Conecte-se às fontes de dados relevantes", 
                "• Realize a limpeza e transformação dos dados", 
                "• Estabeleça relacionamentos entre tabelas"]:
        p.drawString(70, y_position, item)
        y_position -= 20
    
    y_position -= 10
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, y_position, "2. Criação do Relatório")
    y_position -= 20
    p.setFont("Helvetica", 12)
    
    for item in ["• Desenvolva visualizações para análise de vendas", 
                "• Implemente filtros interativos por região e período", 
                "• Crie dashboards com KPIs de desempenho", 
                "• Configure drill-down para análises detalhadas"]:
        p.drawString(70, y_position, item)
        y_position -= 20
    
    y_position -= 10
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, y_position, "3. Publicação e Compartilhamento")
    y_position -= 20
    p.setFont("Helvetica", 12)
    
    for item in ["• Publique o relatório no serviço Power BI", 
                "• Configure atualizações automáticas dos dados", 
                "• Defina permissões de acesso para usuários", 
                "• Gere link público ou incorpore em aplicações"]:
        p.drawString(70, y_position, item)
        y_position -= 20
    
    p.showPage()
    p.save()
    buffer.seek(0)
    
    st.download_button(
        label="Baixar Guia Completo em PDF",
        data=buffer,
        file_name="guia_implementacao_power_bi.pdf",
        mime="application/pdf"
    )
    
    # Adiciona o footer
    add_footer()
