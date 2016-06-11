from chatterbot.training.trainers import ListTrainer
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from rest_framework.views import APIView
import logging


chatterbot = ChatBot(
    'Example ChatterBot',
    io_adapter="chatterbot.adapters.io.JsonAdapter"
)

chatterbot.set_trainer(ListTrainer)
chatterbot.train([
    "Hi",
    "Hello",
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
])

logger = logging.getLogger(__name__)
class ChatterBotView(View):

    def get(self, request, *args, **kwargs):
        data = {
            'detail': 'You should make a POST request to this endpoint.'
        }

        # Return a method not allowed response
        return JsonResponse(data, status=405)

    def post(self, request, *args, **kwargs):

        logger.info("entered the method post")
        input_statement = request.POST.get('text')

        response_data = chatterbot.get_response(input_statement)

        return JsonResponse(response_data)