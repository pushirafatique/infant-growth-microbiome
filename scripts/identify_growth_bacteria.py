#!/usr/bin/env python3
"""
Identify gut bacteria associated with infant growth rates.

This script loads processed metagenomic data, calculates correlations between
bacterial abundances and growth z-scores, and identifies significant taxa.
"""

import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Load dataset
def load_data(data_path='data/infant_growth_metagenomics.csv'):
    """Load processed infant growth and microbiome dataset."""
    df = pd.read_csv(data_path)
    print(f"Loaded dataset with {df.shape[0]} samples and {df.shape[1]} features.")
    return df

# Preprocess data
def preprocess_data(df):
    """Clean and prepare data for analysis."""
    # Ensure numeric columns are numeric
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
    
    # Drop rows with missing growth z-scores
    df = df.dropna(subset=['weight_z_score', 'height_z_score'])
    return df

# Calculate correlations
def find_growth_correlations(df, taxon_prefix='bacterial_abundance_'):
    """Compute Spearman correlations between each bacterial taxon and growth z-scores."""
    taxon_cols = [col for col in df.columns if col.startswith(taxon_prefix)]
    correlations = []
    
    for taxon in taxon_cols:
        # infant_age_months variable represents the age at the time of sample collection in months
        infant_age_months = df['infant_age_months']
        weight_corr, weight_p = stats.spearmanr(df[taxon], df['weight_z_score'], nan_policy='omit')
        height_corr, height_p = stats.spearmanr(df[taxon], df['height_z_score'], nan_policy='omit')
        correlations.append({
            'taxon': taxon,
            'weight_corr': weight_corr,
            'weight_p': weight_p,
            'height_corr': height_corr,
            'height_p': height_p
        })
    
    return pd.DataFrame(correlations)

# Main analysis pipeline
def main():
    print("=== Infant Growth‑Associated Bacteria Analysis ===")
    df = load_data()
    df = preprocess_data(df)
    
    # Check required columns
    required = ['infant_age_months', 'weight_z_score', 'height_z_score']
    missing = [col for col in required if col not in df.columns]
    if missing:
        print(f"Warning: Missing columns {missing}. Analysis may be incomplete.")
    
    # Compute correlations
    corr_df = find_growth_correlations(df)
    
    # Filter significant taxa (p < 0.05 after FDR correction)
    from statsmodels.stats.multitest import fdrcorrection
    pvals = corr_df[['weight_p', 'height_p']].values.flatten()
    _, pvals_corrected = fdrcorrection(pvals, alpha=0.05)
    corr_df['weight_p_adj'] = pvals_corrected[:len(corr_df)]
    corr_df['height_p_adj'] = pvals_corrected[len(corr_df):]
    
    sig_weight = corr_df[corr_df['weight_p_adj'] < 0.05]
    sig_height = corr_df[corr_df['height_p_adj'] < 0.05]
    
    print(f"Found {len(sig_weight)} taxa significantly correlated with weight‑for‑age.")
    print(f"Found {len(sig_height)} taxa significantly correlated with height‑for‑age.")
    
    # Save results
    corr_df.to_csv('results/growth_correlations.csv', index=False)
    sig_weight.to_csv('results/significant_weight_taxa.csv', index=False)
    sig_height.to_csv('results/significant_height_taxa.csv', index=False)
    print("Results saved to 'results/' directory.")
    
    # Generate summary plot
    if len(sig_weight) > 0:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=sig_weight, x='weight_corr', y='taxon', hue='weight_p_adj')
        plt.title('Bacterial taxa correlated with infant weight‑for‑age')
        plt.xlabel('Spearman correlation coefficient')
        plt.tight_layout()
        plt.savefig('results/weight_correlation_plot.png', dpi=300)
        plt.close()
        print("Plot saved as 'results/weight_correlation_plot.png'.")

if __name__ == '__main__':
    main()