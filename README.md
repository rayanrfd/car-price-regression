# Car Price Regression

## 🚀 Project Overview

This project predicts used car prices using a machine learning regression model. It includes data preprocessing, model training, a FastAPI backend for serving predictions, and a Streamlit frontend for user interaction.

## 📂 Project Structure

```markdown
.

├── data/ # Raw datasets and auxiliary files
├── models/ # Saved model and preprocessor artifacts
├── notebooks/ # Jupyter notebooks for EDA and training
├── src/ # Source code modules
│ ├── api/ # FastAPI app, routes, schemas, business logic
│ ├── pipeline/ # Training pipeline scripts
│ ├── transformers/ # Custom data transformers and imputers
│ └── ui/ # Streamlit user interface code
├── test/ # Unit and integration tests
├── main.py # Optional entry point
├── requirements.txt # Python dependencies
├── pyproject.toml # Project metadata/configuration
├── README.md # This file
└── .gitignore # Git ignore rules
```

## ⚙️ Installation

### Prerequisites

- Python 3.11+  
- Git  
- [uv (Astral)](https://github.com/astral-sh/uv) installed (you can install it via `pip install uv` or your package manager)

### Steps

1. Clone the repository:

```bash
git clone https://github.com/yourusername/car-price-regression.git
cd car-price-regression
```

Install dependencies with uv (reads pyproject.toml):
```bash
uv sync
```

(Optional) Activate the virtual environment:
```bash
source .venv/bin/activate
```


---

## 🏗️ Usage

### Train the model

Run the training pipeline to preprocess data and train the regression model:

```bash
python src/pipeline/train.py
```

This saves the model and preprocessor in the `models/` folder.

---

### Start the FastAPI backend

Launch the API server to serve predictions:

```bash
uvicorn src.api.app:app --reload
```

Access the interactive API docs at `http://localhost:8000/docs`.

---

### Run the Streamlit UI

Launch the frontend app for user-friendly prediction input:

```bash
python -m streamlit run src/ui/ui.py
```
