from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import os
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Plot fixed t (similarity) results.")
    parser.add_argument('--t', type=float, required=True, help='Similarity value t, for which expt was done.')
    parser.add_argument('--alpha', type=float, required=True, help='Alpha value for AlphaMaxGeom.')
    parser.add_argument('--k_mgh', type=int, required=True, help='r value for MaxGeom.')
    parser.add_argument('--scale', type=float, required=True, help='Scale factor value for FMH.')
    parser.add_argument('--k_mh', type=int, required=True, help='k value for MinHash (num permutations).')
    parser.add_argument('--metric', type=str, choices=['cosine', 'jaccard'], required=True, help='What similarity metric to consider.')
    
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    t = args.t
    alpha = args.alpha
    k_mgh = args.k_mgh
    scale = args.scale
    k_mh = args.k_mh
    metric = args.metric
    
    # read data
    filename_mgs = f"results/fixed_{metric}_expt_mgh_t{t}_k{k_mgh}"
    filename_amg = f"results/fixed_{metric}_expt_amgh_t{t}_a{alpha}"
    filename_fmh = f"results/fixed_{metric}_expt_fmh_t{t}_s{scale}"
    filename_mh = f"results/fixed_{metric}_expt_mh_t{t}_k{k_mh}"

    df_mgs = pd.read_csv(filename_mgs, sep="\t")
    df_amg = pd.read_csv(filename_amg, sep="\t")
    df_fmh = pd.read_csv(filename_fmh, sep="\t")
    if metric == 'jaccard':
        df_mh = pd.read_csv(filename_mh, sep="\t")

    # in each df, there is a column '|A|', 'mean_sample_size_A', 'mse'
    # create two plots: (1) mean sample size vs |A|, (2) mse vs |A|

    # (1): output plot name: fixed_{metric}_vary_set_size_sample_size_t{t}.pdf
    output_plot1 = f"plots/fixed_{metric}_vary_set_size_sample_size_t{t}.pdf"

    colors = sns.color_palette("bright")
    markers = ['D', '<', 'o', '>', '^', 'v', 'D', 'P', 'X']

    plt.figure(figsize=(4, 3))
    # set fontsize to 10
    plt.rcParams.update({'font.size': 10})

    minhash_color_index = 1
    fracminhash_color_index = 3
    maxgeom_color_index = 2
    alphamaxgeom_color_index = 5

    if metric == 'jaccard':
        sns.lineplot(data=df_mh, x='|A|', y='mean_sample_size_A', label=f'MinHash ($k$={k_mh})', marker=markers[8], color=colors[minhash_color_index])
    sns.lineplot(data=df_fmh, x='|A|', y='mean_sample_size_A', label=f'FracMinHash ($s$={scale})', marker=markers[7], color=colors[fracminhash_color_index])
    sns.lineplot(data=df_mgs, x='|A|', y='mean_sample_size_A', label=f'MaxGeomHash ($b$={k_mgh})', marker=markers[2], color=colors[maxgeom_color_index])
    sns.lineplot(data=df_amg, x='|A|', y='mean_sample_size_A', label=f'α-MaxGeomHash (α={alpha})', marker=markers[5], color=colors[alphamaxgeom_color_index])

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Set sizes')
    plt.ylabel('Mean sketch size')
    # decrease legend font size
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.grid(True, alpha=0.3)
    plt.savefig(output_plot1)
    plt.close()

    # (2): output plot name: fixed_{metric}_vary_set_size_mse_t{t}.pdf
    output_plot2 = f"plots/fixed_{metric}_vary_set_size_mse_t{t}.pdf"
    plt.figure(figsize=(4, 3))
    
    if metric == 'jaccard':
        sns.lineplot(data=df_mh, x='|A|', y='mse', label=f'MinHash ($k$={k_mh})', marker=markers[8], color=colors[minhash_color_index])
    sns.lineplot(data=df_fmh, x='|A|', y='mse', label=f'FracMinHash ($s$={scale})', marker=markers[7], color=colors[fracminhash_color_index])
    sns.lineplot(data=df_mgs, x='|A|', y='mse', label=f'MaxGeomHash ($b$={k_mgh})', marker=markers[2], color=colors[maxgeom_color_index])
    sns.lineplot(data=df_amg, x='|A|', y='mse', label=f'α-MaxGeomHash (α={alpha})', marker=markers[5], color=colors[alphamaxgeom_color_index])

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Set sizes')
    plt.ylabel('Mean Squared Error (MSE)')
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.grid(True, alpha=0.3)
    plt.savefig(output_plot2)
    plt.close()