from logging import raiseExceptions
from tkinter import getboolean
from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from .serializers.review import ReivewListSerializer, ReviewSerializer
from .serializers.comment import CommentSerializer
from .models import Review, Comment

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def review_list(request):
    review = get_list_or_404(Review)
    serializer = ReivewListSerializer(review, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_review(request):
    serializer = ReviewSerializer(data=request.data)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    def review_detail():
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    def update_review():
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    def delete_review():
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        review_detail()
    
    elif request.method == 'PUT':
        if request.user == review.user:
            update_review()
    
    elif request.method == 'DELETE':
        if request.user == review.user:
            delete_review()

@api_view(['POST'])
def like_review(request, review_pk):
    if request.user.is_authenticatd:
        review = get_object_or_404(Review, pk=review_pk)
        if review.like_people.filter(pk=request.user.pk).exists():
            review.like_people.remove(request.user)

        else:
            review.like_people.add(request.user)
        


@api_view(['POST'])
def create_comment(request, review_pk):
    user=request.user
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, review=review)

        comments = review.comment_set.all()
        serializer = Comment(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def update_delete_comment(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = review.comment_set.all()
                serializer = Comment(comments, many=True)
                return Response(serializer.data)
        

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = review.comment_set.all()
            serializer = Comment(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        update_comment()
    elif request.method == 'DELETE':
        delete_comment()