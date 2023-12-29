import typing as t

import polars as pl

from app.modules.category_classificator.data import repositories


class CleanDataRepository(repositories.BaseRepository):

    def __init__(self) -> None:
        self.df = pl.read_excel("/Users/lsvtech2022/Documents/projects/python/text_clasificator/app/modules/category_classificator/data/train_data/test_data.xlsx")
        self.texts = None
        self.labels = None

    def clean(self) -> t.Tuple[str]:
        data = self._sort_data()

        self.texts = [item['text'] for item in data]
        self.labels = [item['label'] for item in data]

        return (self.texts, self.labels)

    def _sort_data(self) -> t.List[t.Dict[str, str]]:
        data = []

        for row in self.df.iter_rows(named=True):
            data.append({"text": row["wait for"], "label": "wait for"})
            data.append({"text": row["rent book"], "label": "rent book"})
            data.append({"text": row["use computer"], "label": "use computer"})
            data.append({"text": row["other"], "label": "other"})

        return data