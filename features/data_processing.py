import pandas as pd
import missingno as msn
import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.abspath('../visualization'))
import data_visualization
path = '../data/filtered/compressive_strength.csv'


class CompressiveStrength:
    def __init__(self):
        # Initiate df and objects
        self.df_filtered = pd.read_csv(path, index_col=False)
        self.df_filtered.reset_index(drop=True, inplace=True)
        self.plotting = data_visualization.GraphPlotting()

    def data_analysis(self):
        # View the Structural properties of data
        print(self.df_filtered.info())
        print('_' * 150)
        print(self.df_filtered.describe())
        print('_' * 150)

        # Visual distribution of missing values
        msn.matrix(self.df_filtered, color=(0.66, 0.45, 0.013), figsize=[13, 15], fontsize=7)
        plt.title("Missingno Matrix for Compressive Strength data:")
        plt.show()

        # Scan for Null values and Sanitize the data
        print("•Null-value Diagnostics: ")
        print(self.df_filtered.isnull().sum())
        print('_' * 150)
        self.df_filtered.dropna(axis='columns')

        # Histogram for label inspection
        bins = 20
        title = "Distribution of the Compressive Strength"
        x_label = "Strength (MPa)"
        y_label = 'Frequency'

        self.plotting.distribution_histogram(self.df_filtered['compressive_strength'], bins, title, x_label, y_label)

        # Histogram for the inspection of features
        bins = 15
        d1 = self.df_filtered['cement']
        d2 = self.df_filtered['blast_furnace_slag']
        d3 = self.df_filtered['water']
        d4 = self.df_filtered['super_plasticisers']
        d5 = self.df_filtered['coarse_aggregate']
        d6 = self.df_filtered['fine_aggregate']
        d7 = self.df_filtered['age']
        self.plotting.distribution_histogram_multi(d1, d2, d3, d4, d5, d6, d7, bins)

        # Pearson Correlation
        title = "Pearson Correlation Heatmap for the modified Dataframe."
        self.plotting.pearson_correlation(self.df_filtered, title)

    @staticmethod
    def display_dataframe(name, df, contents):
        table = df.head(contents)
        print('\n', '_' * 150)
        print("◘ Displaying dataframe for ", name)
        print(table.to_string())
        print('_' * 150)

    def data_storage(self):
        # Save modified data to storage
        try:
            self.df_filtered.drop(columns='index')

        except Exception as exc:
            print(exc)

        finally:
            name = "Modified dataframe"
            self.display_dataframe(name, self.df_filtered, 20)

            self.df_filtered.to_csv('../data/processed/compressive_strength.csv', sep=',', index=False)
            self.df_filtered.to_json('../data/processed/compressive_strength.json')


if __name__ == "__main__":
    main = CompressiveStrength()
    main.data_analysis()
    main.data_storage()

