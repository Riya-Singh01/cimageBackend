from rest_framework import serializers

class userDetailsSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    email=serializers.EmailField()
    number=serializers.IntegerField()
    password=serializers.CharField(max_length=50)#write_only=True
    address=serializers.CharField(max_length=100)