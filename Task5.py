import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = [10, 6]

df = pd.read_csv("/Users/iuv/Documents/Elevate_labs/train.csv")
print(df.head())

# Dataset overview
print(df.info())
print(df.describe(include='all'))
print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace=True)

df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

df.drop(columns=['Cabin'], inplace=True)

df['Sex_encoded'] = df['Sex'].map({'male': 0, 'female': 1})

df['Embarked_encoded'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# 1. Survival Count Plot
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Survived', palette='Set2')
plt.title("Survival Count")
plt.xticks([0, 1], ['Did Not Survive', 'Survived'])
plt.xlabel("Survival")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output_1_survival_count.png")
plt.show()

# 2. Survival by Sex
sns.countplot(data=df, x='Sex', hue='Survived', palette='pastel')
plt.title("Survival by Sex")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.tight_layout()
plt.savefig("output_2_survival_by_sex.png")
plt.show()

# 3. Survival by Pclass
sns.countplot(data=df, x='Pclass', hue='Survived', palette='husl')
plt.title("Survival by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.tight_layout()
plt.savefig("output_3_survival_by_class.png")
plt.show()

# 4. Age Distribution
sns.histplot(df['Age'], bins=30, kde=True, color='skyblue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("output_4_age_distribution.png")
plt.show()

# 5. Boxplot of Age by Survival
sns.boxplot(data=df, x='Survived', y='Age', palette='coolwarm')
plt.title("Age vs Survival")
plt.xticks([0, 1], ['No', 'Yes'])
plt.tight_layout()
plt.savefig("output_5_age_vs_survival_boxplot.png")
plt.show()

# 6. Pairplot
sns.pairplot(df[['Survived', 'Pclass', 'Age', 'Fare', 'Sex_encoded']], hue='Survived', palette='Set1')
plt.suptitle("Pairplot of Features", y=1.02)
plt.savefig("output_6_pairplot.png")
plt.show()

# 7. Correlation Heatmap
plt.figure(figsize=(10, 6))
corr = df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_encoded', 'Embarked_encoded']].corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, annot=True, cmap='coolwarm', mask=mask, linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("output_7_correlation_heatmap.png")
plt.show()

