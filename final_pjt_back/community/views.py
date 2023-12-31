from traceback import print_tb
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count

from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .serializers.review import ReivewListSerializer, ReviewSerializer, ReviewCreationSerializer
from .serializers.comment import CommentSerializer
from .models import Review, Comment

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def review_list(request):
    review = Review.objects.annotate(
        comment_count= Count('comments', distinct=True),
        like_count = Count('like_people', distinct=True)
    ).order_by('-pk')
    serializer = ReivewListSerializer(review, many=True)
    return Response(serializer.data)

class ReviewPagination(PageNumberPagination):
    page_size = 4

class ReviewViewSet(viewsets.ModelViewSet):
    pagination_class = ReviewPagination
    serializer_class = ReivewListSerializer
    queryset = Review.objects.annotate(
        comment_count= Count('comments', distinct=True),
        like_count = Count('like_people', distinct=True)
    ).order_by('-pk')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request):
    serializer = ReviewCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def serach_review(request):
    pass


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def review_detail(request, review_pk):
    review = Review.objects.annotate(
        like_count = Count('like_people', distinct=True)
    ).get(pk=review_pk)
    
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            data = {
                "message": "정상적으로 삭제되었습니다"
            }
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_review(request, review_pk):
    if request.user.is_authenticated:
        review = Review.objects.annotate(
        like_count = Count('like_people', distinct=True)
            ).get(pk=review_pk)
        if review.like_people.filter(pk=request.user.pk).exists():
            review.like_people.remove(request.user)
            review = Review.objects.annotate(
                like_count = Count('like_people', distinct=True)
                ).get(pk=review_pk)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)

        else:
            review.like_people.add(request.user)
            review = Review.objects.annotate(
                like_count = Count('like_people', distinct=True)
                ).get(pk=review_pk)
            serializer = ReviewSerializer(review)
            # print(serializer.data)
            return Response(serializer.data)
        


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, review_pk):
    user=request.user
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, review=review)

        comments = review.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_delete_comment(request, review_pk, comment_pk):
    # review = get_object_or_404(Review, pk=review_pk)
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    print('get')

    if request.method == 'PUT':
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(review=review)

    elif request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
    
    new_comments = review.comments.all()
    serializer = CommentSerializer(new_comments, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_comment(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.like_people.filter(pk=request.user.pk):
        print('del')
        comment.like_people.remove(request.user)
        comments = Comment.objects.filter(review=review_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    else:
        print('cre')
        comment.like_people.add(request.user)
        comments = Comment.objects.filter(review=review_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def filter_reviews(request, movie_pk):
    review = Review.objects.filter(movie=movie_pk).annotate(
                like_count = Count('like_people', distinct=True)
                ).order_by('-like_count')[0:3]
    print(review)
    serializer = ReviewSerializer(review, many=True)
    return Response(serializer.data)