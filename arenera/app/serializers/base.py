from app.models.base import MeasureUnit

from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureUnit
        exclude = ('state','create_date','modified_date','delete_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'description': instance.description,
        }