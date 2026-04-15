# Data Analysis Template

A reusable Python template for exploratory data analysis (EDA) built with clean design patterns. Pull this repo and plug in your own dataset to get a structured, repeatable analysis workflow.

## Project Structure

```
data_analysis_template/
├── analyzer/
│   ├── basic_data_inspection.py      # Data type & summary inspection strategies
│   ├── missing_values_analysis.py    # Missing values identification & visualization
│   └── univariate_data_analysis.py   # Numerical & categorical univariate analysis
├── data/
│   └── AmesHousing.csv               # Sample dataset (Ames Housing)
├── EDA.ipynb                         # Main EDA notebook demonstrating the workflow
├── .gitignore
└── README.md
```

## Features

### Basic Data Inspection
- **Data types & non-null counts** — quickly understand column types and completeness
- **Summary statistics** — descriptive stats for both numerical and categorical features

### Missing Values Analysis
- **Identification** — counts missing values per column
- **Visualization** — heatmap of missing data patterns across the dataset

### Univariate Analysis
- **Numerical features** — histogram with KDE overlay
- **Categorical features** — frequency bar plots

## Design Patterns

The template uses the **Strategy Pattern** and **Template Method Pattern** to keep analysis steps modular and swappable:

- **Strategy Pattern** (`DataInspector`, `UnivariateAnalyzer`) — swap inspection or analysis strategies at runtime without changing client code
- **Template Method Pattern** (`MissingValuesAnalysisTemplate`) — defines the analysis skeleton (identify → visualize) while letting subclasses fill in the details

## Getting Started

### Prerequisites

- Python 3.8+
- pandas
- matplotlib
- seaborn
- numpy
- Jupyter Notebook / JupyterLab

### Installation

```bash
git clone <repo-url>
cd data_analysis_template
pip install pandas matplotlib seaborn numpy jupyter
```

### Usage

1. **Replace the sample data** — drop your CSV into the `data/` folder and update the path in `EDA.ipynb`
2. **Run the notebook** — open `EDA.ipynb` and execute cells to see the full workflow
3. **Extend with your own strategies** — implement new analysis strategies by subclassing the abstract base classes

```python
from analyzer.basic_data_inspection import DataInspector, DataTypesInspection, DataSummaryInspection
from analyzer.missing_values_analysis import SimpleMissingValuesAnalysis
from analyzer.univariate_data_analysis import UnivariateAnalyzer, NumericalUnivariateAnalysis

# Inspect data types
inspector = DataInspector(DataTypesInspection())
inspector.execute_inspection(df)

# Switch to summary stats
inspector.set_strategy(DataSummaryInspection())
inspector.execute_inspection(df)

# Analyze missing values
SimpleMissingValuesAnalysis().analyze(df)

# Univariate analysis on a numerical feature
analyzer = UnivariateAnalyzer(NumericalUnivariateAnalysis())
analyzer.execute_analysis(df, "SalePrice")
```

## Roadmap

- [ ] Bivariate and multivariate analysis strategies
- [ ] Outlier detection and handling
- [ ] Missing data imputation strategies
- [ ] Correlation and multicollinearity analysis
- [ ] Feature engineering utilities
- [ ] Categorical encoding strategies
- [ ] Data export and reporting

## License

This project is open source and available for anyone to use as a starting point for their data analysis workflows.
