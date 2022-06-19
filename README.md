echo "# csw-backend" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Malin-Greats/csw-backend.git
git push -u origin main

ssh-keygen -t rsa -f ~/.ssh/csw-backend -b 4096 -C "csworgzw@csw.org.zw"

ssh -i ~/.ssh/csw-backend -T git@github.com
