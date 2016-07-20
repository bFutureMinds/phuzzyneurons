from django.views.generic import View
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
import logging
import unicodedata as ud
import rest_fuzzy.wordsfilter as wf
import services as s
import os
import rest_fuzzy.responsefilter as rf
from rest_fuzzy.settings import BASE_DIR
import json

from services import getBot


chatterbot = getBot()

logger = logging.getLogger(__name__)
class ChatterBotView(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse("hello", safe=False)

    def post(self, request, *args, **kwargs):
        input_statement = request.POST.get('text')
        input_statement = wf.filterString(input_statement)
        response_data = chatterbot.get_response(ud.normalize('NFKD', input_statement).encode('ascii','ignore'))
        response_data = rf.filterresponse(str(response_data))

        return JsonResponse(JSONRenderer().render(response_data),safe=False)


    def put(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        response_data = chatterbot.get_response(json_data["question"])
        map = { "answer" : response_data.text}
        return JsonResponse(map)

class TrainBot(View):

        def post(self, request, *args, **kwargs):
            input_statement = request.POST.get('text')
            with open(os.path.join(BASE_DIR, 'train')) as file:
                content = file.readlines()
            conversation = []
            for line in content:
                for con in line.split(","):
                    conversation.append(con.rstrip())
                s.getBot().train(conversation)
            return JsonResponse(JSONRenderer().render("Bot trained with the given input"), safe=False)

