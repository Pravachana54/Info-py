# In[3]:


# dataset - https://www.kaggle.com/datasets/bhadaneeraj/cardio-vascular-disease-detection

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cardio_train.csv', sep=';')

df['age'] = df['age'] // 365
cholesterol_mapping = {1: 'normal', 2: 'above normal', 3: 'well above normal'}
df['cholesterol'] = df['cholesterol'].map(cholesterol_mapping)
glucose_mapping = {1: 'normal', 2: 'above normal', 3: 'well above normal'}
df['gluc'] = df['gluc'].map(glucose_mapping)
gender_mapping = {1: 'male', 2: 'female'}
df['gender'] = df['gender'].map(gender_mapping)
cardio_mapping = {0: 'no', 1: 'yes'}
df['cardio'] = df['cardio'].map(cardio_mapping)

sns.set(style="dark")
fig, axes = plt.subplots(2, 2, figsize=(20, 20))
fig.set_facecolor('#FFEBEE')


sns.kdeplot(data=df[df['cardio']=='no']['age'], label='No Cardio', fill=True, common_norm=False, color='red', ax=axes[0, 0])
sns.kdeplot(data=df[df['cardio']=='yes']['age'], label='Cardio', fill=True, common_norm=False, color='green', ax=axes[0, 0])
axes[0, 0].set_title('PDF Plot of Age with Cardio as Hue', fontsize=18)
axes[0, 0].set_xlabel('Age')
axes[0, 0].set_ylabel('Density')
axes[0, 0].legend(title='Cardiovascular Disease', labels={'No', 'Yes'})

sns.countplot(x='gender', hue='cardio', data=df, palette='husl', ax=axes[0, 1])
axes[0, 1].set_title('Cardiovascular Disease by Gender', fontsize=18)
axes[0, 1].set_xlabel('Gender')
axes[0, 1].set_ylabel('Count')
axes[0, 1].legend(title='Cardiovascular Disease', labels={'No', 'Yes'})

sns.scatterplot(x='height', y='weight', hue='cardio', data=df, palette='husl', s=80, ax=axes[1, 0])
axes[1, 0].set_title('Scatter Plot with Cardiovascular Disease Status', fontsize=18)
axes[1, 0].set_xlabel('Height')
axes[1, 0].set_ylabel('Weight')

sns.countplot(x="cholesterol", hue="cardio", data=df, palette='husl', ax=axes[1, 1])
axes[1, 1].set_title('Cardiovascular Disease Count for Different Cholesterol Levels', fontsize=18)
axes[1, 1].set_xlabel('Cholesterol Level')
axes[1, 1].set_ylabel('Count')

fig.suptitle('Various Cardiovascular Disease Plots', fontsize=30)
plt.figtext(0.1, 0.93, 'Name: Pravachana Maadala', ha='left', fontsize=18)
plt.figtext(0.1, 0.91, 'SID: 22093562', ha='left', fontsize=18)

text = """Plot 1: The pdf plot shows the probability of having cardiovascular disease rise in disease prevalence starting around the age of 50.

Plot 2: Bar plot indicates that males have a slightly higher count of cardiovascular cases than females.

Plot 3: The scatter plot shows that height and weight are not decisive factors alone in determining cardiovascular health.
There is no clear boundary separating those with and without the disease, indicating that other factors besides height and weight play a significant role.

Plot 4: The individuals with above normal cholestrol levels and well above normal cholestrol levels are at higher risk"""

fig.text(0.05, -0.05, text, fontsize=18, va='baseline', fontweight='bold')

plt.savefig('22093562.png', format='png', dpi=300, bbox_inches='tight')
plt.show()

# 
