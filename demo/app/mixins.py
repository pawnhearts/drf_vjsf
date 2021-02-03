from django.shortcuts import render
from drf_jsonschema import to_jsonschema
from rest_framework.decorators import action
from rest_framework.response import Response


class JsonSchemaMixin(object):
    @action(detail=False, methods=['GET'])
    def schema(self, request):
        return Response(to_jsonschema(self.get_serializer()))

    @action(detail=False, methods=['GET'])
    def html(self, request):
        return render(request, 'vue_form.html', {})
