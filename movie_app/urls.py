
from django.contrib import admin
from django.urls import path, include
from main import views
from movie_app import yasg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movies/', views.MovieListApiView.as_view()),
    path('api/v1/create_movie', views.MovieCreateApiView.as_view()),
    path('api/v1/movies/<int:id>', views.MovieUpdateDeleteApiView.as_view()),
    path('api/v1/directors/', views.DirectorListApiView.as_view()),
    path('api/v1/directors/<int:id>', views.DirectorUpdateDeleteApiView.as_view()),
    path('api/v1/reviews/', views.ReviewListApiView.as_view()),
    path('api/v1/reviews/<int:id>', views.ReviewUpdateDeleteApiView.as_view()),
    # path('api/v1/movies/reviews', views.movie_review_view),
    path('api/v1/users/', include('users.urls')),

]
urlpatterns += yasg.urlpatterns
