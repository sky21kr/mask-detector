from rest_framework import serializers
from api.models import MaskHistory

class MaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaskHistory
        fields = ('date', 'outing', 'wearing', 'withMask')

    def create(self, validated_data):
        return MaskHistory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.outing = validated_data.get('outing', instance.outing)
        instance.wearing = validated_data.get('wearing', instance.wearing)
        instance.wearing = validated_data.get('withMask', instance.wearing)
        instance.save()
        return instance
