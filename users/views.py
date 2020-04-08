from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
#for msgs
from django.contrib import messages
#to redirect the user when valid form is submitted
from django.shortcuts import redirect
#extend UserCreationForm to add email n all
from .forms import UserRegisterForm
#decorators : login required
from django.contrib.auth.decorators import login_required


def register(request):
	if request.method == 'POST':#2)when user fills the form and submit it

		#create form using request.POST data
		form = UserRegisterForm(request.POST) #x1 #UserCreationForm(request.POST)

		if form.is_valid():#if form valid


			#save the user
			form.save()

			#optional : flash success msg
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}! Login now!')

			#redirect to home page
			return redirect('login')

		#else : #if invalid form --> return to form page with form data saved bcos of x1

	else :#1)when user visit page for first time 
		form = UserRegisterForm()#UserCreationForm()

	#return the form
	return render(request, 'users/register.html', {'form':form})

#update forms : sent to profile.html
from .forms import UserUpdateForm, ProfileUpdateForm

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        print(p_form.instance.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        print(request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/profile.html', context)


from .forms import PersonUpdateForm, ShopUpdateForm

@login_required
def person_address(request):
	if request.method == 'POST':
		try:
			person_form = PersonUpdateForm(request.POST, instance=request.user.person)
		except:
			person_form = PersonUpdateForm(request.POST)
		# person_form = PersonUpdateForm(request.POST, instance=request.user.person)
		person_form.instance.user = request.user

		if person_form.is_valid() :
				person_form.save()
				messages.success(request, f'person address has been updated!')
				return redirect('index')

	else:
		try:
			person_form = PersonUpdateForm(instance=request.user.person)
		except:
			person_form = PersonUpdateForm()

	context = {
        'person_form': person_form
    }

	return render(request, 'users/person_address.html', context)


@login_required
def shop_address(request):
	if request.method == 'POST':
		try:
			shop_form = ShopUpdateForm(request.POST, instance=request.user.shop)
		except:
			shop_form = ShopUpdateForm(request.POST)

		# shop_form = ShopUpdateForm(request.POST, instance=request.user.shop)
		shop_form.instance.user = request.user

		if shop_form.is_valid():

			shop_form.save()
			messages.success(request, f'Shop address has been updated!')
			return redirect('index')

	else:
		try:
			shop_form = ShopUpdateForm(instance=request.user.shop)
		except:
			shop_form = ShopUpdateForm()

	context = {
        'shop_form': shop_form
    }

	return render(request, 'users/shop_address.html', context)

