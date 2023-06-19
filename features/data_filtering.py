import pandas as pd
path = '../data/raw/compressive_strength.xlsx'


class CompressiveStrength:
    def __init__(self):
        self.df_raw = pd.read_excel(path, index_col=False)

    @staticmethod
    def display_dataframe(name, df, contents):
        table = df.head(contents)
        print('\n', '_' * 150)
        print("◘ Displaying dataframe for ", name)
        print(table.to_string())
        print('_' * 150)

    def data_processing(self):
        print("• Raw Dataset: \n", self.df_raw.columns)
        print('-' * 150)

        self.df_raw.rename(columns={'Cement': 'cement', 'BlastFurnaceSlag': 'blast_furnace_slag', 'Water': 'water',
                                    'Superplasticizer': 'super_plasticisers', 'CoarseAggregate': 'coarse_aggregate',
                                    'FineAggregate': 'fine_aggregate', 'Age': 'age'}, inplace=True)

        print("• Modified Dataset: \n", self.df_raw.columns)
        print('-' * 150)

    def data_storage(self):
        name = "Modified dataframe"
        self.display_dataframe(name, self.df_raw, 20)

        # Save modified data to storage
        self.df_raw.to_csv('../data/filtered/compressive_strength.csv', sep=',', index=False)
        self.df_raw.to_json('../data/filtered/compressive_strength.json')


if __name__ == "__main__":
    main = CompressiveStrength()
    main.data_processing()
    main.data_storage()

