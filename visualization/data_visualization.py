import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib.font_manager import FontProperties


class GraphPlotting:
    def __init__(self):
        pass

    @staticmethod
    def graph_settings():
        # Customizable Set-ups
        plt.figure(figsize=(13, 15))
        font = FontProperties()
        font.set_family('serif bold')
        font.set_style('oblique')
        font.set_weight('bold')
        ax = plt.axes()
        ax.set_facecolor("#e6eef1")

    def distribution_histogram(self, data_values, bins, title, x_label, y_label):
        self.graph_settings()

        plt.hist(data_values, bins=bins, color='maroon')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()

    @staticmethod
    def distribution_histogram_multi(d1, d2, d3, d4, d5, d6, d7, bins):
        fig, axes = plt.subplots(1, 7)
        plt.rcParams["figure.figsize"] = [14, 16]
        plt.rcParams["figure.autolayout"] = True

        d1.hist(bins=bins, color='maroon', ax=axes[0])
        d2.hist(bins=bins, color='maroon', ax=axes[1])
        d3.hist(bins=bins, color='maroon', ax=axes[2])

        d4.hist(bins=bins, color='maroon', ax=axes[3])
        d5.hist(bins=bins, color='maroon', ax=axes[4])
        d6.hist(bins=bins, color='maroon', ax=axes[5])
        d7.hist(bins=bins, color='maroon', ax=axes[6])

        axes[0].set_title('Cement')
        axes[1].set_title('Blast Furnace Slag')
        axes[2].set_title('Water')
        axes[3].set_title('Super Plasticisers')
        axes[4].set_title('Coarse Aggregate')
        axes[5].set_title('Fine Aggregate')
        axes[6].set_title('Age')
        plt.show()

    def distribution_pie(self, data_values, explode, labels, title):
        self.graph_settings()

        plt.pie(data_values, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
        plt.title(title)
        plt.show()

    @staticmethod
    def pearson_correlation(df, title):
        print("•Pearson Correlation Matrix:\n", df.corr())
        data_plot = sb.heatmap(df.corr(), cmap="YlGnBu", annot=True)
        plt.title(title)
        plt.yticks(rotation='horizontal')
        plt.show()

    @staticmethod
    def covariance_matrix(df, title):
        print("•Covariance Matrix:\n", df.corr())
        corr = df.select_dtypes('number').corr()
        sb.heatmap(corr, cmap="Blues", annot=True)
        plt.title(title)
        plt.show()

    def bar_graph(self, x, y, title, x_label, y_label):
        # Vertical Bar charts using matplotlib
        self.graph_settings()
        plt.bar(x, y)

        plt.title(title, fontsize=16)
        plt.xlabel(x_label)
        plt.xticks()
        plt.ylabel(y_label)
        plt.show()

    def scatter_graph(self, x, y, title, x_label, y_label):
        # Vertical Bar charts using matplotlib
        self.graph_settings()
        plt.scatter(x, y)

        plt.title(title, fontsize=16)
        plt.xlabel(x_label)
        plt.xticks()
        plt.ylabel(y_label)
        plt.show()


if __name__ == "__main__":
    main = GraphPlotting()