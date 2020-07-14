#github instructions

#to switch branch:
git checkout branchname

#you can use:
git branch
#to make sure the branch exists

#to create a new branch:
git check out -b newbranchname

#pull the master:
git pull origin master

#sync local repo with github, add new files, then:
git add .

#commit the changes:
git commit -m "message"

#push the origin master:
git push origin master

#to delete a branch:
#locally:
git branch -d localbranchname
#remotely:
git push origin --delete remotebranchname

#to git clone, got to directory and enter: (or whatever git url)
git clone https://github.com/simonegoldman/base/
