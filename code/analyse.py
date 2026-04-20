import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/marketing_data.csv')

df['ROI'] = (df['Revenue'] - df['Spend']) / df['Spend']

mean = df['ROI'].mean()
std = df['ROI'].std()
df['Z_score'] = (df['ROI'] - mean) / std

print(df)

plt.figure(figsize=(14,10))

plt.subplot(2,2,1)
plt.bar(df['Campaign'], df['ROI'])
plt.xticks(rotation=45)

plt.subplot(2,2,2)
plt.scatter(df['Spend'], df['Revenue'])

plt.subplot(2,2,3)
sns.heatmap(df[['Spend','Clicks','Conversions','Revenue','ROI']].corr(), annot=True)

plt.tight_layout()
plt.figtext(0.5, 0.01, 
"Recommendation: Shift budget to high ROI campaigns like Google Ads.",
ha='center', fontsize=10)
plt.savefig('../output/dashboard.png')
plt.show()