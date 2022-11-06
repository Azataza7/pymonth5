from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import MovieSerializers, ReviewSerializers, DirectorSerializers,\
    MovieValidateUpdateSerializer, ReviewValidateSerializer, DirectorValidateSerializer
from .models import Movie, Review, Director
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStaffUser


@api_view(['GET', 'POST'])
@permission_classes([IsStaffUser])
def movie_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = MovieValidateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        movie = Movie.objects.create(
            title=serializer.validated_data.get('title'),
            description=serializer.validated_data.get('description'),
            duration=serializer.validated_data.get('duration'),
            director_id=serializer.validated_data.get('director_id'),
        )
        return Response(data=MovieSerializers(movie).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Movie not found'})
    if request.method == 'GET':
        serializer = MovieSerializers(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={'message': 'Movie has been deleted'},
                        status=status.HTTP_204_NO_CONTENT)
    else:
        movie = Movie.objects.create(
            **request.data
        )
        movie.save()
        return Response(data=MovieSerializers(movie).data,
                        status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializers(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        review = Review.objects.create(
            text=serializer.validated_data.get('text'),
            stars=serializer.validated_data.get('stars'),
            movie_id=serializer.validated_data.get('movie_id'),
        )
        return Response(data=ReviewSerializers(review).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not found'})
    if request.method == 'GET':
        serializer = ReviewSerializers(review)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        review = Review.objects.create(
            **request.data
        )
        return Response(data=ReviewSerializers(review).data,
                        status=status.HTTP_202_ACCEPTED)
    else:
        review.delete()
        return Response(data={'message': 'Review has been deleted'},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def director_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializers(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        director = Director.objects.create(
            name=serializer.validated_data.get('name'),
        )
        return Response(data=DirectorSerializers(director).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Director not found'})
    if request.method == 'GET':
        serializer = DirectorSerializers(director)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        director = Director.objects.create(
            **request.data
        )
        return Response(data=DirectorSerializers(director).data,
                        status=status.HTTP_202_ACCEPTED)
    else:
        director.delete()
        return Response(data={'message': 'Director has been deleted'},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movie_review_view(request):
    movie_review = Movie.objects.all()
    data = MovieSerializers(movie_review, many=True).data
    return Response(data=data)
