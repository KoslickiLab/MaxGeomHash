import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
import math


def f(alpha):
    ret_val = 1.0 / alpha
    return ret_val

def C(alpha):
    numerator = 2**(1.0 / (1.0 - alpha)) - 1.0
    denominator = 2**(alpha / (1.0 - alpha)) - 1.0
    return numerator / denominator

def C2(alpha):
    return 1.5 - 1.0 / math.log(2.0) + 1.0 / (alpha * math.log(2.0))

def C1(alpha):
    return 1.0 - 1.0 / math.log(2.0) + 1.0 / (alpha * math.log(2.0))


def plot_growth_against_multiple_alpha(data_filename, output_filename):
    df = pd.read_csv(data_filename, sep='\t', index_col=False)

    # filter by set_size % 10^5 == 0
    df = df[df['set_size'] % 100000 == 0]

    plt.figure(figsize=(4, 3))
    
    # set fontsize to 10
    plt.rcParams.update({'font.size': 10})

    # column names: set_size	amgs_sample_size_avg_alpha_0.25	amgs_sample_size_stddev_alpha_0.25	amgs_sample_size_avg_alpha_0.5	amgs_sample_size_stddev_alpha_0.5	amgs_sample_size_avg_alpha_0.75	amgs_sample_size_stddev_alpha_0.75
    # need to plot sample sizes for different k values against set_size with error bars as shaded region using stddev

    #alpha_values = [0.3, 0.4, 0.5]
    alpha_values = [0.4, 0.45, 0.5]
    colors = sns.color_palette("bright")
    markers = ['D', '<', 'o', '>', '^', 'v', 'D', 'P', 'X']
    colors = colors[4:7]
    markers = markers[4:7]

    for alpha, color, marker in zip(alpha_values, colors, markers):
        avg_col = f'amgs_sample_size_avg_alpha_{alpha}'
        stddev_col = f'amgs_sample_size_stddev_alpha_{alpha}'
        plt.plot(df['set_size'], df[avg_col], label=f'α={alpha}', color=color, marker=marker, markersize=4)
        plt.fill_between(df['set_size'], 
                         df[avg_col] - df[stddev_col], 
                         df[avg_col] + df[stddev_col], 
                         color=color, alpha=0.3)

    # also plot theoretical line: y = n^alpha for each alpha
    for alpha, color in zip(alpha_values, colors):
        theoretical_sizes_C = C(alpha) * df['set_size'] ** alpha
        plt.plot(df['set_size'], theoretical_sizes_C, linestyle='--', color='black', linewidth=0.75)

    # add the following to the legend: "Expected size" with a black dashed line, not the actual line 
    plt.plot([], [], linestyle='--', color='black', label='Expected size', linewidth=0.75)

    plt.xlabel('Original set size')
    plt.ylabel('Average $α$-MGH sample sizes')
    #plt.title('Growth of $α$-MGS Samples Against Set Size for Different $α$ Values')
    plt.legend(fontsize=8)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close()


def plot_growth_against_multiple_alpha_stddev(data_filename, output_filename):
    df = pd.read_csv(data_filename, sep='\t', index_col=False)

    # filter by set_size % 10^5 == 0
    df = df[df['set_size'] % 100000 == 0]

    plt.figure(figsize=(4, 3))
    
    # set fontsize to 10
    plt.rcParams.update({'font.size': 10})

    # column names: set_size	amgs_sample_size_avg_alpha_0.25	amgs_sample_size_stddev_alpha_0.25	amgs_sample_size_avg_alpha_0.5	amgs_sample_size_stddev_alpha_0.5	amgs_sample_size_avg_alpha_0.75	amgs_sample_size_stddev_alpha_0.75
    # need to plot sample sizes for different k values against set_size with error bars as shaded region using stddev

    #alpha_values = [0.3, 0.4, 0.5]
    alpha_values = [0.4, 0.45, 0.5]
    k_values = [70, 80, 90, 100]
    colors = sns.color_palette("bright")
    markers = ['D', '<', 'o', '>', '^', 'v', 'D', 'P', 'X']
    colors = colors[4:7]
    markers = markers[4:7]

    for alpha, color, marker in zip(alpha_values, colors, markers):
        stddev_col = f'amgs_sample_size_stddev_alpha_{alpha}'
        plt.plot(df['set_size'], df[stddev_col], label=f'α={alpha}', color=color, marker=marker, markersize=4)

    # plot theoretical line: y = n^alpha for each alpha
    for alpha, color, marker in zip(alpha_values, colors, markers):
        theoretical_stddev = (df['set_size'] ** alpha) ** 0.5
        plt.plot(df['set_size'], theoretical_stddev, linestyle='--', color=color, linewidth=0.75, label=f'sqrt(n^α), α={alpha}', marker=marker, markersize=4)

    plt.xlabel('Original set size')
    plt.ylabel('Stddev of $α$-MGH sample sizes')
    #plt.title('Growth of $α$-MGS Samples Against Set Size for Different $α$ Values')
    plt.legend(fontsize=8)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close()
    
    
if __name__ == "__main__":
    input_file = os.path.join('results', 'results_growth_of_amgs_varying_alpha')
    output_file = os.path.join('plots', 'growth_of_alpha_mgs_samples.pdf')
    plot_growth_against_multiple_alpha(input_file, output_file)