# 🚀 LeetCode Pattern Analyzer

## 📌 Overview

LeetCode Pattern Analyzer is a full-stack web application that analyzes a user's LeetCode activity and recommends problems based on their weak algorithmic patterns.

It helps users **identify gaps in their problem-solving skills** and improve efficiently.

---

## 🛠 Tech Stack

* **Frontend:** React.js
* **Backend:** FastAPI
* **Data Processing:** Pandas
* **API:** LeetCode GraphQL API
* **Language:** Python, JavaScript

---

## ⚡ Features

* 🔍 Analyze LeetCode username
* 📊 Identify weak problem-solving patterns
* 🎯 Recommend problems based on weak topics
* 🌐 Full-stack integration (React + FastAPI)
* 📁 Uses real dataset of coding problems

---

## 📂 Project Structure

```
Leetcode Pattern Analyzer/
│
├── backend/
│   ├── main.py
│   ├── recommender.py
│   ├── leetcode_api.py
│   └── data_cleaning.py
│
├── frontend/
│   ├── src/
│   ├── components/
│   └── services/
│
├── clean_dataset.csv
└── README.md
```

---

## ▶️ How to Run

### 🔹 Backend Setup

```
cd backend
pip install fastapi uvicorn pandas requests
uvicorn main:app --reload --port 5000
```

---

### 🔹 Frontend Setup

```
cd frontend
npm install
npm start
```

---

## 🧠 How It Works

1. User enters their LeetCode username
2. Backend fetches recent solved problems using LeetCode API
3. Dataset is used to map problems → topics
4. Weak topics are identified
5. New problems are recommended from those topics

---

## 📸 Screenshots (Add Later)

> Add screenshots of your UI here for better presentation

---

## 🌟 Future Improvements

* 📈 Graph visualization of weak topics
* 🤖 AI-based recommendations
* 📊 Difficulty-wise performance analysis
* 🌐 Deployment (Vercel + Render)

---

## 👨‍💻 Author

**Sanath**

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
