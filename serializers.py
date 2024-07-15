from rest_framework import serializers
from .models import Topic, Comment

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'message', 'course_name', 'creation_date', 'author']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'topic', 'message', 'author', 'creation_date']
