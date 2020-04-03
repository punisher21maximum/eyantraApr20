# WorkFlow

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

