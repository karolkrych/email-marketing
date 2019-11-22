from rest_framework import serializers


class SendEmailsSerializer(serializers.Serializer):
    template = serializers.IntegerField(required=True)
    contact = serializers.IntegerField(required=False)
    segment = serializers.IntegerField(required=False)

    def validate(self, data):
        """
        Check if only one of 'contact' and 'segment' values is provided
        """
        if data.get('contact') and data.get('segment'):
            raise serializers.ValidationError('You cannot provide both recipient and segment')
        elif not (data.get('contact') or data.get('segment')):
            raise serializers.ValidationError('You must provide recipient or segment')
        return data

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

