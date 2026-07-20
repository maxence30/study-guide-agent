# AI Agents in Python

## Description

This project is a multi-agent study guide generator built with Python, Google ADK, LiteLLM, and Ollama.

The application generates beginner-friendly study guides about programming topics using multiple AI agents working together in a sequential workflow.

The generated guide is validated and saved as a Markdown file.

---

## Requirements

- Python 3.12+
- Ollama
- Google ADK
- LiteLLM
- Google GenAI SDK

---

## Setup

Clone the repository:

```bash
git clone https://github.com/maxence30/study-guide-agent.git
cd study-guide-agent
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Download the model:

```bash
ollama pull qwen2.5:3b
```

Start Ollama:

```bash
ollama serve
```

---

## Configuration

Create a `.env` file.

Example:

```env
OLLAMA_API_BASE=http://localhost:11434
MODEL_NAME=ollama_chat/qwen2.5:3b
```

---

## How to Run

```bash
python main.py
```

Enter a topic such as:

```
Python decorators
```

---

## Example Input

```
Python decorators
```

---

## Example Output

```md
# Topic

## Simple Explanation

...

## Key Concepts

...

## Example

...

## Practice Exercise

...

## Common Mistakes

...

## Review Comments

...

## Final Summary
```

---

## Project Structure

```
study-guide-agent/
│
├── agents/
│   ├── explainer_agent.py
│   ├── practice_designer_agent.py
│   └── reviewer_agent.py
│
├── tools/
│   ├── file_writer.py
│   └── validation.py
│
├── output/
│
├── data/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
└── main.py
```

---

## Agents

### Explainer Agent

Explains a programming topic.

Produces:

- Simple explanation
- Key concepts
- Example

---

### Practice Designer Agent

Creates a beginner exercise using the explanation generated previously.

Produces:

- Practice Exercise
- Expected Input
- Expected Output
- Hints

---

### Reviewer Agent

Reviews the generated study guide.

Produces:

- Common Mistakes
- Review Comments
- Final Summary

---

## Tools

### save_markdown_file()

Saves the generated study guide into the `output/` directory.

---

### validate_required_sections()

Checks that the Markdown contains all required sections.

Returns:

- validation status
- missing sections

---

## Self-Validation Checklist

- [x] Project structure created
- [x] Local model configured with Ollama
- [x] Google ADK configured
- [x] Explainer Agent implemented
- [x] Practice Designer Agent implemented
- [x] Reviewer Agent implemented
- [x] Sequential workflow implemented
- [x] Markdown validation implemented
- [x] Markdown saved automatically

---

## Reflection

### What is the difference between a direct LLM call and an AI agent?

A direct LLM call simply sends a prompt to a language model and returns a response.

An AI agent combines a model with instructions, a specific role, and can interact with tools or other agents to complete more complex workflows.

---

### What role does each agent have?

**Explainer Agent**

Explains the programming topic.

**Practice Designer Agent**

Creates a beginner-friendly exercise based on the explanation.

**Reviewer Agent**

Reviews the study guide and provides constructive feedback.

---

### What role does each tool have?

**save_markdown_file**

Writes the generated study guide to disk.

**validate_required_sections**

Ensures that every required Markdown section is present.

---

### What was the most difficult part?

The most difficult part was configuring Google ADK with LiteLLM and Ollama so that all components worked together correctly.

---

### What limitation did you observe?

The selected local model sometimes produces inconsistent Markdown formatting and may omit requested sections without careful prompt design.

---

## Known Limitations

- Small local models may produce inconsistent formatting.
- Responses may vary between executions.
- Validation checks only the document structure, not the quality of the content.
- The project currently supports one topic at a time.python main.py
