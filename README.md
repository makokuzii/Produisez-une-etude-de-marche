# International Market Study for Chicken Export

A data-driven analysis project for **La poule qui chante** to identify optimal international markets for chicken export expansion. This study combines PESTEL framework analysis with advanced statistical methods (PCA and clustering) to segment countries into strategic market groups.

## Business Context

This project was commissioned by Patrick, CEO of La poule qui chante, to support the company's international expansion strategy. The objective is to analyze country groupings that can be targeted for chicken exports, providing a foundation for deeper market studies.

### Project Objectives

- Identify and analyze country clusters suitable for chicken export
- Integrate minimum 8 variables covering multiple PESTEL dimensions
- Cover at least 100 countries representing 60%+ of global population
- Apply dimensionality reduction (PCA) and clustering techniques (HAC + K-means)
- Provide actionable insights for market selection and prioritization

## Analytical Framework

### PESTEL Analysis

The variable selection follows the PESTEL framework to ensure comprehensive market assessment:

- **Political**: Political Stability Index, Regulatory Quality Index
- **Economic**: GDP per Capita, GDP per Capita Growth, Import/Export volumes
- **Social**: Population Growth, Urbanization Growth, Urban Population, Poultry Consumption patterns
- **Technological**: Access to Electricity, Logistics Performance Index
- **Environmental**: Chicken Meat Production capacity
- **Legal**: Regulatory Quality, Trade policies (implicit in import/export data)

## Data Sources

The analysis integrates open data from multiple authoritative sources:

- **FAO (Food and Agriculture Organization)**: 
  - Chicken meat production statistics
  - Import/export quantities for live and processed chicken
  - Per capita meat consumption by type
  
- **World Bank Open Data**:
  - GDP per capita (current US$)
  - GDP per capita growth rates
  - Population metrics and growth rates
  - Urbanization rates and trends
  - Access to electricity (% of population)
  - Logistics Performance Index
  - Political Stability Index
  - Regulatory Quality Index

- **UN M49 Standard**: Country codes and regional classifications

### Dataset Coverage

- **Countries**: 100+ nations analyzed
- **Population Coverage**: 60%+ of global population
- **Variables**: 15+ indicators across PESTEL dimensions
- **Time Period**: Most recent available data (2020-2023)

## Project Structure

```
.
├── data/                                    # Raw and processed datasets
│   ├── cleaned_chicken_market_study_data.csv    # Final merged dataset
│   ├── GDP per capita/                          # World Bank GDP data
│   ├── access to electricity/                   # Infrastructure indicator
│   ├── chicken-meat-production/                 # FAO production data
│   ├── import export of dead and live chicken/  # FAO trade data
│   ├── logistics index/                         # World Bank logistics
│   ├── political stability index/               # Governance indicator
│   ├── regulatory quality/                      # Business environment
│   ├── population growth/                       # Demographic trends
│   ├── urban population/                        # Urbanization metrics
│   └── ubranization growth/                     # Urban growth rates
├── docs/                                    # Project documentation
│   └── WITSAPI_UserGuide.pdf               # Trade data API guide
├── preparation_et_le_nettoyage.ipynb       # Data preparation workflow
├── acp_et_clustering.ipynb                 # PCA and clustering analysis
├── requirements.txt                         # Python dependencies
└── README.md                                # This file
```

## Methodology

### Phase 1: Data Preparation (`preparation_et_le_nettoyage.ipynb`)

**Data Collection**:
- Load FAO datasets (production, trade, consumption)
- Retrieve World Bank indicators via API
- Standardize country codes using UN M49

**Data Cleaning**:
- Handle missing values through multiple strategies (imputation, filtering)
- Remove duplicate entries and resolve conflicts
- Standardize units (monetary values to USD, volumes to kg)
- Merge datasets on country codes

**Feature Engineering**:
- Calculate Import Dependency Ratio: `imports x 100/(production + imports - exports)`
- Calculate Self-Sufficiency Ratio: `production × 100/(production + imports − exports)`
- Compute Poultry Consumption Growth Potential
- Derive composite indicators for market attractiveness

**Data Validation**:
- Verify minimum 100 countries retained
- Confirm 60%+ global population coverage
- Check data quality and completeness

### Phase 2: PCA and Clustering (`acp_et_clustering.ipynb`)

**Principal Component Analysis (PCA)**:
- Standardize all variables (z-score normalization)
- Apply PCA for dimensionality reduction
- Analyze correlation circle to interpret variable relationships
- Examine scree plot to determine optimal components
- Project countries onto principal component space

**Outlier Detection**:
- Apply Isolation Forest algorithm
- Identify and analyze anomalous countries
- Document reasons for outlier status

**Hierarchical Clustering (HAC)**:
- Perform Hierarchical Ascendant Classification
- Generate dendrogram for visual interpretation
- Determine optimal number of clusters using dendrogram cuts
- Analyze cluster composition and characteristics

**K-Means Clustering**:
- Apply elbow method to determine optimal k
- Run K-means with selected number of clusters
- Compare results with HAC for validation
- Assign countries to final clusters

**Cluster Profiling**:
- Calculate cluster centroids and statistics
- Interpret business meaning of each cluster
- Rank countries within target clusters
- Generate recommendations for market selection

## Key Features

- **PESTEL-Driven Variable Selection**: Ensures comprehensive market assessment across all strategic dimensions
- **Multi-Source Data Integration**: Combines 15+ indicators from FAO and World Bank
- **Robust Statistical Methods**: PCA for dimensionality reduction, dual clustering approaches for validation
- **Business-Focused Interpretation**: Translates statistical findings into actionable market insights
- **Extensive Visualizations**: Correlation circles, scree plots, dendrograms, cluster maps, and country projections
- **Reproducible Workflow**: Clear separation between data preparation and analytical phases

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Jupyter Notebook or JupyterLab

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd "Do market study for chicken"
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Complete Analysis

**Step 1: Data Preparation**
```bash
jupyter notebook preparation_et_le_nettoyage.ipynb
```
Execute all cells sequentially to:
- Load raw data from all sources
- Clean and merge datasets
- Engineer features
- Export `cleaned_chicken_market_study_data.csv`

**Step 2: PCA and Clustering**
```bash
jupyter notebook acp_et_clustering.ipynb
```
Execute all cells to:
- Perform PCA and analyze results
- Run HAC and K-means clustering
- Generate cluster profiles
- Identify target markets

### Key Outputs

**Data Files**:
- `data/cleaned_chicken_market_study_data.csv`: Complete merged dataset ready for analysis

**Analytical Results**:
- PCA correlation circle showing variable relationships
- Scree plot for component selection
- Dendrogram from hierarchical clustering
- Cluster assignments for all countries
- Country rankings within optimal clusters

**Visualizations**:
- Correlation matrices
- Principal component projections
- Cluster scatter plots
- Box plots for cluster comparison
- Geographic distribution maps

## Analysis Results

### Market Segmentation

The clustering analysis identifies distinct country groups based on:

**Cluster Characteristics**:
- **High Import Dependency**: Countries with strong import needs and purchasing power
- **Emerging Markets**: Growing populations with increasing consumption potential
- **Self-Sufficient Markets**: High production capacity, limited import opportunities
- **Developing Markets**: Lower GDP but high growth potential

**Target Market Selection Criteria**:
- Import dependency ratio (higher is better for exports)
- Market size (population × consumption per capita)
- Economic capacity (GDP per capita)
- Growth potential (population growth + urbanization + consumption trends)
- Market accessibility (political stability + regulatory quality + logistics)

### Recommended Approach

1. Focus on clusters with high import dependency and strong economic indicators
2. Prioritize countries with favorable political and regulatory environments
3. Consider logistics infrastructure for distribution efficiency
4. Evaluate growth potential for long-term market development

## Technical Stack

**Data Processing**:
- `pandas`: Data manipulation and analysis
- `numpy`: Numerical computations
- `PySpark`: Large-scale data processing

**Statistical Analysis**:
- `scikit-learn`: PCA, clustering, outlier detection (via PySpark MLlib)
- `scipy`: Statistical functions and hierarchical clustering

**Visualization**:
- `matplotlib`: Base plotting library
- `seaborn`: Statistical visualizations

**Data Acquisition**:
- `requests`: HTTP requests for API calls
- `world_trade_data`: Trade statistics API
- `xmltodict`: Parse XML responses

**Development Environment**:
- `jupyter`: Interactive notebook environment
- `ipykernel`: Jupyter kernel for Python

See `requirements.txt` for complete dependency list with versions.

## Technical Notes

- All monetary values are in current US dollars
- Trade volumes standardized to kilograms for consistency
- Missing data handled through domain-appropriate imputation
- Features standardized (z-score) before PCA and clustering
- PCA retains components explaining 95% of cumulative variance
- Clustering performed on both PCA-transformed and raw standardized data
- Optimal cluster count validated through multiple methods (dendrogram, elbow, silhouette)

## Future Enhancements

- Incorporate time-series analysis for trend forecasting
- Add competitive analysis (other exporters in target markets)
- Include tariff and trade agreement data
- Develop interactive dashboard for market exploration
- Integrate real-time data updates via APIs

## Acknowledgments

- **FAO**: Food and Agriculture Organization for comprehensive agricultural data
- **World Bank**: Open data platform for economic and development indicators
- **La poule qui chante**: Project sponsorship and business context

---