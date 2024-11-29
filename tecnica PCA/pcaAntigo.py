import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('dados.csv')

scaler = StandardScaler()

colunas = list(df.columns)

# Aplicar padronização
df = scaler.fit_transform(df)

# Exibir os dados padronizados
print("\nDados padronizados:")
print(df)

# Creating a matrix of the standardized data
X_std = np.column_stack(df)

# Calculating the covariance matrix
cov_matrix = np.cov(X_std.T)

# Eigendecomposition
eigen_vals, eigen_vecs = np.linalg.eig(cov_matrix)

# Plotando a Matriz de Covariância
plt.figure(figsize=(20, 15))  # Aumenta o tamanho da figura
sns.heatmap(
    cov_matrix,
    annot=True,                 # Exibe os valores
    fmt=".2f",                  # Formato com 2 casas decimais
    cmap='coolwarm',            # Mapa de cores
    xticklabels=colunas,        # Etiquetas dos eixos
    yticklabels=colunas,
    cbar_kws={'shrink': 0.8}    # Ajusta o tamanho da barra de cores
)
plt.xticks(rotation=45, fontsize=10)  # Rotaciona as etiquetas do eixo X
plt.yticks(fontsize=10)               # Ajusta o tamanho das etiquetas do eixo Y
plt.title('Covariance Matrix Heatmap', fontsize=16)  # Título maior
plt.tight_layout()  # Ajusta automaticamente os elementos para não cortarem
plt.show()

# 3D Data Plot with Eigenvectors
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter()

# Adding eigenvectors to the 3D plot
for i in range(len(eigen_vals)):
    vec = eigen_vecs[:,i] * eigen_vals[i]
    ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color='r')

ax.set_xlabel('Standardized Age')
ax.set_ylabel('Standardized Height')
ax.set_zlabel('Standardized Weight')
plt.title('3D Data Plot with Eigenvectors')
plt.show()