from haystack.backends.whoosh_backend import WhooshEngine, WhooshSearchBackend
from haystack.backends.whoosh_backend import NGRAM

class CustomSearchBackend(WhooshSearchBackend):
    def build_schema(self, fields):
        content_field_name, schema = super(CustomSearchBackend, self).build_schema(fields)

        for field_name, field_class in fields.items():
            if field_class.field_type == 'ngram':
                schema.remove(field_class.index_fieldname)
                schema.add(field_class.index_fieldname,
                           NGRAM(minsize=1, maxsize=15, stored=field_class.stored, field_boost=field_class.boost)
                           )

        return content_field_name, schema

class CustomWhooshEngine(WhooshEngine):
    backend = CustomSearchBackend
