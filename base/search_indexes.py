from haystack import indexes
from base.models import Phage

class PhageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    spanin_type = indexes.IntegerField(model_attr='spanin_type')
    name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Phage

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
