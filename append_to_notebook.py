import json
import pandas as pd

notebook_path = 'acp_et_clustering_v2.ipynb'

try:
    with open(notebook_path, 'r') as f:
        notebook = json.load(f)

    new_cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Target Country Selection\n",
                "Based on the cluster analysis, **Cluster 0** has been identified as the optimal cluster due to its high stability, wealth, and market potential. We will now select the best country from this cluster."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Filter for Cluster 0\n",
                "target_cluster = 0\n",
                "target_countries = cluster_analysis[cluster_analysis['Cluster'] == target_cluster].copy()\n",
                "\n",
                "print(f\"Number of countries in Cluster {target_cluster}: {len(target_countries)}\")\n",
                "print(target_countries['Country Name'].values)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "from sklearn.preprocessing import MinMaxScaler\n",
                "\n",
                "# Define ranking metrics and weights for country selection\n",
                "# We want high import quantity, high growth potential, stability, and wealth.\n",
                "ranking_weights = {\n",
                "    'Import Quantity (kg)': 0.3,\n",
                "    'Poultry Consumption Growth Potential': 0.2,\n",
                "    'GDP per Capita (current US$)': 0.2,\n",
                "    'Political Stability Index': 0.15,\n",
                "    'Regulatory Quality Index': 0.15\n",
                "}\n",
                "\n",
                "# Normalize metrics for the target countries\n",
                "scaler = MinMaxScaler()\n",
                "ranking_metrics = list(ranking_weights.keys())\n",
                "normalized_target = pd.DataFrame(scaler.fit_transform(target_countries[ranking_metrics]), \n",
                "                                 columns=ranking_metrics, \n",
                "                                 index=target_countries.index)\n",
                "\n",
                "# Calculate Country Score\n",
                "target_countries['Country_Score'] = 0\n",
                "for metric, weight in ranking_weights.items():\n",
                "    target_countries['Country_Score'] += normalized_target[metric] * weight\n",
                "\n",
                "# Sort by score\n",
                "top_candidates = target_countries.sort_values('Country_Score', ascending=False)\n",
                "\n",
                "# Display top 10\n",
                "cols_to_show = ['Country Name', 'Country_Score'] + ranking_metrics\n",
                "top_candidates[cols_to_show].head(10)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Visualize Top 5 Candidates\n",
                "top5 = top_candidates.head(5)\n",
                "\n",
                "fig = px.bar(top5, x='Country Name', y='Country_Score',\n",
                "             title='Top 5 Target Countries in Cluster 0',\n",
                "             color='Country_Score',\n",
                "             color_continuous_scale='Viridis')\n",
                "fig.show()\n",
                "\n",
                "best_country = top5.iloc[0]['Country Name']\n",
                "print(f\"\\nThe recommended target country is: {best_country}\")"
            ]
        }
    ]

    notebook['cells'].extend(new_cells)

    with open(notebook_path, 'w') as f:
        json.dump(notebook, f, indent=1)

    print("Notebook updated successfully.")

except Exception as e:
    print(f"Error updating notebook: {e}")
