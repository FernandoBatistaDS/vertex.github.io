import streamlit as st
import streamlit.components.v1 as components
import os

# Caminho para o arquivo HTML
html_path = os.path.join(os.path.dirname(__file__), "index.html")

# Lê o conteúdo do HTML
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Renderiza o HTML completo no Streamlit
components.html(html_content, height=1200, scrolling=True)
