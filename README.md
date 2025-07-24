
# 📱 Mental Health Predictor Based on Digital Habits

An elegant machine learning web app that predicts **mental health stress levels** based on Gen Z’s digital behavior—including screen time, social media use, and sleep patterns.

---

## 🧠 About the Dataset

### Overview
The **Digital Habits vs. Mental Health** dataset is a **synthetic yet realistic dataset** designed to study the relationship between the digital lifestyle of Gen Z and their mental health.

It includes **100,000 samples** across **6 behavior and psychological features**, designed for EDA, regression modeling, and public health analysis.

This dataset is ideal for:
- Exploratory Data Analysis (EDA)
- Correlation Studies
- Machine Learning (Regression/Classification)
- Educational Projects on Digital Well-being

---

## 📊 Feature Descriptions

| Column Name                  | Data Type | Description                                                                 |
|-----------------------------|-----------|-----------------------------------------------------------------------------|
| `screen_time_hours`         | float64   | Total daily screen time across all devices (in hours).                     |
| `social_media_platforms_used` | int64     | Number of social media platforms used daily.                               |
| `hours_on_TikTok`           | float64   | Daily time spent specifically on TikTok (in hours).                        |
| `sleep_hours`               | float64   | Average hours of sleep per day.                                            |
| `stress_level`              | int64     | Perceived stress level (1–10).                                             |
| `mood_score`                | int64     | Mood rating (1–10), where higher is better.                                |

---

## 🧭 Context

In the digital age, particularly among Gen Z, screen time and social media engagement have become dominant parts of daily life. Research by the **American Psychological Association (APA)** and **Pew Research Center** suggests:

- High screen time is linked to **poor sleep quality** and **increased anxiety**.
- Short-form content (like TikTok) has been shown to **shorten attention spans**.
- Lack of proper sleep is associated with **higher stress** and **mood disorders**.

This app and dataset simulate real-world conditions while maintaining ethical and privacy standards, offering insights into how digital habits may affect mental health.

---

## 💡 Inspiration & Data Sources

This project and dataset were inspired by:

- Peer-reviewed **academic research** in psychology and behavioral science.
- Trends reported by organizations like **Common Sense Media**, **CDC YRBS**, and **Statista**.
- Community practices from **Kaggle**, **Hugging Face**, and **Claude Opus training notes**.
- Social media trends including the massive impact of platforms like **TikTok** on digital behavior.

The synthetic data generation logic applied **controlled randomness** and **logical correlations** (e.g., more TikTok → less sleep → more stress) to mimic real-world behavioral dynamics.

---

## 🚀 Features of the App

- 🎚️ **Interactive Sliders** for all inputs in a stylish UI
- 💡 **Clean Apple-like UI** with gradients and intuitive layout
- ⚡ Powered by a trained **XGBoost Regressor** model
- 🧠 Predicts **stress level** in real-time based on inputs
- 📁 Model path: `/home/aryan/AI/Project 2/notebooks/xgbreg.pkl`

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (custom), Jinja2 Templates
- **Model**: XGBoost (`xgbreg.pkl`) (Best choosen)
- **Visualization**: Matplotlib, Seaborn (for EDA)

---

## 🧪 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Aryan-KAisth/Stress_level.git
   cd mental-health-predictor
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask app:
   ```bash
   python app.py
   ```

---
