from drf_jsonschema import to_jsonschema
from rest_framework.metadata import SimpleMetadata


class JsonSchemaMetadata(SimpleMetadata):

    def determine_metadata(self, request, view):

        metadata = super().determine_metadata(request, view)
        if serializer := getattr(view, 'get_serializer', getattr(view, 'serializer_class', None))():
            metadata['schema'] = to_jsonschema(serializer)
            metadata['url'] = view.request.path
            metadata['detail'] = view.detail

        return metadata
