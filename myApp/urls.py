from django.urls import path 
from . import views
# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView,
#     UserPostListView
# )


urlpatterns = [

	# path('', PostListView.as_view(), name='index'),
	# path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
	# path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	# path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	# path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	# path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('', views.index, name='index'),
	path('detail/<int:pk>/', views.detail, name='detail'),
	path('my-customers-index/', views.my_customers_index, name='my_customers_index'),
	
]


























