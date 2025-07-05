
# 🚗 Smart Parking Demand-Based Pricing Engine (Capstone Project)

This capstone project simulates a real-time dynamic pricing system for urban parking lots based on demand indicators like occupancy, traffic, vehicle type, queue length, and special day flags. It uses both batch (Pandas) and streaming (Pathway) approaches to calculate and stream parking prices in real-time.

---

## 🛠Tech Stack

- **Python 3.11**
- **Pandas** – Data preprocessing, feature engineering
- **Pathway** – Real-time streaming engine
- **JSONL** – Output format for streamed price data
- **Google Colab Notebook** – Prototyping, visualization (optional)
- **Bokeh (Optional)** – Plotting results in early experiments

---

## 📊 Models Implemented

### Model 1: Occupancy-Based Pricing
> A simple pricing model that increases price with occupancy.

### Model 2: Demand-Based Pricing (Deployed in Pathway)
> Uses a weighted score of features like queue length, traffic, and vehicle type to calculate price dynamically.  
Deployed as a real-time stream using Pathway.

### Model 3: Competitive Pricing (Planned Extension)
> Intended to adjust price based on nearby lot prices within 1 km.
This model was scoped and designed but not integrated due to time constraints.

---

## Architecture Overview

```
Raw CSV Data (Cleaned) → Feature Engineering (Pandas) → Pathway Engine → JSONL Streaming Output
```

---

## How to Run

```bash
pip install pathway pandas
```

1. Upload `sample_100.csv`  
2. Run `pathway_model2.py`  
3. Output will be saved to: `model2_output.jsonl`

To preview:
```bash
head model2_output.jsonl
```

---

## 📁 Folder Structure

```
📂 iitg-analytics-course/Capstone Project/
├── smart_parking_notebook.ipynb         # Logic prototyping, EDA, Model 1 & 2 (Pandas)
├── pathway_model2.py                    # Final deployed model in Pathway
├── sample_100.csv                       # Trimmed sample of the dataset
├── model2_output.jsonl                  # Output stream of demand-based prices
└── README.md                            # This file 
```

---

## Sample Output

```json
{"SystemCodeNumber": "BHMBCCMKT01", "Timestamp": "2016-10-04 09:59:00", "Occupancy": 150, "Capacity": 577, "DemandPrice": 10.14}
```

---

## Acknowledgements

This project was completed as part of a beginner's data analytics journey.  
Model 3 was explored conceptually but reserved for future deployment.

---

✨ Built with chaos, errors, retries, and a whole lot of perseverance 😅
