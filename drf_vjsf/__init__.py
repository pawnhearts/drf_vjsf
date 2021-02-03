from drf_jsonschema import converters
from .converters import PrimaryKeyRelatedFieldConverter, DecimalFieldConverter
from rest_framework.metadata import SimpleMetadata


# Yeah, I know :-/
converters.PrimaryKeyRelatedFieldConverter = PrimaryKeyRelatedFieldConverter
converters.DecimalFieldConverter = DecimalFieldConverter


class JsonSchemaMetadata(SimpleMetadata):

    def determine_metadata(self, request, view):
        from drf_jsonschema import to_jsonschema

        metadata = super().determine_metadata(request, view)
        if serializer := getattr(view, 'get_serializer', getattr(view, 'serializer_class', None)):
            metadata['schema'] = to_jsonschema(serializer)
            metadata['url'] = view.request.path
            metadata['detail'] = view.detail

        return metadata
