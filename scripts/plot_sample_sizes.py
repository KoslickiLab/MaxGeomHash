import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
    
    
    
def plot_growth_against_multiple_k(data_filename, output_filename):
    df = pd.read_csv(data_filename, sep='\t', index_col=False)

    # filter by set_size % 10^5 == 0
    df = df[df['set_size'] % 100000 == 0]

    plt.figure(figsize=(4, 3))

    # set fontsize to 10
    plt.rcParams.update({'font.size': 10})
    
    # column names: set_size	mgs_sample_size_avg_k_25	mgs_sample_size_stddev_k_25	mgs_sample_size_avg_k_50	mgs_sample_size_stddev_k_50	mgs_sample_size_avg_k_100	mgs_sample_size_stddev_k_100	mgs_sample_size_avg_k_200	mgs_sample_size_stddev_k_200	mgs_sample_size_avg_k_400	mgs_sample_size_stddev_k_400	mgs_sample_size_avg_k_800	mgs_sample_size_stddev_k_800
    # need to plot sample sizes for different k values against set_size with error bars as shaded region using stddev

    #k_values = [25, 50, 100, 200, 400, 800]
    #k_values = [200, 400, 800]
    k_values = [70, 80, 90, 100]
    k_values = [70, 80, 90, 100]
    colors = sns.color_palette("bright")
    markers = ['D', '<', 'o', '>', '^', 'v', 'D', 'P', 'X']
    colors = colors[0:4]
    markers = markers[0:4]

    # also plot theoretical line: y = k * long(n/k) for each k
    for k, color in zip(k_values, colors):
        theoretical_sizes = k * np.log2(df['set_size'] / k) + k
        plt.plot(df['set_size'], theoretical_sizes, linestyle='--', color='black', linewidth=0.75)

    for k, color, marker in zip(k_values, colors, markers):
        avg_col = f'mgs_sample_size_avg_k_{k}'
        stddev_col = f'mgs_sample_size_stddev_k_{k}'
        plt.plot(df['set_size'], df[avg_col], label=f'$b$={k}', color=color, marker=marker, markersize=4)
        plt.fill_between(df['set_size'], 
                         df[avg_col] - df[stddev_col], 
                         df[avg_col] + df[stddev_col], 
                         color=color, alpha=0.3)

    # add the following to the legend: "Expected size" with a black dashed line, not the actual line 
    plt.plot([], [], linestyle='--', color='black', label='Expected size', linewidth=0.75)
        
    plt.xlabel('Original set size')
    plt.ylabel('Average MGH sample sizes')
    #plt.title('Growth of MaxGeom Sample Sizes Against Original Set Size for Different k Values')
    plt.legend(fontsize=6)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close()


def plot_growth_against_multiple_k_stddev(data_filename, output_filename):
    df = pd.read_csv(data_filename, sep='\t', index_col=False)

    # filter by set_size % 10^5 == 0
    df = df[df['set_size'] % 100000 == 0]

    plt.figure(figsize=(4, 3))

    # set fontsize to 10
    plt.rcParams.update({'font.size': 10})
    
    # column names: set_size	mgs_sample_size_avg_k_25	mgs_sample_size_stddev_k_25	mgs_sample_size_avg_k_50	mgs_sample_size_stddev_k_50	mgs_sample_size_avg_k_100	mgs_sample_size_stddev_k_100	mgs_sample_size_avg_k_200	mgs_sample_size_stddev_k_200	mgs_sample_size_avg_k_400	mgs_sample_size_stddev_k_400	mgs_sample_size_avg_k_800	mgs_sample_size_stddev_k_800
    # need to plot sample sizes for different k values against set_size with error bars as shaded region using stddev

    #k_values = [25, 50, 100, 200, 400, 800]
    #k_values = [200, 400, 800]
    k_values = [70, 80, 90, 100]
    colors = ['#a6cee3','#b2df8a', '#1f78b4', '#33a02c','#fb9a99','#e31a1c','#fdbf6f','#ff7f00','#ab93b7']
    markers = ['D', '<', 'o', '>', '^', 'v', '*', 'P', 'X']
    colors = colors[0:4]
    markers = markers[0:4]

    for k, color, marker in zip(k_values, colors, markers):
        stddev_col = f'mgs_sample_size_stddev_k_{k}'
        plt.plot(df['set_size'], df[stddev_col], label=f'k={k}', color=color, marker=marker, markersize=4)

        # also plot theoretical line: y = k for each k
        theoretical_stddev = [k**0.5 for _ in range(len(df['set_size']))]
        plt.plot(df['set_size'], theoretical_stddev, linestyle='--', color=color, linewidth=0.75, label=f'sqrt(k), k={k}', marker=marker, markersize=4)
    
    plt.xlabel('Original set size')
    plt.ylabel('Stddev of MGH sample sizes')
    #plt.title('Growth of MaxGeom Sample Sizes Against Original Set Size for Different k Values')
    plt.legend(fontsize=6)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close()


if __name__ == "__main__":
    
    data_file_k = os.path.join('results', 'results_growth_of_mgs_varying_k')
    output_file_k = os.path.join('plots', 'growth_against_multiple_k.pdf')
    plot_growth_against_multiple_k(data_file_k, output_file_k)
