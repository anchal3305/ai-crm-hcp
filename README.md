# AI CRM for Healthcare Professionals

An AI-powered CRM system that converts natural language interaction summaries into structured data automatically.

---

## Overview

This project allows users to enter interaction details in plain English, and the system automatically extracts key CRM fields like:

* Doctor Name
* Interaction Type
* Topics Discussed
* Sentiment
* Outcomes
* Follow-up Actions

---

## Problem Statement

Traditional CRM systems require users to manually fill multiple fields after every interaction, which is time-consuming and inefficient.

---

## Solution

This system uses AI to:

* Understand natural language input
* Extract structured data
* Automatically populate CRM fields
* Store interaction data in a database

---

## Tech Stack

**Frontend**

* React.js

**Backend**

* FastAPI (Python)

**AI / NLP**

* LangGraph
* Groq API (LLM)

**Database**

* MySQL

---

## Project Structure

```
ai-crm-hcp/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── db.py
│   ├── tools.py
│   ├── langgraph_agent.py
│
├── frontend/
│   ├── src/
│   ├── components/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How to Run

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app_api --reload
```

---

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Environment Variables

Create a `.env` file inside the `backend/` folder:

```
GROQ_API_KEY=your_api_key_here
```

## Example Input

```
Met Dr. Mehta, discussed insulin, he was interested
```

---

## Output Example

```
Doctor Name: Dr. Mehta  
Interaction Type: Meeting  
Topics: Insulin  
Sentiment: Positive  
Outcomes: Interested  
Follow-up: Schedule next meeting  
```

---
## UI
### Ouput Image
<img width="958" height="560" alt="image" src="https://github.com/user-attachments/assets/ac69d97d-9483-4b41-a393-f06ddf2032de" />


## Features

* Natural language input
* AI-powered data extraction
* Automatic form filling
* Database storage
* Clean UI

---

## Future Improvements

* Interaction history dashboard
* Authentication system
* Better UI/UX design
* Multi-language support

---

## Author

Anchal Gupta

---

## If you like this project, give it a star!
