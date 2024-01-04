import io
import base64

import flask

from app.modules.common import interfaces, utils, decorators
from app.modules.user_recognition.data import use_cases, repositories, models
from app.modules.user_recognition import controllers



class UserRecognitionView(interfaces.APIView):

    @decorators.x_api_key_required
    def post(self):
        try:
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
                return utils.Response({"message": 'Picture not found'}, status=utils.Status.NOT_FOUND_404)

            picture = flask.request.files["picture"]
            io_picture = io.BytesIO(picture.stream.read())

            recognition = controller.detect_face(io_picture)

            recognition["image"].seek(0)
            recognition["image"] = base64.b64encode(recognition["image"].getvalue()).decode("ascii")

            return utils.Response(recognition)

            # return flask.send_file(
            #     recognition["image"],
            #     mimetype='image/jpeg',
            #     as_attachment=True,
            #     download_name='image.jpg'
            # )
        except:
            return utils.Response({"message": 'No persons were recognised.'}, status=utils.Status.BAD_REQUEST_400)
