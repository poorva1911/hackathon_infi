# Agentic Bug Hunter
Agent-Based Retrieval-Augmented Debugging System

Agentic Bug Hunter is a modular AI-powered debugging system that detects bugs in C++ code, classifies the error type, retrieves relevant documentation using a vector-based MCP server, and generates structured technical explanations.

This system combines:

Diff-based bug localization

Rule-based bug classification

MCP-powered semantic retrieval

Structured explanation generation

Batch processing (CSV)

Interactive UI (Streamlit)

## Project Root Path

All commands must be executed from:

D:\poorva\nirma\b19\code\hackathon_infi
### Project Structure
hackathon_infi/
│
├── abh_app/
│   ├── main.py                  # Orchestrator (Batch Mode)
│   │
│   ├── agents/
│   │   ├── diff_agent.py        # Bug Detection Agent
│   │   ├── explanation_agent.py # Classification + Retrieval Agent
│   │
│   └── utils/
│       ├── csv_writer.py        # Output Writer
│
├── server/
│   ├── mcp_server.py            # Embedding + Retriever Setup
│   ├── embedding_model/         # Local embedding model
│   └── storage/                 # Stored vector index
│
├── ui_app.py                    # Streamlit UI
├── samples.csv                  # Input dataset
├── output.csv                   # Generated output
└── requirements.txt

## Agents Used in This System

The system is built using modular agents:

### Diff Agent — Bug Localization

File:

abh_app/agents/diff_agent.py


Purpose:

Compare incorrect and correct code.

Identify the first mismatched line.

Return the buggy line number.

Technology:

Python difflib

This agent answers:
 "Where is the bug?"

### Classification & Explanation Agent

File:

abh_app/agents/explanation_agent.py


Responsibilities:

Detect bug type (assignment error, logic mismatch, etc.)

Classify error type (Logical Error, Runtime Error, Undefined Behavior)

Retrieve documentation using MCP retriever

Generate structured explanation

This agent answers:
"What kind of bug is this?"
"Why is it wrong?"
"How is it fixed?"

### MCP Retrieval Agent (Vector Layer)

File:

server/mcp_server.py


Purpose:

Load HuggingFace embedding model

Load stored vector index

Create retriever object

Perform semantic similarity search

How it is used:

Inside explanation_agent.py:

from server.mcp_server import retriever
nodes = retriever.retrieve(buggy_line)


This means:

Buggy line → converted into embedding.

Compared against stored documentation embeddings.

Most relevant documentation chunks returned.

Used as technical reference in explanation.

This makes the system:

✔ Retrieval-Augmented
✔ Context-aware
✔ Explainable
✔ Offline-capable

## System Workflow
Input (Incorrect + Correct Code)
        ↓
Diff Agent (Find Bug Line)
        ↓
Classification Agent (Detect Bug Type)
        ↓
MCP Retriever (Semantic Documentation Search)
        ↓
Structured Explanation Generation
        ↓
Output (CSV / UI)

⚙ Installation
Step 1 — Navigate to Project Folder
cd D:\poorva\nirma\b19\code\hackathon_infi

Step 2 — Install Dependencies
pip install -r requirements.txt


If required, manually install:

pip install fastmcp llama-index llama-index-embeddings-huggingface sentence-transformers transformers torch pandas streamlit

## Running Batch Mode (Generate output.csv)

This processes samples.csv and generates output.csv.

From project root:

cd D:\poorva\nirma\b19\code\hackathon_infi
python -m abh_app.main


After execution:

output.csv


is generated in:

D:\poorva\nirma\b19\code\hackathon_infi

## Running UI Mode

Launch Streamlit interface:

cd D:\poorva\nirma\b19\code\hackathon_infi
streamlit run ui_app.py


Open browser at:

http://localhost:8501


You can:

Paste incorrect code

Paste correct code

Click "Detect Bug"

View structured explanation instantly

## Commands Used During Development

Below are the main commands executed during development:

Navigate to project:

cd D:\poorva\nirma\b19\code\hackathon_infi


Install dependencies:

pip install -r requirements.txt


Run batch processing:

python -m abh_app.main


Run UI:

streamlit run ui_app.py




## Output Format

Example structured explanation:

Bug Detected at Line 2

Incorrect Statement:
if (x = 5)

Correct Statement:
if (x == 5)

Bug Category:
Assignment in Condition

Error Type:
Logical Error

Why This Is an Error:
The condition uses '=' instead of '=='...

Technical Reference:
[Retrieved documentation snippet]

How It Is Fixed:
Correct comparison restores intended logic.





