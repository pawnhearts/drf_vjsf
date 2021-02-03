from drf_jsonschema import to_jsonschema
from rest_framework.metadata import SimpleMetadata


class JsonSchemaMetadata(SimpleMetadata):

    def determine_metadata(self, request, view):
        metadata = super().determine_metadata(request, view)
        metadata['schema'] = to_jsonschema(view.get_serializer())
        return metadata
