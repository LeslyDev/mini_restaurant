from django import forms

from infrastructure.models import Table
from mini_restaurant.settings import EXIST_TIME


class TableForm(forms.Form):
    time = forms.ChoiceField(label="Время бронирования", required=True)
    owner_name = forms.CharField(label="Ваше имя", max_length=15, required=True)
    owner_number = forms.CharField(label="Ваш номер телефона", max_length=12, required=True)

    # @staticmethod
    # def get_available_table_size():
    #     available_table = Table.objects.filter(status='free').order_by('size')
    #     return [table.size for table in available_table]

    def __init__(self, *args, **kwargs):
        super(TableForm, self).__init__(*args, **kwargs)

        self.fields['time'].choices = [(time, time) for time in EXIST_TIME]
