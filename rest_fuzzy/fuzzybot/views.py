from django.views.generic import View
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
import logging
import unicodedata as ud

from services import getBot

chatterbot = getBot()
logger = logging.getLogger(__name__)
class ChatterBotView(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse("hello", safe=False)

    def post(self, request, *args, **kwargs):
        input_statement = request.POST.get('text')
        response_data = chatterbot.get_response(ud.normalize('NFKD', input_statement).encode('ascii','ignore'))
        return JsonResponse(JSONRenderer().render(response_data.text),safe=False)