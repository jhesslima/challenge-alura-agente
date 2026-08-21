import streamlit as st
import pandas as pd
from pypdf import PdfReader
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente (útil para desenvolvimento local)
load_dotenv()

st.set_page_config(
    page_title="Agente de IA - Challenge Alura",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Agente Inteligente - Challenge Alura")
st.write("Faça o upload de um documento PDF ou CSV e converse com ele utilizando o poder do Google Gemini!")

# Barra lateral para configuração da API Key
st.sidebar.header("⚙️ Configurações")
api_key = st.sidebar.text_input("Insira sua Gemini API Key:", type="password", value=os.getenv("GEMINI_API_KEY", ""))

if not api_key:
    st.sidebar.warning("⚠️ Você precisa inserir uma API Key do Gemini para usar o agente conversacional.")
else:
    genai.configure(api_key=api_key)

# Componente de upload de arquivos
st.sidebar.subheader("📂 Upload do Documento")
uploaded_file = st.sidebar.file_uploader("Escolha um arquivo PDF ou CSV", type=["pdf", "csv"])

# Função para extrair texto do PDF
def extract_text_from_pdf(file):
    try:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception as e:
        st.error(f"Erro ao ler o PDF: {e}")
        return None

# Função para ler o CSV
def extract_text_from_csv(file):
    try:
        df = pd.read_csv(file)
        text = "Estrutura do CSV:\n"
        text += f"Colunas: {', '.join(df.columns)}\n\n"
        text += "Amostra dos Dados:\n"
        text += df.head(50).to_string() # Limita a 50 linhas para evitar estourar limites de contexto simples
        return text
    except Exception as e:
        st.error(f"Erro ao ler o CSV: {e}")
        return None

document_context = ""

if uploaded_file is not None:
    st.info(f"Arquivo carregado com sucesso: **{uploaded_file.name}**")
    
    if uploaded_file.name.endswith('.pdf'):
        with st.spinner("Processando e extraindo textos do PDF..."):
            document_context = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith('.csv'):
        with st.spinner("Lendo e estruturando dados do CSV..."):
            document_context = extract_text_from_csv(uploaded_file)
            
    if document_context:
        st.success("✅ Documento processado e pronto para consultas!")
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Exibe mensagens anteriores
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # Entrada do usuário
        if prompt := st.chat_input("Pergunte algo sobre o seu documento..."):
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            if not api_key:
                st.error("Por favor, insira sua API Key na barra lateral esquerda antes de enviar uma mensagem.")
            else:
                with st.chat_message("assistant"):
                    with st.spinner("O agente está analisando o documento..."):
                        try:
                            # Prompt do sistema para garantir ancoragem (grounding)
                            system_instruction = (
                                "Você é o Agente Inteligente do Challenge Alura. Seu objetivo é responder a perguntas de forma precisa "
                                "utilizando estritamente as informações contidas no documento fornecido abaixo.\n"
                                "Se a resposta não puder ser encontrada ou deduzida a partir do documento, diga de forma educada "
                                "que não encontrou essa informação no arquivo fornecido e que está limitado às informações dele.\n\n"
                                f"--- INÍCIO DO DOCUMENTO ---\n{document_context}\n--- FIM DO DOCUMENTO ---"
                            )
                            
                            model = genai.GenerativeModel("gemini-1.5-flash")
                            
                            chat_history_str = ""
                            for m in st.session_state.messages[:-1]:
                                chat_history_str += f"{m['role'].capitalize()}: {m['content']}\n"
                            
                            full_prompt = f"{system_instruction}\n\nHistórico da Conversa:\n{chat_history_str}\nUser: {prompt}\nAssistant:"
                            
                            response = model.generate_content(full_prompt)
                            response_text = response.text
                            
                            st.markdown(response_text)
                            st.session_state.messages.append({"role": "assistant", "content": response_text})
                            
                        except Exception as e:
                            st.error(f"Erro ao gerar resposta com o Gemini: {e}")
else:
    st.warning("👈 Por favor, carregue um arquivo PDF ou CSV na barra lateral para começar.")
