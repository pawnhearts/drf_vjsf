from rest_framework import serializers
from rest_framework.relations import ManyRelatedField

from drf_jsonschema.drf_jsonschema.convert import converter
from drf_jsonschema.drf_jsonschema.converters import Error, Converter


@converter
class PrimaryKeyRelatedFieldConverter:
    field_class = serializers.PrimaryKeyRelatedField

    def convert(self, field):
        return {
            'type': 'integer',
            'anyOf' if isinstance(field.parent, ManyRelatedField) else 'oneOf': [
                {'const': opt.value,
                 'title': opt.display_text}
                for opt in field.iter_options()
            ]
        }

        # try:
        #     url = reverse(f'{field.queryset.model.__name__.lower()}-list')
        #     return {
        #         'type': 'object',
        #         'x-fromUrl': url,
        #         # 'x-itemsProp': '',
        #         'x-itemTitle': 'title',
        #         'x-itemKey': 'href'
        #     }
        # except NoReverseMatch:
        #     return {
        #         'type': 'integer'
        #     }


@converter
class DecimalFieldConverter(Converter):
    # the JSON Schema spec doesn't support decimals, I suggested it should
    # https://github.com/json-schema-org/json-schema-spec/issues/361
    type = 'string'
    field_class = serializers.DecimalField

    def convert(self, field):
        # if field.max_digits is not None:
        #     raise Error("max_digits not yet supported")
        # who cares tbh
        if not getattr(field, 'coerce_to_string', True):
            raise Error("coerce_to_string must be True")
        result = super(DecimalFieldConverter, self).convert(field)
        result['pattern'] = "^\\-?[0-9]*(\\.[0-9]{1,%d})?$" % (
            field.decimal_places)
        return result
