import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

if __name__ == "__main__":
    results_file = os.path.join("results", "results_accuracy_by_varying_jaccard_alpha_MGS")
    output_file = os.path.join("plots", "accuracy_jaccard_by_varying_jaccard_alpha_MGS.png")
    df = pd.read_csv(results_file, sep='\t', index_col=False)
    # columns: k, True_Jaccard, Estimated_Jaccard

    df = df.sample(frac=0.2, random_state=42)
    
    # plot true jaccard vs estimated jaccard for each method and parameter
    # method names: MGS, alpha-MGS. each method has four parameters
    alpha_values_tested = [0.4, 0.45, 0.5]
    colors = sns.color_palette("tab10")
    markers = ['D', '<', 'o', '>', '^', 'v', 'D', 'P', 'X']
    colors = sns.color_palette("bright")[4:]
    markers = markers[4:]
    alpha_values_to_plot = [1.0, 0.8, 0.5]
    markersize = 2

    plt.figure(figsize=(4, 3))
    color_idx = 0
    for alpha in alpha_values_tested:
        subset = df[df['alpha'] == alpha]
        plt.scatter(subset['True_Jaccard'], subset['Estimated_Jaccard'], 
                    label=f'α-MaxGeomHash (α={alpha})', color=colors[color_idx], 
                    alpha=alpha_values_to_plot[color_idx], s=markersize, 
                    marker=markers[color_idx])
        color_idx += 1
    
    # plot a diagonal line y=x
    max_val = df['True_Jaccard'].max()
    print(max_val)
    plt.plot([0, max_val], [0, max_val], 'k--', label='True Jaccard', linewidth=0.5)
    plt.xlabel('True Jaccard')
    plt.ylabel('Estimated Jaccard')
    plt.legend(fontsize=8)

    # change the alpha values in the legend to 1.0
    leg = plt.gca().get_legend()
    for handle in leg.legend_handles:
        handle.set_alpha(1.0)

    #plt.grid(True, alpha=0.3)
    # export with high resolution
    plt.tight_layout()
    plt.savefig(output_file, dpi=500)
    plt.close()
    
    print("Plot saved to: ", output_file )
    
    # now calculate the R^2 value for each method and parameter
    for alpha in alpha_values_tested:
        subset = df[df['alpha'] == alpha]
        r2 = np.corrcoef(subset['True_Jaccard'], subset['Estimated_Jaccard'])[0, 1] ** 2
        print(f'R^2 for α-MaxGeomHash (α={alpha}): {r2:.4f}')