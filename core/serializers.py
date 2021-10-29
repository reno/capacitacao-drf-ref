from rest_framework import serializers
from core.models import Answer, Question


class AnswerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            'id', 'question', 'content', 'user', 'created_at',
        ]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        answer = super(AnswerListSerializer, self).create(
            validated_data)
        return answer


class QuestionListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='core:question-detail')

    class Meta:
        model = Question
        fields = [
            'url', 'title', 'content', 'created_at', 'user',
        ]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        question = super(QuestionListSerializer, self).create(validated_data)
        return question


class QuestionDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='core:question-detail')
    answer_set = AnswerListSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'url', 'title', 'content', 'created_at', 'user', 'answer_set'
        ]

