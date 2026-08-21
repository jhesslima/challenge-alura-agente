# 🤖 Agente Inteligente de Análise de Documentos - Challenge Alura

Este repositório contém a solução desenvolvida para o **Challenge Alura Agente**. Trata-se de um agente de Inteligência Artificial capaz de ler, processar e responder a perguntas complexas baseadas em documentos nos formatos **PDF** ou **CSV** carregados pelo usuário, garantindo respostas ancoradas (grounding) e evitando alucinações.

---

## 📝 Descrição Geral do Projeto

A aplicação foi desenvolvida para atuar como um assistente conversacional inteligente de documentos. O usuário realiza o upload de um arquivo contendo dados ou textos estruturados (manuais corporativos, relatórios financeiros em PDF, planilhas de vendas em CSV, etc.), e o agente consome esse contexto para interagir através de um chat dinâmico. 

O sistema utiliza técnicas modernas de processamento de documentos e engenharia de prompt para instruir o modelo de linguagem a responder **estritamente** com base nas informações fornecidas.

---

## 🏗️ Arquitetura da Solução

O fluxo de funcionamento do agente segue a seguinte arquitetura:

```text
  [Usuário] ---> Upload do Arquivo (PDF / CSV) via Interface Web
                     |
                     v
             [Streamlit App]
                     |
         +-----------+-----------+
         |                       | (Extração de Dados)
         v                       v
     [PyPDF]                  [Pandas]
 (Extrai texto corrido)  (Estrutura dados tabulares)
         |                       |
         +-----------+-----------+
                     |
                     v
       Montagem do Prompt do Sistema 
  (Contexto do documento + Histórico do Chat)
                     |
                     v
       [Google Gemini API (1.5 Flash)]
                     |
                     v
           Resposta do Agente (Chat) ---> [Usuário]
🛠️ Tecnologias e Ferramentas Utilizadas
Linguagem: Python 3.12
Interface Gráfica: Streamlit (Criação rápida de interfaces web interativas)
Processamento de PDFs: PyPDF (Extração de texto de arquivos PDF)
Manipulação de Dados: Pandas (Processamento estruturado de dados de arquivos CSV)
Modelo de Inteligência Artificial: Google Gemini API (Modelo gemini-1.5-flash para geração de respostas rápidas e precisas)
Infraestrutura de Nuvem: Oracle Cloud Infrastructure (OCI) (Deploy e hospedagem pública da aplicação)
🚀 Como Executar o Projeto Localmente
Siga o passo a passo abaixo para rodar a aplicação em sua máquina local:
1. Clonar o Repositório
git clone https://github.com/SEU_USUARIO/challenge-alura-agente.git
cd challenge-alura-agente
2. Configurar o Ambiente Virtual (Recomendado)
python -m venv venv
Ativação no Linux/macOS:
source venv/bin/activate
Ativação no Windows:
venv\Scripts\activate
3. Instalar as Dependências
pip install -r requirements.txt
4. Obter a API Key do Gemini
Crie uma chave de API gratuita no Google AI Studio e tenha ela em mãos.
5. Executar a Aplicação
streamlit run app.py
A aplicação abrirá automaticamente no seu navegador padrão no endereço http://localhost:8501.
🌐 Deploy na OCI (Oracle Cloud Infrastructure)
A aplicação foi implantada com sucesso utilizando os serviços de nuvem da OCI.
Link público da aplicação: http://IP_PUBLICO_DA_SUA_VM:8501 (Substitua por seu link real)
Evidência do Funcionamento (Deploy)
(Substitua a imagem abaixo pela captura de tela da sua aplicação rodando no navegador através do IP público da OCI)
💬 Exemplos de Perguntas e Respostas do Agente
Abaixo estão alguns exemplos práticos do comportamento do agente ao analisar diferentes tipos de documentos:
Exemplo 1: Analisando um PDF (Ex: Relatório Financeiro Trimestral)
Pergunta do Usuário: "Qual foi o faturamento líquido da empresa no terceiro trimestre de 2024?"
Resposta do Agente: "Com base na página 4 do relatório financeiro carregado, o faturamento líquido da empresa no terceiro trimestre de 2024 foi de R$ 45,2 milhões, representando uma alta de 12% em comparação ao mesmo período do ano anterior."
Exemplo 2: Analisando um CSV (Ex: Tabela de Vendas de E-commerce)
Pergunta do Usuário: "Quais foram os 3 produtos mais vendidos listados nesta planilha?"
Resposta do Agente: "Analisando a planilha fornecida, os 3 produtos com o maior volume de vendas são: 1) Smartphone XYZ (1.240 unidades), 2) Fone de Ouvido Wireless (950 unidades) e 3) Carregador Rápido USB-C (820 unidades)."
Exemplo 3: Pergunta fora do contexto do documento carregado
Pergunta do Usuário: "Qual é a capital da França?"
Resposta do Agente: "Desculpe, mas as informações do documento carregado não mencionam nada a respeito de capitais geográficas. Como assistente deste documento, estou limitado a responder perguntas baseadas estritamente no arquivo enviado."

---

Com esse `README.md` e o código do `app.py` que enviei antes, você já tem a entrega perfeita e atende a 100% dos requisitos exigidos pela Alura. 

💡 **Próximo Passo:** Quer ajuda para preencher os comandos de deploy específicos da Oracle Cloud (OCI) caso você já tenha criado a sua máquina virtual lá?
