# 📈 Stock Market ML Predictor

**End-to-End Machine Learning Platform for Next-Day Stock Forecasting**

[![Python](https://img.shields.io/badge/Python-3.x-3776ab?style=flat-square&logo=python&logoColor=white)](#)
[![Django](https://img.shields.io/badge/Django-Backend-092E20?style=flat-square&logo=django&logoColor=white)](#)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](#)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=flat-square&logo=mongodb&logoColor=white)](#)
[![Chart.js](https://img.shields.io/badge/Chart.js-Frontend-FF6384?style=flat-square&logo=chartdotjs&logoColor=white)](#)

---

Stock Market ML Predictor is an **end-to-end machine learning–powered forecasting platform** built to analyze and predict the market behavior of the Top 10 companies by market capitalization. A **Linear Regression model**, trained dynamically on the fly, classifies continuous growth trends to forecast the next trading day's closing price. The Django web application wraps that model in a full workflow — automated historical data ingestion, live inference, and graphical result comparison — optionally backed by a persistent cloud database.

> ⚠️ **Disclaimer:** This project is a research/portfolio tool intended to demonstrate an ML-powered data pipeline. It is **not** a certified financial advisory tool and should not be used for real-world trading or financial decision-making.

## ✨ Key Features

| Feature | Description |
|---|---|
| **Live Data Ingestion** | Automatically downloads the last 3 years of daily historical closing prices directly via the `yfinance` API upon page load. |
| **On-the-Fly ML Engine** | A Linear Regression model (`scikit-learn`) is trained dynamically from scratch for each company to recognize current growth trends. |
| **Dynamic Visualization** | Uses `Chart.js` to render a comparative, color-coded bar graph of current actual prices versus predicted prices. |
| **Cloud Database Persistence** | SQLAlchemy/Djongo models securely connect to MongoDB Atlas to store and track prediction records over time. |
| **Stateless Capability** | Capable of running as a stateless architecture, processing data entirely in memory for rapid, database-free deployment and testing. |
| **Continuous Integration** | Integrated GitHub Actions pipeline automatically installs dependencies and runs Django system checks on every push. |

## 🏗️ Architecture

```mermaid
graph LR
    A["🌐 Web Dashboard<br/><small>Chart.js UI</small>"] --> B["⚙️ Django Backend<br/><small>views.py</small>"]
    B --> C["📉 Yahoo Finance API<br/><small>3-Year Historical Data</small>"]
    C --> D["🧠 ML Engine<br/><small>Scikit-Learn</small>"]
    D --> E["🔮 Next-Day Prediction<br/><small>Linear Regression</small>"]
    E --> F["🗄️ Database<br/><small>MongoDB Atlas</small>"]
    F --> A

    style A fill:#06b6d422,stroke:#06b6d4,color:#e2e8f0
    style B fill:#eab30822,stroke:#eab308,color:#e2e8f0
    style C fill:#ef444422,stroke:#ef4444,color:#e2e8f0
    style D fill:#22c55e22,stroke:#22c55e,color:#e2e8f0
    style E fill:#7c3aed22,stroke:#7c3aed,color:#e2e8f0
    style F fill:#3b82f622,stroke:#3b82f6,color:#e2e8f0
