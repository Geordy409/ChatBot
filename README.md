# 🤖 Assistant IA avec Recherche Intelligente

**🚀 Application déployée sur Streamlit Community :** [https://chatbotapppy-n52dfbo4e5nslnae9a4ehl.streamlit.app/](https://chatbotapppy-n52dfbo4e5nslnae9a4ehl.streamlit.app/)

We Building a capable assitant and a chatBot like ChatGPT

Ce projet Streamlit permet de discuter avec un assistant IA intelligent capable de répondre à des questions en utilisant divers outils externes comme :

- 🔍 **Recherche Web (DuckDuckGo)**
- 📚 **Wikipedia**
- 📜 **ArXiv** (recherche scientifique)
- 🧪 **Wolfram Alpha** (calculs et données scientifiques)

Le modèle LLM utilisé est **LLaMA 3.1 8B** via l'API **Groq**.

## 🚀 Fonctionnalités

- Interface de **chat** fluide avec Streamlit
- Support **multitool** grâce à LangChain Agents
- Requêtes en **temps réel** avec streaming
- **Historique** des messages avec possibilité de réinitialiser
- Accès aux dernières informations grâce à DuckDuckGo
- Intégration directe avec **Wikipedia, ArXiv**, et **Wolfram Alpha**

## 🧠 Outils et API utilisées

| Outil             | Description                                           |
| ----------------- | ----------------------------------------------------- |
| **DuckDuckGo**    | Recherche web pour des infos récentes                 |
| **Wikipedia**     | Résumés encyclopédiques (langue : français)           |
| **ArXiv**         | Recherche d'articles scientifiques                    |
| **Wolfram Alpha** | Calculs, conversions, formules, données scientifiques |

## 🧑‍💻 Technologies utilisées

- `LangChain`
- `langchain_community`
- `langchain_groq`
- `Streamlit`
- `Python 3.10+`
- `.env` pour gérer les clés API

## 🔧 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/votre-username/assistant-ia-recherche.git
cd assistant-ia-recherche
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configuration des clés API

Créez un fichier `.env` à la racine du projet :

```env
GROQ_API_KEY=your_groq_api_key_here
WOLFRAM_ALPHA_APPID=your_wolfram_alpha_key_here
```

#### Obtenir les clés API :

- **Groq API** : [https://console.groq.com/keys](https://console.groq.com/keys)
- **Wolfram Alpha** : [https://developer.wolframalpha.com/](https://developer.wolframalpha.com/)

## 🚀 Lancement

```bash
streamlit run streamlit_app.py
```

L'application sera accessible à l'adresse : `http://localhost:8501`

## 📋 Requirements (Optionel si vous exéccuté tous dans votre venv)

```txt
streamlit
langchain
langchain-community
langchain-groq
python-dotenv
duckduckgo-search
wikipedia
arxiv
wolframalpha
```

## 🎯 Utilisation

1. **Lancez l'application** avec la commande ci-dessus ou **testez directement** l'application déployée : [https://chatbotapppy-n52dfbo4e5nslnae9a4ehl.streamlit.app/](https://chatbotapppy-n52dfbo4e5nslnae9a4ehl.streamlit.app/)
2. **Posez vos questions** dans le chat
3. **L'assistant utilisera automatiquement** les outils appropriés :
   - Questions récentes → DuckDuckGo
   - Sujets encyclopédiques → Wikipedia
   - Recherche scientifique → ArXiv
   - Calculs/formules → Wolfram Alpha

## 🌐 Déploiement

### Sur Streamlit Community Cloud

L'application est déployée et accessible à l'adresse : [https://chatbotapppy-n52dfbo4e5nslnae9a4ehl.streamlit.app/](https://chatbotapppy-n52dfbo4e5nslnae9a4ehl.streamlit.app/)

- Il se peut que la Clé GROQ ne soit plus valide car -valide et gratuite toutes les 24H, donc elle est à -renouveler par jour

### Variables d'environnement (Secrets)

Dans les paramètres de votre Space, ajoutez :

- `GROQ_API_KEY`
- `WOLFRAM_ALPHA_APPID`

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche pour votre feature
3. Commit vos changements
4. Ouvrir une Pull Request

⭐ **N'hésitez pas à laisser une étoile si ce projet vous a été utile !**

