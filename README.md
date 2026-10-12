# Sales Data Analysis

A beginner-friendly Data Science project that analyzes a sample retail sales dataset using Python, pandas, and matplotlib.

## Project objectives
- Clean and prepare sales data
- Calculate revenue after discount
- Find revenue by product and region
- Analyze monthly revenue trends
- Export summary tables and charts

## Folder structure
```text
Sales_Data_Analysis/
├── data/
│   └── sales_data.csv
├── outputs/
├── sales_analysis.py
├── requirements.txt
└── README.md
```

## Requirements
- Python 3.9 or newer
- pandas
- matplotlib

## How to run
1. Extract the ZIP file.
2. Open a terminal or command prompt inside the `Sales_Data_Analysis` folder.
3. (Optional) Create and activate a virtual environment.
4. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the analysis:
   ```bash
   python sales_analysis.py
   ```

The script prints key metrics and creates CSV summaries and PNG charts inside the `outputs` folder.

## Dataset columns
- `OrderDate`: date of the order
- `Region`: sales region
- `Product`: product name
- `Category`: product category
- `Quantity`: units sold
- `UnitPrice`: price per unit in rupees
- `Discount`: discount per unit in rupees

## Suggested next improvements
- Add profit and cost columns
- Import a larger public dataset
- Build an interactive dashboard in Power BI or Excel
- Add unit tests and a Jupyter Notebook
- Write a short report describing insights and limitations

## Important
The included dataset is synthetic sample data created for practice, not real company sales data. Review the output and understand the code before adding this project to your resume.
