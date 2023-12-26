from app.modules.category_clasificator.data import use_cases


class ClassifierController(object):

    def __init__(
        self,
        clean_data_use_case: use_cases.CleanDataUseCase = None,
        train_model_use_case: use_cases.TrainModelUseCase = None,
    ):
        # TODO: Make predict functionalities
        self.data = {}
        self.clean_data_use_case = clean_data_use_case
        self.train_model_use_case = train_model_use_case

    def train_model(self):
        self.train_model_use_case.call(
            params=use_cases.TrainModelUseCaseParams(self.get_data())
        )

    def get_data(self):
        (texts, labels) = self.clean_data_use_case.call()

        data = {"texts": texts, "labels": labels}
        self.data = data

        return data
