import polars as pl

from app.modules.category_clasificator.data import repositories


class CleanDataRepository(repositories.BaseRepository):

    def __init__(self):
        self.df = pl.read_excel("app/modules/category_clasificator/data/train_data/test_data.xlsx")
        self.texts = None
        self.labels = None

    def clean(self) -> tuple:
        data = self._sort_data()

        self.texts = [item['text'] for item in data]
        self.labels = [item['label'] for item in data]

        return (self.texts, self.labels)

    def _sort_data(self):
        data = []

        for row in self.df.iter_rows(named=True):
            data.append({"text": row["wait for"], "label": "wait for"})
            data.append({"text": row["rent book"], "label": "rent book"})
            data.append({"text": row["use computer"], "label": "use computer"})
            data.append({"text": row["other"], "label": "other"})

        return data