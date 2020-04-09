from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#we cant use decorators on classe (only on funcs)
#we use these classes
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#create update delete
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import PersonAddressModel
from django.contrib.auth.decorators import login_required
#UserPostListView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.
from users.models import Shop, Person, Profile
shop_category_CHOICES=[('dairy','dairy'),('grocery','grocery'),
    ('electronics','electronics'), ('mechanic','mechanic')]
@login_required
def index(request):
	print('shop', Shop, type(Shop), request.user.id)
	# pos_user = Person.objects.filter(user_id=request.user.id).first().
	pos_person = Person.objects.filter(user_id=request.user.id).first().gmap_location
	near_shop = dict()
	for categ in ['dairy','grocery','electronics','mechanic']:
		near_shop[ categ ] = []
		for s in Shop.objects.all():
			print('s.category',s.category, 'categ', categ)
			if s.category ==  categ:
				print('shopdist', s.shop_gmap_location, 'posper', pos_person)

				near_shop[ categ ].append( [s, abs(s.shop_gmap_location - pos_person) ] )

	for cat in near_shop:
		for shops in near_shop[cat]:
			print('cat', cat, ':', 'shop', shops[0].shop_name, shops[1])

	# finding the nearest shop in each category
	nearest_shop = dict()
	for cat in ['dairy','grocery','electronics','mechanic']:
		print('----->', cat)
		all_shops_from_categ = near_shop[cat]
		print(cat, all_shops_from_categ)
		min_dist_shop_object = all_shops_from_categ[0]
		for a_shop in all_shops_from_categ:
			if min_dist_shop_object!=a_shop and a_shop[1]<min_dist_shop_object[1]:
				min_dist_shop_object = a_shop 
		nearest_shop[cat] = min_dist_shop_object
		print('++++++++++', cat, nearest_shop[cat], nearest_shop[cat][1])



	context = {
		'nearest_shop': nearest_shop,
		 
	}


	return render(request, 'myApp/index.html', context)

@login_required
def detail(request, pk):

	context = {"shop_obj":Shop.objects.filter(pk=pk).first()}
	return render(request, 'myApp/detail.html', context)



# class PostListView(ListView):
#     model = PersonAddressModel
#     template_name = 'myApp/index.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'PersonAddressModel' #object_list
#     # ordering = ['-date_posted']
#     paginate_by = 2


# #for posts from particular user
# class UserPostListView(ListView):
#     model = PersonAddressModel
#     template_name = 'myApp/user_posts.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'PersonAddressModel'
#     paginate_by = 2

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return PersonAddressModel.objects.filter(author=user) 




# class PostDetailView(DetailView):
#     model = PersonAddressModel
#     #pk_url_kwarg = 'pk' path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
#     #template_name = 'myApp/personaddressmodel_detail.html'  # <app>/<model>_<viewtype>.html
#     #context_object_name = 'object'


# #LoginRequiredMixin : login rqd to create a post
# class PostCreateView(LoginRequiredMixin, CreateView):
# 	model = PersonAddressModel
# 	fields = ['address_line1','landmark', 'additional_ph_no', 'num_fam_mem']
# 	#template_name = 'myApp/personaddressmodel_form.html'
# 	#override form_valid to add author field in the create form
# 	#why override : bcos our form does not take who created/author of the form
# 	#and it should not bcos author should always be the person logged in
# 	#so that we do manually here.
# 	def form_valid(self, form):
# 		form.instance.author = self.request.user 
# 		return super().form_valid(form)


# #UserPassesTestMixin : defines a test func logged in user has to pass too update
# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
# 	model = PersonAddressModel
# 	fields = ['address_line1','landmark', 'additional_ph_no', 'num_fam_mem']

# 	#template_name = 'myApp/personaddressmodel_form.html'
# 	#same template used for PostCreateView and PostUpdateView

# 	def form_valid(self, form):
# 		form.instance.author = self.request.user 
# 		return super().form_valid(form)

# 	#UserPassesTestMixin : uses this func to check updater is creator
# 	def test_func(self):
# 		post = self.get_object() #consider a particular post / that user trying to update
# 		if self.request.user == post.author:
# 			return True
# 		return False

# 	#self.request.user : post updater
# 	#post.author       : post creator



# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
# 	model = PersonAddressModel
# 	#pk_url_kwarg = 'pk' path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
# 	#template_name = 'myApp/personaddressmodel_confirm_delete.html'  
# 	#<app>/<model>_<confirm_delete>.html
# 	#context_object_name = 'object'
# 	success_url = '/'
# 	def test_func(self):
# 		post = self.get_object() #consider a particular post / that user trying to update
# 		if self.request.user == post.author:
# 			return True
# 		return False


