from rest_framework import serializers

from basedata.models import Human, Dog


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'


class HumanAndFriendsSerializer(serializers.ModelSerializer):
    friends = DogSerializer(many=True, read_only=True)

    class Meta:
        model = Human
        fields = '__all__'
