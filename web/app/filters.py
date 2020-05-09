from django_filters import filters
from django_filters import FilterSet
from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    name = filters.CharFilter(label='氏名', lookup_expr='contains')
    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('name', 'name'),
            ('no', 'no'),
        ),
        field_labels={
            'name': '氏名',
            'no': '図鑑番号',
        },
        label='並び順'
    )

    class Meta:

        model = Item
        fields = ('name', 'type1', 'type2','ability1','ability2','hidden_ability','h','a','b','c','d','s','memo',)