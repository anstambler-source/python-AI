# Final Project: S&P 500 Historical Data Analysis

## Objective

Imagine you are a data analyst at an investment company. Your task is to analyze the historical S&P 500 dataset and prepare a Jupyter Notebook that presents your findings.

---

## Requirements

Your notebook must perform the following tasks:

### 1. Load the Data

- Load the `HistoricalPrices.csv` file into a Pandas DataFrame.
- Display the first and last five rows.
- Display basic information about the dataset.

---

### 2. Prepare the Data

- Convert the `Date` column to the `datetime` type.
- Set `Date` as the DataFrame index.
- Sort the data by date in ascending order.

---

### 3. Create Additional Columns

Add the following calculated columns:

- `Range` = `High - Low`
- `Change` = `Close - Open`
- `Return` = `(Close - Open) / Open * 100`
- `MA20` – 20-day moving average of the closing price
- `MA50` – 50-day moving average of the closing price
- `Volatility` – 20-day rolling standard deviation of `Return`

---

### 4. Perform Statistical Analysis

Calculate and present:

- Number of trading days
- Highest closing price
- Lowest closing price
- Average closing price
- Median closing price
- Standard deviation of the closing price

Additionally, identify:

- The day with the largest daily gain
- The day with the largest daily loss
- The day with the largest trading range

---

### 5. Create Visualizations

Include at least **five** informative charts, such as:

- Closing price over time
- Open vs. Close prices
- Histogram of daily returns
- Closing price with 20-day and 50-day moving averages
- Rolling volatility

Ensure that every chart includes:

- A descriptive title
- Axis labels
- A grid
- A legend (where appropriate)

---

