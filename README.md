# 🎓 College Club Recommender

**Developer:** Ujjwal Sharma  
**Registration Number:** 25BCE11120  
**Institution:** VIT Bhopal University  
**Degree:** B.Tech in Computer Science and Engineering  
**Academic Year:** 2025–2026

---

## 📌 Project Overview
This repository contains a Machine Learning-powered recommendation system designed to help college students find the perfect campus clubs and organizations. By analyzing a student's personal interests, skills, and professional goals, this terminal-based application uses Natural Language Processing (NLP) to bridge the gap between students and student-led organizations, providing highly personalized matches directly in the command line.

---

## 📂 Repository Structure & Core Components

### [1. Main Execution Script (app.py)](./app.py)
* **Objective:** Serve as the core engine and user interface for the recommender.
* **Description:** A lightweight, terminal-based Python script that handles user input prompts, executes the NLP text vectorization (e.g., TF-IDF or CountVectorizer), calculates Cosine Similarity, and prints the ranked club recommendations directly to the console.

### [2. Club Dataset (clubs_data.csv)](./clubs_data.csv)
* **Objective:** Provide the foundational data corpus for the ML model to learn from.
* **Description:** A curated dataset containing comprehensive details about various college clubs, including their titles, detailed descriptions, and categorizing tags.

### [3. Project Dependencies (requirements.txt)](./requirements.txt)
* **Objective:** Ensure seamless local setup and environment replication.
* **Description:** Contains all necessary Python libraries required to run the core machine learning logic, ensuring version compatibility across different machines.

---

## 🛠️ Technical Toolkit
* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-learn (Text Vectorization, Cosine Similarity)
* **Interface:** Command-Line Interface (CLI) / Terminal
* **Version Control:** Git & GitHub

---

## ⚙️ Local Setup & Execution
To deploy and test this project on your local machine, run the following commands in your terminal:

```bash
# 1. Clone the repository
git clone [https://github.com/UjjwalSharma2304/College-Club-Recommender.git](https://github.com/UjjwalSharma2304/College-Club-Recommender.git)

# 2. Navigate into the directory
cd College-Club-Recommender

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py
