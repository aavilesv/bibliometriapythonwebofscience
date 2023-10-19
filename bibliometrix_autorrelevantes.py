import matplotlib.pyplot as plt

# Datos
authors = ["AL-RAHMI WM", "LOWENTHAL PR", "AGGARWAL A", "ALIJA S", "ALLEN KA", 
           "CHAMORRO-ATALAYA O", "MALONEY S", "MORALES-ROMERO G", "SANTALLY MI", "ABDALLA ME"]
articles = [7, 4, 3, 3, 3, 3, 3, 3, 3, 2]
articles_fractionalized = [1.65, 1.67, 1.08, 0.92, 0.47, 0.45, 0.66, 0.43, 1.08, 0.33]

# Creación del gráfico
fig, ax1 = plt.subplots(figsize=(15, 10))

# Eje y doble
ax2 = ax1.twinx()
index = [i for i in range(len(authors))]
bar_width = 0.35

# Barras
bars1 = ax1.bar(index, articles, bar_width, label='Articles', color='b')
bars2 = ax2.bar([i + bar_width for i in index], articles_fractionalized, bar_width, label='Fractionalized articles', color='r')

# Etiquetas, títulos, etc.
ax1.set_xlabel('Authors')
ax1.set_ylabel('Number of Articles', color='b')
ax2.set_ylabel('Fractionalized Articles', color='r')
ax1.set_title('Most relevant authors and their production')
ax1.set_xticks([i + bar_width / 2 for i in index])
ax1.set_xticklabels(authors, rotation=45, ha='right')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Mostrar valores en las barras
for bar in bars1:
    yval = bar.get_height()
    print(yval)
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 2), ha='center', va='center', color='b')

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.02, round(yval, 2), ha='center', va='center', color='r')

# Mostrar gráfico
plt.tight_layout()
plt.show()