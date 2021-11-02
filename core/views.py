from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.models import Answer, Question
from core.serializers import (
    AnswerListSerializer, QuestionListSerializer, QuestionDetailSerializer
)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuestionDetailSerializer
        else:
            return QuestionListSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['post', 'head']


