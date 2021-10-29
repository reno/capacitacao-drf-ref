from django.shortcuts import render
from rest_framework import viewsets
from core.models import Answer, Question
from core.serializers import (
    AnswerListSerializer, QuestionListSerializer, QuestionDetailSerializer
)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuestionDetailSerializer
        else:
            return QuestionListSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerListSerializer
    http_method_names = ['post', 'head']


