# Infant Growth-Associated Gut Bacteria Project

## Overview
This project aims to identify specific gut bacteria associated with growth rates in infants. By analyzing stool samples from a longitudinal cohort of infants, we seek to understand how the gut microbiome influences growth trajectories and identify potential microbial biomarkers for healthy growth.

## Repository Structure
- `/data` – Contains processed datasets (metagenomic profiles, growth measurements)
- `/scripts` – Python scripts for data analysis and visualization
- `/environment.yml` – Conda environment specification for reproducibility

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/pushirafatique/infant-growth-microbiome.git
   cd infant-growth-microbiome
   ```
2. Set up the Conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate infant-growth-microbiome
   ```
3. Explore the data and scripts.

## Data
The processed dataset `infant_growth_metagenomics.csv` is available under the [Releases](https://github.com/pushirafatique/infant-growth-microbiome/releases) page (tag `v1.0-initial-analysis`). This dataset includes normalized bacterial abundance and growth z-scores.

## Analysis Scripts
- `identify_growth_bacteria.py` – Main script for identifying bacteria correlated with growth rates
- `visualize_results.py` – Generates plots and summary statistics
- `utils.py` – Helper functions for data processing

## Contributing
Please follow the lab's contribution guidelines. Create a new branch for each feature, and open a pull request for review.

## License
This project is licensed under the MIT License.