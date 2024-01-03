import io
import base64

import flask

from app.modules.common import interfaces, utils
from app.modules.user_recognition.data import use_cases, repositories, models
from app.modules.user_recognition import controllers


class UserRecognitionView(interfaces.APIView):

    def post(self):
        image_manager = models.ImageManager()
        controller = controllers.RecognitionController(
            image_manager=image_manager,
            recognition_use_case=use_cases.RecognitionUseCase(
                repository=repositories.RecognitionRepository(
                    image_manager=image_manager
                )
            )
        )

        if "picture" not in flask.request.files:
            return utils.Response({"message": 'Picture not found'}, status=404)

        picture = flask.request.files["picture"]
        io_picture = io.BytesIO(picture.stream.read())

        recognition = controller.detect_face(io_picture)

        io_picture.seek(0)
        recognition["image"] = base64.b64encode(io_picture.getvalue()).decode()

        return utils.Response(recognition)

        # return flask.send_file(
        #     recognition["image"],
        #     mimetype='image/jpeg',
        #     as_attachment=True,
        #     download_name='image.jpg'
        # )

