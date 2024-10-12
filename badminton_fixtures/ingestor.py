from dataclasses import dataclass

import pandas as pd


@dataclass
class Ingestor:
    path: str = "./data/fixtures.xlsx"
    sheet: str = "Table 1"

    def ingest(self):
        df_fixtures = pd.read_excel(self.path, self.sheet)
        df_fixtures = df_fixtures[df_fixtures["Status"] == "Arranged"]
        print(df_fixtures)
