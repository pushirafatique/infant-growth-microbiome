# Data Directory

This directory contains processed datasets for the infant growth microbiome project.

## Main Dataset
The primary dataset `infant_growth_metagenomics.csv` is available under the [Releases](https://github.com/pushirafatique/infant-growth-microbiome/releases) page (tag `v1.0-initial-analysis`). Please download it and place it here for local analysis.

## Data Description
- **infant_id**: Unique identifier for each infant
- **sample_month**: Month of sample collection (0 = birth)
- **infant_age_months**: Age at sample collection in months (calculated from birth)
- **weight_z_score**: WHO weight-for-age z-score
- **height_z_score**: WHO height-for-age z-score
- **bacterial_abundance_***: Normalized abundance of bacterial taxa (columns)

## Usage
Run the analysis scripts from the parent directory; they expect the dataset in `data/infant_growth_metagenomics.csv`.