![GeminiSQL](https://socialify.git.ci/vivek-2567/GeminiSQL/image?font=Raleway&name=1&owner=1&theme=Dark)

Built an AI-powered application that allows users to ask natural language questions about a database and get accurate SQL queries and results instantly. The system uses LangChain to orchestrate query generation, Google Gemini as the LLM for reasoning, HuggingFace embeddings for semantic understanding, and Chroma vector store for context retrieval. A Streamlit web app serves as the user interface for smooth interaction.

## Project Screenshot
![Project Screenshot](/uploads/project.png?raw=true)

## Features
- Conversational NL→SQL over a MySQL schema
- Google Gemini through `langchain-google-genai`
- Few‑shot example selection with Chroma + `sentence-transformers`
- Shows both the final SQL query and the computed answer
- Streamlit UI with example tables (T‑Shirt inventory, Discounts)

## How it works
- Prompting: Few‑shot prompt assembled with `SemanticSimilarityExampleSelector` using examples from `few_shots.py`
- Vector store: `Chroma` built from curated examples (all‑MiniLM‑L6‑v2 embeddings)
- LLM: `ChatGoogleGenerativeAI` (Gemini) plans SQL and reasoning
- SQL execution: `SQLDatabaseChain` runs the generated SQL against MySQL and returns intermediate steps
- UI: `main.py` renders the result and the final SQL

## Tech Stack
- Python, Streamlit
- LangChain, langchain-google-genai, langchain-experimental, langchain-community
- ChromaDB, sentence-transformers
- MySQL (via `pymysql`)

## Setup
### 1) Install
```bash
git clone <your-repo-url>
cd SQL
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Environment
Create a `.env` in the project root:
```env
Google_API_Key=YOUR_GOOGLE_API_KEY
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_NAME=atliq_tshirts
```

### 3) Database
The app expects two tables: `t_shirts` and `discounts`.
```sql
CREATE TABLE t_shirts (
  t_shirt_id INT PRIMARY KEY,
  brand VARCHAR(64),
  color VARCHAR(64),
  size VARCHAR(8),
  price DECIMAL(10,2),
  stock_quantity INT
);

CREATE TABLE discounts (
  t_shirt_id INT PRIMARY KEY,
  pct_discount DECIMAL(5,2)
);
```
Seed from your CSVs (`t_shirt.csv`, `discounts.csv`) or load your own data.

### 4) Run
```bash
streamlit run main.py
```
Then open the URL shown in the terminal. In the Interaction tab, ask a question (e.g., "How many large Nike t‑shirts are in stock?") and click Answer to see both SQL and results.

## Key Files
- `main.py` – Streamlit UI; renders the answer and final SQL
- `helper.py` – Builds LangChain `SQLDatabaseChain` with Gemini and few‑shot prompt
- `few_shots.py` – Curated examples for semantic selection
- `table.py` – Loads and displays example data
- `style/style.css` – UI styling

## Use Cases
- Business users querying databases without SQL knowledge
- Automating analytics & reporting
- Learning tool for SQL generation
