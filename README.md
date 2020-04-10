# website link : http://fightcovid2021.herokuapp.com/

### Title : 
# fightcovid2021

## Description : 


We will take all details and gmap location
Of people and shops on locality

Then in each category like grocery, mechanic, mobile repair, medical shop
We will assign the nearest shop to people of locality


We will divide people into different group 
So they can visit different shops in different category
Once/twice a week at particular hours of the day

Maintaining social distancing and avoiding panick to when they will buy food and essentials.

Groups size of locality = 315 people (45x3)

Sub-group size = 45people  (15x3)

Further sub-group (batch) size = 15

No. of grocery shops they go to = 1 (Always)

batch 1 = 9:00-13:00 hrs

batch 2 = 14:00-18:00 hrs

batch 3 = 19:00-23:00 hrs



## Software requirements :<br>
chardet==2.3.0 <br>
Django==3.0  <br>
gunicorn==20.0.4  <br>
idna==2.9 <br>
python-dateutil==2.4.2 <br>
pytz==2019.3 <br>
requests==2.9.1 <br>
urllib3==1.13.1 <br>
django-bootstrap==0.2.4 <br>
django-crispy-forms==1.9.0 <br>
Pillow==7.1.1 <br>

## Process flow<br>
1.User register : fill username, email, password<br>
2.User fill profile form : his personal details<br>
3.User fill shop form : if he owns a shop<br>
4.As buyer role : gets a email of nearest shop to him in different category<br>
As shopkeeper role : gets email a list of people who will visit him today, with adhaar no, name etc to verify the buyer<br>

## Dont work directly on master branch
step1 : create a branch for a feature you want to work on <br>
$ git branch print-uni # 1.created branch, print-uni <br>
$ git branch # check if branch created <br>
 * master # * means - current branch<br>
   print-uni<br>
$ git checkout print-uni # 2.switch to that print-uni branch<br>

step2 : <br>
#inside print-uni branch<br>
1.make changes to anyfile you want all over djangowebsite<br>
2.$ git add -A<br>
3.$ git commit -m 'joey' #add messages properly<br>
it has no effect on remote repo yet.<br>
#add messages using vim<br>
3.$ git commit <br>
opens vim <br>
write msg<br>
press i<br>
press Esc<br>
press :wq<br>
#add msgs using nano<br>
3.$ git commit <br>
write msg<br>
ctrl + x<br>
y<br>
press enter<br>


step3 : <br>
#change remote repo<br>
$ git push -u origin print-uni<br>
<br>
step4 :<br>
#1. switch to master<br>
$ git checkout master<br>
#2. check if changes to (origin master) made by someone else (remote one)<br>
$ git pull origin master<br>

#print-uni not yet branch of master<br>
$ git branch  #branches we have merged so far<br>
*master<br>
#3. merge print-uni (to master)<br>
$ git merge print-uni<br>
#git branch --merged<br>
*master<br>
print-uni<br>

#4. push change to origin(remote repo)<br>
$ git push origin master<br>

step5 :<br>

once you have merged a branch to the master you can delete it<br>
#1. delete locally<br>
$ git branch -d print-uni<br>
#2. delete from remote repo<br>
$ git push origin --delete print-uni<br>

