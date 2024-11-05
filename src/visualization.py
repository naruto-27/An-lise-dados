import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=column)
    plt.title(f'Distribuição de {column}')
