from django.shortcuts import render, get_object_or_404, redirect
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
from django.contrib import messages
# Create your views here.
from users.models import Shop, Person, Profile
shop_category_CHOICES=[('dairy','dairy'),('grocery','grocery'),
    ('electronics','electronics'), ('mechanic','mechanic')]

#email
from django.core.mail import send_mail
# send_mail('subject', 'you are logged in', 'vishal7x7@gmail.com', ['effort21pool@gmail.com'])


from django.core.mail import EmailMultiAlternatives
def func(request):
	subject, from_email, to = 'hello', 'vishal7x7@gmail.com', 'effort21pool@gmail.com'
	text_content = 'This is vishal, we are the hero'
	html_content = 'This is <h1>vishal , we are the hero</h1>'
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.attach_file(request.user.profile.image.url)
	msg.send()




@login_required
def index(request):
	# func(request)
	try:

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


		


				


				#check of that shop is current user's shop



		context = {
			'nearest_shop': nearest_shop,
		}
	except:
		messages.warning(request, f'Fill person-address form first')
		return redirect('person-address')

	return render(request, 'myApp/index.html', context)

@login_required
def my_customers_index(request):
	#for show view - get all persons for that shop
	#check if user has a shop
	current_shop_obj = Shop.objects.filter(user_id=request.user.id).first()
	print('\n\n\n\n\n\n\n')
	print('current_shop', current_shop_obj)
	if current_shop_obj == None:
		# print("No shops", current_shop_obj)
		context = {"my_customers": None}
	else:
		current_shops = []
		current_cat = current_shop_obj.category
		print('current_cat', current_cat)
		all_shops_in_current_cat = Shop.objects.filter(category=current_cat)
		print('all_shops_in_current_cat', all_shops_in_current_cat)
		for p in Person.objects.all():
			x1 = p.gmap_location
			#find nearest shop to each person in that category
			min_dist_shop_object = all_shops_in_current_cat[0]
			print('for person', p)
			print('		all shops---')
			for s in all_shops_in_current_cat:
				print('s-', s)
				print(min_dist_shop_object!=s, (s.shop_gmap_location-x1), (min_dist_shop_object.shop_gmap_location-x1))
				if min_dist_shop_object!=s and abs(s.shop_gmap_location-x1)<abs(x1-min_dist_shop_object.shop_gmap_location):
					min_dist_shop_object = s
					# print('smaller dist shop obj ----------->',s)
			print('		nearest shop', min_dist_shop_object)

			if min_dist_shop_object==current_shop_obj:
				current_shops.append(p)
				# print('same user --------------------------------->',s)
				# print('uk', p.user, min_dist_shop_object, request.user,current_shop_obj)

		context = {"my_customers": current_shops}

		#send email to my customers

		for cust in current_shops:
			sub = f"You can visit  {current_shop_obj.category} today "
			msg = f'''
			\n\n
			Visit  <h1>{current_shop_obj.shop_name}<h1>
			shop owner <h3>{current_shop_obj.user}</h3> 
			shop address : <h2>{current_shop_obj.shop_address_line1}, {current_shop_obj.shop_address_line2},{current_shop_obj.shop_address_line3}</h2>
			location : <h2>{current_shop_obj.shop_gmap_location}</h2>
			'''
			to = cust.user.email
			# print(sub, msg, to)
			# send_mail(sub, msg, 'vishal7x7@gmail.com', [to])

			msg = EmailMultiAlternatives(sub, msg, 'vishal7x7@gmail.com', [to])
			msg.attach_alternative(msg, "text/html")
			# msg.attach_file(request.user.profile.image.url)
			try:
				msg.send()
			except:
				pass

		#email to shopkeeper
		sub="These people will visit you today"
		total = len(current_shops)
		text_content=f"Total count : {total}"
		for cust in current_shops:
			text_content+=f'''
			\n\n
			<h1 style="font-color:red;">{cust.user} {cust.user.last_name}</h1>
			<h3>{cust.user.profile.phone_number}<h3>
			adhaar number <h3>{cust.user.profile.adhaar_no}<h3>
			num of family members <h3>{cust.user.person.num_fam_mem}<h3>
			Distance from you {abs(cust.user.person.gmap_location-request.user.shop.shop_gmap_location)} km
			'''
		# send_mail(sub, msg, 'vishal7x7@gmail.com', ['effort21pool@gmail.com'])
		subject, from_email, to = "These people will visit you today", 'vishal7x7@gmail.com', 'effort21pool@gmail.com'
		# text_content = 'This is vishal, we are the hero'
		html_content = text_content
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		# msg.attach_file(request.user.profile.image.url)
		msg.send()


	return render(request, 'myApp/my_customers_index.html', context)


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


