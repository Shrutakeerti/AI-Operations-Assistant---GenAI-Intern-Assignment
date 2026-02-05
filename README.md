# AI Operations Assistant

This is a local AI agent I built to handle various operations tasks. It's designed with a multi-agent architecture (Planner → Executor → Verifier) to break down complex natural language requests into actionable steps.

## How It Works

The system operates in a loop:
1.  **Planner Agent**: Takes your request (e.g., "Find the latest Python news") and creates a JSON execution plan.
2.  **Executor Agent**: Loops through the plan and calls the necessary tools. It's smart enough to pass data between steps — for example, using a URL found in a search step as input for a reading step.
3.  **Verifier Agent**: Takes the raw tool outputs, checks them for errors, and formats everything into a clean final response.

## Features

-   **Multi-Agent Workflow**: Separates reasoning (Planning) from action (Execution) and checking (Verification).
-   **Real Tools**:
    -   `github_search`: Finds repositories and metadata.
    -   `news_search`: Fetches latest headlines (requires NewsAPI key).
    -   `web_search`: Performs general web searches using DuckDuckGo (no key needed).
-   **Smart Chaining**: I implemented a dynamic dependency system so steps can reference previous results (like `{{LATEST_URL}}`), allowing for multi-step research flows.
-   **Robust Error Handling**: If a tool fails or an API blocks a request, the verifier handles it gracefully instead of crashing the app.

## Setup & Running

1.  **Install Dependencies**

    **Using uv (Recommended for speed)**
    ```bash
    # Create a virtual environment and install dependencies
    uv venv
    source .venv/bin/activate
    uv pip install -r requirements.txt
    ```

    **Using pip**
    ```bash
    # Create a virtual environment
    python -m venv .venv
    source .venv/bin/activate
    
    # Install dependencies
    pip install -r requirements.txt
    ```

2.  **Environment Variables**
    You'll need a `.env` file in the root directory. I've included a `.env.example` you can copy.
    ```ini
    GROQ_API_KEY=<your-groq-api-key>
    GROQ_MODEL_NAME="llama-3.1-8b-instant"
    NEWS_API_KEY=2ed3d82045cd4c36861f956022f5370d
    ```

3.  **Run the App**
    The interface is built with Streamlit.
    
    **Using uv**
    ```bash
    uv run streamlit run main.py
    ```

    **Using standard streamlit**
    ```bash
    streamlit run main.py
    ```

## Project Structure

-   `agents/`: Contains the logic for the Planner, Executor, and Verifier.
-   `tools/`: The actual Python scripts that hit APIs (GitHub, News, DDG).
-   `llm/`: Wrapper for the Groq client.
-   `main.py`: The frontend entry point.

## Notes

I specifically chose the **Groq** API for inference because its speed makes the agentic loop feel almost instant. If you want to swap models, just update the client in `llm/groq_client.py`.
