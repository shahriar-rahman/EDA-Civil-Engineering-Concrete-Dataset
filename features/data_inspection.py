import pandas as pd
import sys
import os
sys.path.append(os.path.abspath('../visualization'))
import data_visualization
data_path = '../data/processed/compressive_strength.csv'


class CompressiveStrength:
    def __init__(self):
        # Initiate df and objects
        self.df_processed = pd.read_csv(data_path, index_col=False)
        self.df_processed.reset_index(drop=True, inplace=True)
        self.plotting = data_visualization.GraphPlotting()

    def data_inspections(self):
        # Compressive Strength
        print('•Displaying Statistical data for the Label:\n', self.df_processed['compressive_strength'].describe())
        print('_' * 150)

        # Quantity of cement where strength is greater than mean value
        high_strength = self.df_processed[self.df_processed['compressive_strength'] >
                                          self.df_processed['compressive_strength'].mean()]
        df = high_strength[['cement', 'compressive_strength']].sort_values(by='compressive_strength', ascending=False)

        # Bar Plot and Covariance Matrix
        title = "Cement vs High Compressive Strength"
        x_label = "Compressive Strength (MPa)"
        y_label = "Cement (kg in a m^3 mixture)"
        self.display_dataframe('df', df, 25)
        self.plotting.bar_graph(df['compressive_strength'].iloc[:150], df['cement'].iloc[:150], title, x_label, y_label)
        self.plotting.covariance_matrix(df, "Covariance Matrix -Cement vs High Compressive Strength")

        # Blast furnace effect on Compressive strength (Combined)
        df = self.df_processed[['blast_furnace_slag', 'compressive_strength']].sort_values(by='compressive_strength',
                                                                                           ascending=False)

        # Scatter Plot and Covariance Matrix
        title = "Blast Furnace Slag vs High Compressive Strength"
        x_label = "Compressive Strength (MPa)"
        y_label = "Blast Furnace Slag (kg in a m^3 mixture)"
        self.display_dataframe('df', df, 25)
        self.plotting.scatter_graph(df['compressive_strength'].iloc[:150], df['blast_furnace_slag'].iloc[:150],
                                    title, x_label, y_label)

        df = high_strength[['blast_furnace_slag', 'compressive_strength']].sort_values(by='compressive_strength',
                                                                                       ascending=False)
        self.plotting.covariance_matrix(df, "Covariance Matrix -Blast furnace vs Compressive strength")

        # How much water is required to acquire adequate Strength
        df = high_strength[['water', 'compressive_strength']].sort_values(by='compressive_strength',
                                                                          ascending=False)
        # Bar Plot and Covariance Matrix
        title = "Water vs High Compressive Strength"
        x_label = "Compressive Strength (MPa)"
        y_label = "Water (kg in a m^3 mixture)"
        self.display_dataframe('df', df, 25)
        self.plotting.bar_graph(df['compressive_strength'].iloc[:150], df['water'].iloc[:150], title, x_label, y_label)
        self.plotting.covariance_matrix(df, "Covariance Matrix -Water vs High Compressive Strength")

        # How Super Plasticisers affect Compressive strength (combined)
        df = self.df_processed[['super_plasticisers', 'compressive_strength']].sort_values(by='compressive_strength',
                                                                                           ascending=False)

        # Scatter Plot and Covariance Matrix
        title = "Super Plasticisers vs High Compressive Strength"
        x_label = "Compressive Strength (MPa)"
        y_label = "Super Plasticisers (kg in a m^3 mixture)"
        self.display_dataframe('df', df, 25)
        self.plotting.scatter_graph(df['compressive_strength'].iloc[:150], df['super_plasticisers'].iloc[:150],
                                    title, x_label, y_label)
        self.plotting.covariance_matrix(df, "Covariance Matrix -Super Plasticisers vs Compressive strength")

        # Cases involving Coarse and Fine Aggregate vs Compressive strength (combined)
        self.df_processed['combined_aggregate'] = self.df_processed['coarse_aggregate'] + \
                                                  self.df_processed['fine_aggregate']
        print("Displaying columns after modification:\n", self.df_processed.columns)
        print('_' * 150)

        df = self.df_processed[['coarse_aggregate', 'compressive_strength']].sort_values(by='compressive_strength',
                                                                                         ascending=False)
        self.plotting.covariance_matrix(df, "Covariance Matrix -Coarse Aggregate vs Compressive strength")

        df = self.df_processed[['fine_aggregate', 'compressive_strength']].sort_values(by='compressive_strength',
                                                                                       ascending=False)
        self.plotting.covariance_matrix(df, "Covariance Matrix -Fine Aggregate vs Compressive strength")

        df = self.df_processed[['combined_aggregate', 'compressive_strength']].sort_values(by='compressive_strength',
                                                                                           ascending=False)
        self.plotting.covariance_matrix(df, "Covariance Matrix -Combined Aggregate vs Compressive strength")

        # Whether age affected the strength in the historical data
        df = self.df_processed[['age', 'compressive_strength']].sort_values(by='compressive_strength',
                                                                            ascending=False)

        # Scatter Plot and Covariance Matrix
        title = "Age vs High Compressive Strength"
        x_label = "Compressive Strength (MPa)"
        y_label = "Age (Years)"
        self.display_dataframe('df', df, 25)
        self.plotting.bar_graph(df['compressive_strength'].iloc[:150], df['age'].iloc[:150],
                                title, x_label, y_label)
        self.plotting.covariance_matrix(df, "Covariance Matrix -Age vs Compressive strength")

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
            self.df_processed.drop(columns='index')

        except Exception as exc:
            print(exc)

        finally:
            name = "Modified dataframe"
            self.display_dataframe(name, self.df_processed, 20)

            self.df_processed.to_csv('../data/model_ready/compressive_strength.csv', sep=',', index=False)
            self.df_processed.to_json('../data/model_ready/compressive_strength.json')


if __name__ == "__main__":
    main = CompressiveStrength()
    main.data_inspections()
    main.data_storage()
