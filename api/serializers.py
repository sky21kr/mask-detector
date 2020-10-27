from rest_framework import serializers
from api.models import Article
from api.models import MaskHistory

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'source', 'date')

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.source = validated_data.get('source', instance.source)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

class MaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaskHistory
        fields = ('date', 'outing', 'wearing')

    def create(self, validated_data):
        return MaskHistory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.outing = validated_data.get('outing', instance.outing)
        instance.wearing = validated_data.get('wearing', instance.wearing)
        instance.save()
        return instance
