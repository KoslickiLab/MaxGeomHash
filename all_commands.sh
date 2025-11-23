#export PATH=/scratch/mbr5797/kmer-sketch/bin:$PATH

# basic implementation test
python scripts/expt_basic_implementation.py

# growth against data size (against FMH)
python scripts/expt_growth_of_samples_against_fmh.py > results/results_growth_of_samples

# growth against k
python scripts/expt_growth_of_mgs_varying_k.py > results/results_growth_of_mgs_varying_k

# plot basic MGS results
python scripts/plot_sample_sizes.py

# growth of alpha-MGS samples against data size
python scripts/expt_growth_of_amgs_varying_alpha.py > results/results_growth_of_amgs_varying_alpha

# plot alpha-MGS results
python scripts/plot_alpha_MGS_sample_sizes.py

# experiment for accuracy of jaccard estimation with refining
python scripts/expt_accuracy_with_refining.py

# plot accuracy results with refining
python scripts/plot_accuracy_jaccard_with_refining.py

# vary jaccard from 0 to 1, see how accuracy changes
python scripts/expt_vary_jaccard.py

# plot accuracy results by varying jaccard
python scripts/plot_accuracy_by_varying_jaccard.py

# vary jaccard from 0 to 1, see how accuracy changes for alpha-MGS
python scripts/expt_vary_jaccard_alpha_MGS.py

# plot accuracy results by varying jaccard for alpha-MGS
python scripts/plot_accuracy_by_varying_jaccard_alpha_MGS.py

# fixed similarity, vary set sizes experiments using MGS
# jaccard and cosine, k (r parameter) = 200
python scripts/expt_fixed_similarity_vary_set_size.py --t 0.1 --metric jaccard --k 100 --seeds 500 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_MGS_k100_t0.1.tsv
python scripts/expt_fixed_similarity_vary_set_size.py --t 0.2 --metric jaccard --k 100 --seeds 500 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_MGS_k100_t0.2.tsv
python scripts/expt_fixed_similarity_vary_set_size.py --t 0.3 --metric jaccard --k 100 --seeds 500 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_MGS_k100_t0.3.tsv
python scripts/expt_fixed_similarity_vary_set_size.py --t 0.4 --metric jaccard --k 100 --seeds 500 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_MGS_k100_t0.4.tsv
python scripts/expt_fixed_similarity_vary_set_size.py --t 0.5 --metric jaccard --k 100 --seeds 500 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_MGS_k100_t0.5.tsv
python scripts/expt_fixed_similarity_vary_set_size.py --t 0.1 --metric cosine --k 100 --seeds 1000 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_MGS_k100_t0.1.tsv
python scripts/expt_fixed_similarity_vary_set_size.py --t 0.2 --metric cosine --k 100 --seeds 1000 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_MGS_k100_t0.2.tsv
python scripts/expt_fixed_similarity_vary_set_size.py --t 0.3 --metric cosine --k 100 --seeds 1000 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_MGS_k100_t0.3.tsv
python scripts/expt_fixed_similarity_vary_set_size.py --t 0.4 --metric cosine --k 100 --seeds 1000 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_MGS_k100_t0.4.tsv
python scripts/expt_fixed_similarity_vary_set_size.py --t 0.5 --metric cosine --k 100 --seeds 1000 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_MGS_k100_t0.5.tsv

# fixed similarity, vary set sizes experiments using FMH
# jaccard and cosine, scale=0.001
python scripts/expt_fixed_similarity_vary_set_size_FMH.py --t 0.1 --metric jaccard --s 0.001 --seeds 200 --growth x2 --seed 42 --out results/expt_fixed_jaccard_vary_set_size_jaccard_FMH_s0.001_t0.1.tsv
python scripts/expt_fixed_similarity_vary_set_size_FMH.py --t 0.2 --metric jaccard --s 0.001 --seeds 200 --growth x2 --seed 42 --out results/expt_fixed_jaccard_vary_set_size_jaccard_FMH_s0.001_t0.2.tsv
python scripts/expt_fixed_similarity_vary_set_size_FMH.py --t 0.3 --metric jaccard --s 0.001 --seeds 200 --growth x2 --seed 42 --out results/expt_fixed_jaccard_vary_set_size_jaccard_FMH_s0.001_t0.3.tsv
python scripts/expt_fixed_similarity_vary_set_size_FMH.py --t 0.4 --metric jaccard --s 0.001 --seeds 200 --growth x2 --seed 42 --out results/expt_fixed_jaccard_vary_set_size_jaccard_FMH_s0.001_t0.4.tsv
python scripts/expt_fixed_similarity_vary_set_size_FMH.py --t 0.5 --metric jaccard --s 0.001 --seeds 200 --growth x2 --seed 42 --out results/expt_fixed_jaccard_vary_set_size_jaccard_FMH_s0.001_t0.5.tsv
python scripts/expt_fixed_similarity_vary_set_size_FMH.py --t 0.1 --metric cosine --s 0.001 --seeds 200 --growth x2 --seed 42 --out results/expt_fixed_cosine_vary_set_size_cosine_FMH_s0.001_t0.1.tsv
python scripts/expt_fixed_similarity_vary_set_size_FMH.py --t 0.2 --metric cosine --s 0.001 --seeds 200 --growth x2 --seed 42 --out results/expt_fixed_cosine_vary_set_size_cosine_FMH_s0.001_t0.2.tsv
python scripts/expt_fixed_similarity_vary_set_size_FMH.py --t 0.3 --metric cosine --s 0.001 --seeds 200 --growth x2 --seed 42 --out results/expt_fixed_cosine_vary_set_size_cosine_FMH_s0.001_t0.3.tsv
python scripts/expt_fixed_similarity_vary_set_size_FMH.py --t 0.4 --metric cosine --s 0.001 --seeds 200 --growth x2 --seed 42 --out results/expt_fixed_cosine_vary_set_size_cosine_FMH_s0.001_t0.4.tsv
python scripts/expt_fixed_similarity_vary_set_size_FMH.py --t 0.5 --metric cosine --s 0.001 --seeds 200 --growth x2 --seed 42 --out results/expt_fixed_cosine_vary_set_size_cosine_FMH_s0.001_t0.5.tsv

# fixed similarity, vary set sizes experiments using alpha-MGS
# jaccard and cosine, alpha=0.25
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.1 --metric jaccard --alpha 0.25 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_aMGS_alpha0.25_t0.1.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.2 --metric jaccard --alpha 0.25 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_aMGS_alpha0.25_t0.2.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.3 --metric jaccard --alpha 0.25 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_aMGS_alpha0.25_t0.3.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.4 --metric jaccard --alpha 0.25 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_aMGS_alpha0.25_t0.4.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.5 --metric jaccard --alpha 0.25 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_aMGS_alpha0.25_t0.5.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.1 --metric cosine --alpha 0.25 --seeds 200 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_aMGS_alpha0.25_t0.1.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.2 --metric cosine --alpha 0.25 --seeds 200 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_aMGS_alpha0.25_t0.2.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.3 --metric cosine --alpha 0.25 --seeds 200 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_aMGS_alpha0.25_t0.3.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.4 --metric cosine --alpha 0.25 --seeds 200 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_aMGS_alpha0.25_t0.4.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.5 --metric cosine --alpha 0.25 --seeds 200 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_aMGS_alpha0.25_t0.5.tsv

# jaccard and cosine, alpha=0.4
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.1 --metric jaccard --alpha 0.4 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_aMGS_alpha0.4_t0.1.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.2 --metric jaccard --alpha 0.4 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_aMGS_alpha0.4_t0.2.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.3 --metric jaccard --alpha 0.4 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_aMGS_alpha0.4_t0.3.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.4 --metric jaccard --alpha 0.4 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_aMGS_alpha0.4_t0.4.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.5 --metric jaccard --alpha 0.4 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_aMGS_alpha0.4_t0.5.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.1 --metric cosine --alpha 0.4 --seeds 200 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_aMGS_alpha0.4_t0.1.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.2 --metric cosine --alpha 0.4 --seeds 200 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_aMGS_alpha0.4_t0.2.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.3 --metric cosine --alpha 0.4 --seeds 200 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_aMGS_alpha0.4_t0.3.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.4 --metric cosine --alpha 0.4 --seeds 200 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_aMGS_alpha0.4_t0.4.tsv
python scripts/expt_fixed_similarity_vary_set_size_aMGS.py --t 0.5 --metric cosine --alpha 0.4 --seeds 200 --growth x2 --out results/expt_fixed_cosine_vary_set_size_cosine_aMGS_alpha0.4_t0.5.tsv

# fixed jaccard, vary set sizes, estimate using MinHash
python scripts/expt_fixed_similarity_vary_set_size_MH.py --t 0.1 --metric jaccard --k 500 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_MH_k500_t0.1.tsv
python scripts/expt_fixed_similarity_vary_set_size_MH.py --t 0.2 --metric jaccard --k 500 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_MH_k500_t0.2.tsv
python scripts/expt_fixed_similarity_vary_set_size_MH.py --t 0.3 --metric jaccard --k 500 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_MH_k500_t0.3.tsv
python scripts/expt_fixed_similarity_vary_set_size_MH.py --t 0.4 --metric jaccard --k 500 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_MH_k500_t0.4.tsv
python scripts/expt_fixed_similarity_vary_set_size_MH.py --t 0.5 --metric jaccard --k 500 --seeds 200 --growth x2 --out results/expt_fixed_jaccard_vary_set_size_jaccard_MH_k500_t0.5.tsv


# fixed jaccard experiment for even larger sets 
# uses cpp implementation 
expt_growth --t 0.5 --metric jaccard --seeds 50 --steps 10 --growth x2 --out results/fixed_jaccard_expt_amgh_t0.5_a0.45 --algo alphamaxgeom --alpha 0.45 --base_n 100000
expt_growth --t 0.5 --metric jaccard --seeds 50 --steps 10 --growth x2 --out results/fixed_jaccard_expt_mh_t0.5_k1000 --algo bottomk --k 1000 --base_n 100000
expt_growth --t 0.5 --metric jaccard --seeds 50 --steps 10 --growth x2 --out results/fixed_jaccard_expt_mgh_t0.5_k90 --algo maxgeom --k 90 --base_n 100000
expt_growth --t 0.5 --metric jaccard --seeds 50 --steps 10 --growth x2 --out results/fixed_jaccard_expt_fmh_t0.5_s0.001 --algo fracminhash --scale 0.001 --base_n 100000


# use 500 trials
expt_growth --t 0.5 --metric jaccard --seeds 500 --steps 10 --growth x2 --out results/fixed_jaccard_expt_amgh_t0.5_a0.45 --algo alphamaxgeom --alpha 0.45 --base_n 100000
expt_growth --t 0.5 --metric jaccard --seeds 500 --steps 10 --growth x2 --out results/fixed_jaccard_expt_mh_t0.5_k1000 --algo bottomk --k 1000 --base_n 100000
expt_growth --t 0.5 --metric jaccard --seeds 500 --steps 10 --growth x2 --out results/fixed_jaccard_expt_mgh_t0.5_k90 --algo maxgeom --k 90 --base_n 100000
expt_growth --t 0.5 --metric jaccard --seeds 500 --steps 10 --growth x2 --out results/fixed_jaccard_expt_fmh_t0.5_s0.001 --algo fracminhash --scale 0.001 --base_n 100000


#################################################
# Real-world data experiments
#################################################


# downloading mammal genomes: Human, Chimpanzee, Mouse, Rat, Dog, Cat, Cow, Pig, Horse, Opossum
mkdir -p data
cd data
wget -c https://ftp.ensembl.org/pub/release-112/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.toplevel.fa.gz
wget -c https://ftp.ensembl.org/pub/release-112/fasta/pan_troglodytes/dna/Pan_troglodytes.Pan_tro_3.0.dna.toplevel.fa.gz
wget -c https://ftp.ensembl.org/pub/release-112/fasta/mus_musculus/dna/Mus_musculus.GRCm39.dna_rm.toplevel.fa.gz
wget -c https://ftp.ensembl.org/pub/release-112/fasta/rattus_norvegicus/dna/Rattus_norvegicus.mRatBN7.2.dna.toplevel.fa.gz
wget -c https://ftp.ensembl.org/pub/release-112/fasta/canis_lupus_familiaris/dna/Canis_lupus_familiaris.ROS_Cfam_1.0.dna.toplevel.fa.gz
wget -c https://ftp.ensembl.org/pub/release-112/fasta/felis_catus/dna/Felis_catus.Felis_catus_9.0.dna_rm.toplevel.fa.gz
wget -c https://ftp.ensembl.org/pub/release-112/fasta/bos_taurus/dna/Bos_taurus.ARS-UCD1.3.dna.toplevel.fa.gz
wget -c https://ftp.ensembl.org/pub/release-112/fasta/sus_scrofa/dna/Sus_scrofa.Sscrofa11.1.dna.toplevel.fa.gz
wget -c https://ftp.ensembl.org/pub/release-112/fasta/equus_caballus/dna/Equus_caballus.EquCab3.0.dna.toplevel.fa.gz
wget -c https://ftp.ensembl.org/pub/release-112/fasta/monodelphis_domestica/dna/Monodelphis_domestica.ASM229v1.dna.toplevel.fa.gz

gunzip *.gz
find $(pwd) -type f -name '*.fa' > genome_list
cd ..

# sketch commands (manually record CPU time, peak memory usage, and disk space for the sketch files)
# all sketch files are created in data
/usr/bin/time -v python scripts/parallel_sketch.py data/genome_list --threads 10 --algo maxgeom --k 90
/usr/bin/time -v python scripts/parallel_sketch.py data/genome_list --threads 10 --algo fracminhash --scale 0.001
/usr/bin/time -v python scripts/parallel_sketch.py data/genome_list --threads 10 --algo alphamaxgeom --alpha 0.45
/usr/bin/time -v python scripts/parallel_sketch.py data/genome_list --threads 10 --algo bottomk --k 1000

# finding disk-space
find . -type f -name "*.maxgeom.sketch" -print0 | du --files0-from=- -ch | tail -1
find . -type f -name "*.alphamaxgeom.sketch" -print0 | du --files0-from=- -ch | tail -1
find . -type f -name "*.bottomk.sketch" -print0 | du --files0-from=- -ch | tail -1
find . -type f -name "*.fracminhash.sketch" -print0 | du --files0-from=- -ch | tail -1

# finding pairwise similarities 
/usr/bin/time -v pwsimilarity --metric jaccard --output results/pw_jaccard_maxgeom.csv data/*.maxgeom.sketch
/usr/bin/time -v pwsimilarity --metric jaccard --output results/pw_jaccard_fracminhash.csv data/*.fracminhash.sketch
/usr/bin/time -v pwsimilarity --metric jaccard --output results/pw_jaccard_alphamaxgeom.csv data/*.alphamaxgeom.sketch
/usr/bin/time -v pwsimilarity --metric jaccard --output results/pw_jaccard_bottomk.csv data/*.bottomk.sketch

# tree building from pairwise distances
python scripts/analyze_pw_similarity_scores.py --in results/pw_jaccard_maxgeom.csv --out-newick results/phylo_tree_mammals_maxgeom.nwk --out-plot plots/phylo_tree_mammals_maxgeom.pdf --treat-as similarity --similarity-to-distance mutrate --kmer-size 31
python scripts/analyze_pw_similarity_scores.py --in results/pw_jaccard_fracminhash.csv --out-newick results/phylo_tree_mammals_fracminhash.nwk --out-plot plots/phylo_tree_mammals_fracminhash.pdf --treat-as similarity --similarity-to-distance mutrate --kmer-size 31
python scripts/analyze_pw_similarity_scores.py --in results/pw_jaccard_alphamaxgeom.csv --out-newick results/phylo_tree_mammals_alphamaxgeom.nwk --out-plot plots/phylo_tree_mammals_alphamaxgeom.pdf --treat-as similarity --similarity-to-distance mutrate --kmer-size 31
python scripts/analyze_pw_similarity_scores.py --in results/pw_jaccard_bottomk.csv --out-newick results/phylo_tree_mammals_minhash.nwk --out-plot plots/phylo_tree_mammals_minhash.pdf --treat-as similarity --similarity-to-distance mutrate --kmer-size 31

# trees are to be beautified using Illustrator later

# only the plotting commands
python scripts/plot_sample_sizes.py 
python scripts/plot_alpha_MGS_sample_sizes.py
python scripts/plot_accuracy_by_varying_jaccard.py
python scripts/plot_accuracy_by_varying_jaccard_alpha_MGS.py
python scripts/plot_fixed_t_results.py --t 0.5 --alpha 0.45 --k_mgh 90 --scale 0.001 --k_mh 1000 --metric jaccard

# these images are later stitched and labeled using Illustrator