import flask

from app.modules.common import interfaces, utils
from app.modules.category_classificator.data import use_cases, repositories
from app.modules.category_classificator import controllers


class PredictCategoryClassificatorView(interfaces.APIView):

    def post(self):
        controller = controllers.PredictController(
            predict_use_case=use_cases.PredictUseCase(
                repository=repositories.PredictRepository()
            ),
        )

        data = None

        if flask.request.headers.get('Content-Type').startswith('application/json'):
            data = flask.request.get_json()

        if flask.request.headers.get('Content-Type').startswith('multipart/form-data'):
            data = flask.request.form

        if data is None:
            return utils.Response(response={"message": "Missing data"}, status=utils.Status.NOT_FOUND_404)

        if not data.get("text", False):
            return utils.Response(response={"message": "Missing text"}, status=utils.Status.NOT_FOUND_404)

        return utils.Response(response={"data": controller.predict(data["text"])})


class TrainModelCategoryClassificatorView(interfaces.APIView):

    def get(self):
        controller = controllers.TrainModelController(
            clean_data_use_case=use_cases.CleanDataUseCase(
                repository=repositories.CleanDataRepository()
            ),
            train_model_use_case=use_cases.TrainModelUseCase(
                repository=repositories.TrainModelRepository()
            )
        )

        return utils.Response(response={"message": controller.train()})



