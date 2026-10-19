from samplers import FracMinHashSketch, MaxGeomSample
import random
from helpers.string_utils import generate_random_strings


if __name__ == "__main__":
    # FMH sketch with scale 0.1
    scale = 0.1
    fmh_sketch = FracMinHashSketch(scale)

    # Sample data: random 1M strings over alphabet
    data = generate_random_strings(100000, 10)
    fmh_sketch.add_many_items(data)

    print(f"Scale: {fmh_sketch.get_scale()}")
    print(f"Number of hashes in sketch: {len(fmh_sketch)}")

    # MaxGeomSampling with k=100, w=64
    max_geom_sample = MaxGeomSample(k=100, w=64, seed=42)
    max_geom_sample.add_many_items(data)
    print(f"MaxGeomSampling buckets: {len(max_geom_sample._buckets)}")
    # print number of items in all buckets
    print(f"Total items in MaxGeomSampling: {len(max_geom_sample)}")

    # now show the number of items in each bucket
    bucket_i_values = list(max_geom_sample._buckets.keys())
    bucket_i_values.sort()
    for i in bucket_i_values:
        print(f"Bucket {i}: {len(max_geom_sample._buckets[i])} items")
    
    # check equality
    another_sample = MaxGeomSample(k=100, w=64, seed=42)
    another_sample.add_many_items(data)
    print(f"Samples equal: {max_geom_sample == another_sample}")
    
    # randomly shuffle data 10 times and check equality
    all_equal = True
    for _ in range(10):
        random.shuffle(data)
        temp_sample = MaxGeomSample(k=100, w=64, seed=42)
        temp_sample.add_many_items(data)
        if max_geom_sample != temp_sample:
            all_equal = False
            break
    print(f"Samples equal after 10 random shuffles: {all_equal}")
    
    # randomly select half of data and create another sample
    data2 = random.sample(data, len(data) // 2)
    another_sample = MaxGeomSample(k=100, w=64, seed=42)
    another_sample.add_many_items(data2)
    
    # compute true jaccard index between data sets
    set1 = set(data)
    set2 = set(data2)
    true_jaccard = len(set1.intersection(set2)) / len(set1.union(set2))
    print(f"True Jaccard index between data sets: {true_jaccard:.4f}")
    
    # compute jaccard index using MGS
    jaccard = max_geom_sample.jaccard_index(another_sample)
    print(f"Jaccard index between MGS samples: {jaccard:.4f}")
    
    # compute jaccard index using FMH
    fmh_sketch2 = FracMinHashSketch(scale)
    fmh_sketch2.add_many_items(data2)
    fmh_jaccard = fmh_sketch.jaccard_index(fmh_sketch2)
    print(f"Jaccard index between FMH sketches: {fmh_jaccard:.4f}")
    
    # generate two large sets, take MGS samples, do union, and check if equal to MGS of union
    data3 = generate_random_strings(100000, 10)
    data4 = generate_random_strings(100000, 10)
    sample3 = MaxGeomSample(k=100, w=64, seed=42)
    sample3.add_many_items(data3)
    sample4 = MaxGeomSample(k=100, w=64, seed=42)
    sample4.add_many_items(data4)
    union_sample = sample3.union(sample4)
    combined_data = data3 + data4
    combined_sample = MaxGeomSample(k=100, w=64, seed=42)
    combined_sample.add_many_items(combined_data)
    print(f"Union of samples equals sample of union: {union_sample == combined_sample}")

    # do the same test for 10 different random seeds
    all_equal = True
    for seed in range(10):
        sample3 = MaxGeomSample(k=100, w=64, seed=seed)
        sample3.add_many_items(data3)
        sample4 = MaxGeomSample(k=100, w=64, seed=seed)
        sample4.add_many_items(data4)
        union_sample = sample3.union(sample4)
        combined_sample = MaxGeomSample(k=100, w=64, seed=seed)
        combined_sample.add_many_items(combined_data)
        if union_sample != combined_sample:
            all_equal = False
            break
    print(f"Union of samples equals sample of union for 10 seeds: {all_equal}")