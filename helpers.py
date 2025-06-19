import Levenshtein
from itertools import combinations
import pandas as pd
import random
import numpy as np


def all_intragroup_distances(df, group_col, value_col="achternaam"):
    distances = []
    for _, group in df.groupby(group_col):
        names = [str(x) for x in group[value_col].dropna()]
        if len(names) > 1:
            dists = [Levenshtein.distance(a, b) for a, b in combinations(names, 2)]
            distances.extend(dists)
    return np.array(distances)

def mean_intergroup_levenshtein(df, group_col, value_col="achternaam", sample_size=5000, seed=42):
    rng = random.Random(seed)
    tuples = list(zip(df[value_col], df[group_col]))
    n = len(tuples)
    inter_distances = []
    while len(inter_distances) < sample_size:
        i, j = rng.sample(range(n), 2)
        name1, group1 = tuples[i]
        name2, group2 = tuples[j]
        if group1 != group2 and pd.notnull(name1) and pd.notnull(name2):
            inter_distances.append(Levenshtein.distance(str(name1), str(name2)))
    return np.mean(inter_distances)

def bootstrap_diff(data1, data2, n_bootstrap=10000, seed=42):
    np.random.seed(seed)
    boots = []
    for _ in range(n_bootstrap):
        sample1 = np.random.choice(data1, size=len(data1), replace=True)
        sample2 = np.random.choice(data2, size=len(data2), replace=True)
        boots.append(np.mean(sample1) - np.mean(sample2))
    boots = np.array(boots)
    lower, upper = np.percentile(boots, [2.5, 97.5])
    p_value = np.mean(boots >= 0)
    return lower, upper, p_value
