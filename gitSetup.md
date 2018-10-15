~$ sudo apt-get install git-core    ---> optional
~$ git config --global user.name    "First Last"
~$ git config --global user.email   "<First.Last>@teradata.com"
  
 # In order to commit, you should configure your editor of choice (vi in this example)
~$ git config --global core.editor vi
   
 # Use shared ignore file regarding "git status"
~$ git config --global core.excludesFile /asterfs/engtools/gitignore --->optional

 # Clone repository
~$ git clone https://github.com/sukumarburra/ML.git
