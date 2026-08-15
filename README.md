# Huawei Data Science and Machine Learning Bootcamp

This repository contains the work, assignments, and hands-on projects completed as part of the Huawei Data Science and Machine Learning Bootcamp. The content is organized into three main sections: **Python**, **Data Science**, and **Machine Learning**.

## Table of Contents

- [Python](#python)
- [Data Science](#data-science)
- [Machine Learning](#machine-learning)
- [Setup](#setup)

---

## Python

Topic-by-topic exercises covering everything from Python basics to object-oriented programming.

| Folder | Topic |
|---|---|
| `1_python_introduction` | Introduction to Python, first programs |
| `2_python_basic_structures` | Basic data structures and variables |
| `3_loops_control_structures` | Loops and control structures (`for`, `while`, `if/else`, `break/continue/pass`) |
| `4_functions` | Functions, scope, and built-in functions |
| `5_file_operations` | File reading/writing operations |
| `6_error_management` | Error handling (try/except) |
| `7_environment_packet_management` | Virtual environments and package management |
| `8_numpy` | Numerical operations with NumPy |
| `9_pandas` | Data manipulation with Pandas (CSV/Excel reading-writing) |
| `10_matplotlib` | Data visualization with Matplotlib |
| `11_oop` | Object-oriented programming (OOP) |
| `12_finalproject` | Final project using a student grades dataset |

## Data Science

An end-to-end data science workflow applied to an e-commerce dataset: fixing data types, removing duplicate records, and handling outliers and missing values.

- `data_science.ipynb` / `data_science_work.ipynb` — notebooks containing the analysis and preprocessing steps
- `e_ticaret_veri_seti*.csv` — the raw dataset and the cleaned versions produced after each processing step

## Machine Learning

Standalone exercises covering topics from supervised and unsupervised learning to model explainability, each with its own `requirements.txt` file.

| Folder | Topic |
|---|---|
| `1_data_preprocessing` | Data preprocessing |
| `2_feature_extraction` | Feature engineering |
| `3_supervised_learning` | Supervised learning: Logistic Regression, KNN, SVM, Decision Tree/Random Forest, Linear/Polynomial/Lasso/Ridge Regression |
| `4_unsupervised_learning` | Unsupervised learning: clustering |
| `5_dimension_reduction` | Dimensionality reduction: PCA and t-SNE |
| `6_cross_validation` | Cross-validation |
| `7_hyperparameter_tuning` | Hyperparameter tuning: Grid Search and Random Search |
| `8_explainability` | Model explainability: LIME and SHAP |

## Setup

Each subfolder's `requirements.txt` file lists the dependencies needed for that exercise. Navigate to the relevant folder and run:

```bash
pip install -r requirements.txt
```
