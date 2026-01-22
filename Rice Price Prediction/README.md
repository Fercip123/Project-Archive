# Rice Price Prediction & Automated Reporting System 

This project is part of my **Project-Archive**. It is a data analytics tool designed to process, analyze, and forecast rice commodity prices using historical data.

> **🇮🇩 Language Note:** The source code and comments in `perdiksiberasfinal.py` are written in **Bahasa Indonesia** to maintain the original context of the local food price data.

---

## Dataset Overview
The historical rice price data used in this project is sourced from **PIHPS (Pusat Informasi Harga Pangan Strategis Nasional)**, the official Indonesian national strategic food price information center.
- **Data Source:** [PIHPS National Website](https://www.bi.go.id/hargapangan)
- **Content:** Monthly historical prices of rice commodities across various regions.

## Technical Features
- **Object-Oriented Logic:** Built using a class-based structure (`SistemAnalisisPangan`) for clean and modular data processing.
- **Machine Learning:** Implements **Linear Regression** via `scikit-learn` to project price trends for the upcoming 12 months.
- **Automated Reporting:** - Generates an Excel report (`Laporan_Prediksi_Beras.xlsx`) using `XlsxWriter`.
  - Automatically exports visualization charts into the Excel sheet and saves them as `.png` files.
- **Data Integrity:** Includes custom cleaning logic to handle Indonesian currency formatting and date structures.



## How to Use
1. Ensure you have the dataset from PIHPS in `.csv` format.
2. Install the required libraries:
   ```bash
   pip install pandas numpy scikit-learn matplotlib xlsxwriter
