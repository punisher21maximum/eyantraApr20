# WorkFlow

## Dont work directly on master branch
step1 : create a branch for a feature you want to work on
$ git branch print-uni # 1.created branch, print-uni
$ git branch # check if branch created
 * master # * means - current branch
   print-uni
$ git checkout print-uni # 2.switch to that print-uni branch

step2 : 
#inside print-uni branch
1.make changes to anyfile you want all over djangowebsite
2.$ git add -A
3.$ git commit -m 'joey' #add messages properly
it has no effect on remote repo yet.
#add messages using vim
3.$ git commit 
opens vim 
write msg
press i
press Esc
press :wq
#add msgs using nano
3.$ git commit 
write msg
ctrl + x
y
press enter


step3 : 
#change remote repo
$ git push -u origin print-uni

step4 :
#1. switch to master
$ git checkout master
#2. check if changes to (origin master) made by someone else (remote one)
$ git pull origin master

#print-uni not yet branch of master
$ git branch  #branches we have merged so far
*master
#3. merge print-uni (to master)
$ git merge print-uni
#git branch --merged
*master
print-uni

#4. push change to origin(remote repo)
$ git push origin master

step5 :

once you have merged a branch to the master you can delete it
#1. delete locally
$ git branch -d print-uni
#2. delete from remote repo
$ git push origin --delete print-uni

