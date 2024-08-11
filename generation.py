import numpy as np

np.random.seed(42)

sample_size = 100
vectors = ['pSSK6A', 'pCAMBIA2301', 'Non-Transformed']

prob_kanamycin = {
    'pSSK6A': 0.85,
    'pCAMBIA2301': 0.90,
    'Non-Transformed': 0.05
}

prob_gus = {
    'pSSK6A': 0.75,
    'pCAMBIA2301': 0.80,
    'Non-Transformed': 0.02
}

with open('input.txt', 'w') as f:
    f.write('Sample,Vector,Kanamycin_Resistance,GUS_Staining\n')
    for vector in vectors:
        for i in range(sample_size):
            kan_res = np.random.binomial(1, prob_kanamycin[vector])
            gus_stain = np.random.binomial(1, prob_gus[vector])
            f.write(f'{i+1},{vector},{kan_res},{gus_stain}\n')

print("input.txt generated successfully.")
