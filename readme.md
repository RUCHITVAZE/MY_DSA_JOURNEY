#E-Commerce Sales Dashboard

An interactive Power BI dashboard designed to track, analyze, and optimize direct-to-consumer (D2C) retail performance. This project transforms raw transactional data into actionable business insights using Power Query, a structured star schema data model, and custom DAX measures.

---

## 📊 Project Overview

This dashboard provides a comprehensive view of e-commerce operations, helping stakeholders monitor profitability, consumer purchasing patterns, and regional sales health. It isolates key retail performance indicators to drive data-backed decisions for inventory and marketing strategies.

### Key Insights Tracked:
* **Profitability Analysis:** Real-time tracking of overall sales volume, costs, and net profit margins.
* **Customer Behavior:** Tracking Average Order Value (AOV) and purchase quantities across product sub-categories.
* **Geographic Breakdown:** Performance tracking across different states and localized markets.
* **Operational Lifecycles:** Visibility into payment methods and monthly growth trends.

---

## 🛠️ Tech Stack & Architecture

* **Data Transformation:** Power Query Editor (Data cleaning, handling null values, and data type alignment).
* **Data Modeling:** Star Schema design establishing clean 1-to-many (`1` to `*`) relationships between data layers.
* **Analytical Engine:** Advanced Data Analysis Expressions (DAX) for dynamic calculation blocks.
* **Visualization:** Power BI Desktop tailored with an executive theme for optimal clarity and scannability.

---

## 🗂️ Data Model & Schema

The infrastructure relies on a highly efficient relational schema split into two primary datasets:

1. **`Orders` (Dimension Table):** Contains transaction high-level metadata including `Order ID`, `Order Date`, `Customer Name`, `State`, and `City`.
2. **`Details` (Fact Table):** Contains transactional granular values including `Amount`, `Profit`, `Quantity`, `Category`, `Sub-Category`, and `Payment Mode`.

---

## 📐 Core DAX Measures Used

The analytical framework utilizes the following calculated explicit measures built directly inside the model:

### Total Sales Amount
```dax
Total Sales = SUM('Details'[Amount])