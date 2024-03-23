from rest_framework import serializers



class SlugSerializer(serializers.Serializer):
    slug = serializers.CharField()



class ContactUsSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    email = serializers.EmailField()
    subject = serializers.CharField()
    content = serializers.CharField()