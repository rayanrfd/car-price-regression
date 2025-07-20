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

1. Clone the repository:

```bash
git clone https://github.com/rayanrfd/car-price-regression.git
cd car-price-regression
```

1. (Optional) Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

1. Install dependencies:

```bash
pip install -r requirements.txt
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
streamlit run src/ui/ui.py
```

---

## 🧪 Testing

Run tests using pytest:

```bash
pytest test/
```

Project Link: https://github.com/yourusername/car-price-regression
