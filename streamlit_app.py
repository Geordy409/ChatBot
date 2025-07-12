# Imports pour streamlit
import streamlit as st 
from langchain_community.callbacks import StreamlitCallbackHandler

# Imports pour le modèle 
from langchain.agents import AgentExecutor,create_react_agent #créer un agent basé sur react
from langchain_community.tools import (
    DuckDuckGoSearchRun,
    WikipediaQueryRun,
    ArxivQueryRun,
    WolframAlphaQueryRun
)
from langchain_community.utilities import (
    WikipediaAPIWrapper,
    WolframAlphaAPIWrapper  # Ajout de l'API Wrapper
) # API pour interroger Wikipedia 
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain import hub

import os 
from dotenv import load_dotenv

load_dotenv()
def setup_environment():
    groq_key = os.getenv("GROQ_API_KEY")
    wolfram_key = os.getenv("WOLFRAM_ALPHA_APPID")
    
    if not groq_key:
        st.error("Clé GROQ_API_KEY manquante")
        return False
    if not wolfram_key:
        st.error("Clé WOLFRAM_ALPHA_APPID manquante")
        return False
    
    return True
# CREATION DE L'AGENT DE GROQ

def load_agent() -> AgentExecutor:
    setup_environment()
    
    #Initialisation de modèle
    
    llm = ChatGroq(
            temperature=0,
            model="llama-3.1-8b-instant",
            streaming=True,  # Permet l'affichage en temps réel
            max_tokens=1000,
            max_retries=2,  # Ajout de retry
            request_timeout=30  # Timeout pour éviter les blocages
        )
    
    # Initialisations de outils
    tools = [
            DuckDuckGoSearchRun(
                name="web_search",
                description="Recherche d'informations récentes sur le web"
            ),
            WikipediaQueryRun(
                api_wrapper=WikipediaAPIWrapper(
                    lang = "fr",
                    top_k_results=3,
                    doc_content_chars_max=1500
                ),
                name="wikipedia",
                description="Recherche d'informations encyclopédiques"
            ),
            ArxivQueryRun(
                name="arxiv_search",
                description="Recherche d'articles scientifiques sur ArXiv"
            ),
            WolframAlphaQueryRun(
                api_wrapper=WolframAlphaAPIWrapper(),
                name="wolfram_alpha",
                description="Calculs mathématiques, conversions, données scientifiques et factuelles. Utilisez pour: équations, statistiques, unités, dates, géographie, etc."
            )
        ]
    # Definissons le prompt: le prompt ReACT
    try:
        prompt = hub.pull("hwchase17/react")
    except Exception as e:
        st.error(f"Erreur de configuration : {e}")
        return None
        
    # création de l'agent
    agent = create_react_agent(llm, tools, prompt)
    
    return AgentExecutor(
        agent = agent,
        tools = tools,
        verbose = True,
        handle_parsing_errors = True,
        max_iterations = 5,
        max_execution_time = 30
    )

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Assistant IA avec Recherche",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Titre principal
st.title("🤖 Assistant IA avec Recherche")
st.markdown("Assistant intelligent avec accès à la recherche web, Wikipedia, ArXiv et Wolfram Alpha")

# Sidebar avec informations
with st.sidebar:
    st.header("ℹ️ Informations")
    st.markdown("""
    **Outils disponibles :**
    - 🔍 Recherche web (DuckDuckGo)
    - 📚 Wikipedia
    - 📝 ArXiv (articles scientifiques)
    - 🧮 Wolfram Alpha (calculs)
    
    **Modèle :** Llama 3.1 8B (Groq)
    """)
    
    # Bouton pour vider l'historique
    if st.button("🗑️ Vider l'historique"):
        st.session_state.messages = []
        st.rerun()

# Initialisation de l'état de session
if "messages" not in st.session_state:
    st.session_state.messages = []

if "agent" not in st.session_state:
    with st.spinner("Chargement de l'agent..."):
        st.session_state.agent = load_agent()
        if st.session_state.agent is None:
            st.error("Impossible de charger l'agent. Vérifiez vos clés API.")
            st.stop()

# Affichage des messages existants
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Zone de saisie pour les nouveaux messages
if prompt := st.chat_input("Posez votre question..."):
    # Ajout du message utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Affichage du message utilisateur
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Génération et affichage de la réponse
    with st.chat_message("assistant"):
        # Conteneur pour le callback Streamlit
        st_callback = StreamlitCallbackHandler(st.container())
        
        # Placeholder pour la réponse
        response_placeholder = st.empty()
        
        try:
            # Exécution de l'agent avec callback
            with st.spinner("Recherche en cours..."):
                response = st.session_state.agent.invoke(
                    {"input": prompt},
                    {"callbacks": [st_callback]}
                )
            
            # Affichage de la réponse finale
            full_response = response.get("output", "Désolé, je n'ai pas pu générer une réponse.")
            response_placeholder.markdown(full_response)
            
            # Sauvegarde de la réponse dans l'historique
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            error_message = f"Erreur lors de la génération de la réponse : {str(e)}"
            response_placeholder.error(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})

# # Affichage du statut en bas de page
# st.markdown("---")
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.metric("Messages", len(st.session_state.messages))
# with col2:
#     st.metric("Agent", "✅ Actif" if st.session_state.get("agent") else "❌ Inactif")
# with col3:
#     st.metric("Outils", "4 disponibles")

    
    
    
    
