# ==============================================
# Analisis Data & Visualisasi Data Nilai Siswa
# ==============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv')

print("=== Informasi Dataset ===")
data.info()

print("\n=== 5 Data Pertama ===")
print(data.head())

print("\n=== Statistik Deskriptif ===")
print(data.describe())

print("\n=== Data Lengkap ===")
print(data)

print("\n=== Ukuran Statistik Dasar ===")
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

print("\n=== Nilai Maksimum dan Minimum per Mapel ===")
print(data.groupby('Mapel')['Nilai'].agg(['max','min']))

rata = data.groupby('Mapel')['Nilai'].mean()
rata.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.boxplot(x='Mapel', y='Nilai', data=data, palette='pastel')
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

