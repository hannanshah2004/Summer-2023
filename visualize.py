import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('input.txt')

summary = df.groupby('Vector').mean()
print("Summary statistics:")
print(summary)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

df.groupby('Vector')['Kanamycin_Resistance'].mean().plot(kind='bar', ax=axes[0], color='black')
axes[0].set_title('Kanamycin Resistance by Vector')
axes[0].set_ylabel('Mean Resistance')

df.groupby('Vector')['GUS_Staining'].mean().plot(kind='bar', ax=axes[1], color='red')
axes[1].set_title('GUS Staining by Vector')
axes[1].set_ylabel('Mean GUS Staining')

plt.tight_layout()
plt.show()
