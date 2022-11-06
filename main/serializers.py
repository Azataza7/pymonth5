from rest_framework import serializers
from .models import Movie, Review, Director
from rest_framework.exceptions import ValidationError


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars movie'.split()


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movies_count'.split()


class MovieSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True)
    director = DirectorSerializers()

    class Meta:
        model = Movie
        fields = 'id title description duration director reviews rating'.split()
        # fields = 'id title description'.split()
        # exclude = 'id'.split()


class DirectorCountSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'movies_count'.split()

    def get_movie_count(self, movie):
        return movie.all().count()


class MovieValidateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=50)
    description = serializers.CharField()
    duration = serializers.IntegerField(required=False)
    director_id = serializers.IntegerField()

    def validate_title(self, title):
        if Movie.objects.filter(title=title):
            raise ValidationError("Select unique name for your movie")
        return title


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField(required=False, max_value=5)

    def validate_movie_id(self, movie_id):
        try:
            Review.objects.get(movie_id=movie_id)
        except:
            raise ValidationError("Choose correct id movie")
        return movie_id


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)

    def validate_name(self, name):
        if Director.objects.filter(name=name):
            raise ValidationError("This name is already exists")
        return name





