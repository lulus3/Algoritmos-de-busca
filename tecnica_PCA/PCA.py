import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D

# Carregar o dataset
df = pd.read_csv('dados.csv')  # Altere para o nome correto do seu arquivo CSV

# Padronizar os dados
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Aplicar o PCA
pca = PCA()
pca.fit(df_scaled)

# Variância explicada por cada componente
eigenvalues = pca.explained_variance_ratio_
print("Variância explicada por cada componente principal:")
print(eigenvalues)

# Exibir a variância explicada por cada componente em porcentagem
for i, var_ratio in enumerate(eigenvalues):
    print(f"PC{i+1}: {var_ratio*100:.2f}%")

# Autovetores (pesos das variáveis nos componentes principais)
eigenvectors = pca.components_
components_df = pd.DataFrame(eigenvectors, columns=[f"PC{i+1}" for i in range(len(eigenvectors))], index=df.columns)
print("\nPesos das variáveis nas componentes principais:")
print(components_df)

# 1. Gráfico da variância explicada por componente principal
plt.figure(figsize=(8, 6))
plt.bar(range(1, len(eigenvalues) + 1), eigenvalues, alpha=0.7, color='blue')
plt.xlabel('Componente Principal')
plt.ylabel('Variância Explicada (%)')
plt.title('Variância Explicada por Componente Principal')
plt.show()

# 2. Gráfico da variância acumulada
plt.figure(figsize=(8, 6))
plt.plot(range(1, len(eigenvalues) + 1), np.cumsum(eigenvalues), marker='o', color='green')
plt.xlabel('Número de Componentes Principais')
plt.ylabel('Variância Acumulada (%)')
plt.title('Variância Acumulada por Componentes Principais')
plt.show()

# 3. Heatmap dos pesos das variáveis nas componentes principais
plt.figure(figsize=(12, 8))
sns.heatmap(components_df, annot=True, cmap='coolwarm', fmt='.2f', cbar_kws={'label': 'Peso da Variável'})
plt.title('Pesos das Variáveis nas Componentes Principais')
plt.show()

# 4. Análise visual dos dados nas primeiras duas componentes principais
# Projeção dos dados nas primeiras 2 componentes principais
df_pca = pca.transform(df_scaled)

# Gráfico de dispersão (2D) para as primeiras duas componentes principais
plt.figure(figsize=(8, 6))
plt.scatter(df_pca[:, 0], df_pca[:, 1], alpha=0.7, color='purple')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Projeção dos Dados nas Primeiras 2 Componentes Principais')
plt.show()

# 5. Análise visual dos dados nas primeiras três componentes principais (Gráfico 3D)


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df_pca[:, 0], df_pca[:, 1], df_pca[:, 2], alpha=0.7, color='orange')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')
plt.title('Projeção dos Dados nas 3 Primeiras Componentes Principais')
plt.show()

# 6. Exibir as variáveis mais importantes para PC1, PC2, etc.
print("\nVariáveis mais importantes para PC1:")
print(components_df["PC1"].abs().sort_values(ascending=False))

print("\nVariáveis mais importantes para PC2:")
print(components_df["PC2"].abs().sort_values(ascending=False))

print("\nVariáveis mais importantes para PC3:")
print(components_df["PC3"].abs().sort_values(ascending=False))
