PS D:\Python> pip install cv2
PS D:\Python> python .\cam_demo.py
PS D:\Python> python .\cam_demo.py
Image captured and saved as 'captured_image.png'.
PS D:\Python> python .\cam_demo.py
PS D:\Python> python .\cam_demo.py
PS D:\Python> python .\record_video.py
PS D:\Python>
 *  History restored 

           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--no-lazy-fetch]
           [--no-optional-locks] [--no-advice] [--bare] [--git-dir=<path>]
           [--work-tree=<path>] [--namespace=<name>] [--config-env=<name>=<envvar>]
           <command> [<args>]
PS D:\Python> git config --global user.email "bunnyvishnu2003@gmail.com"
PS D:\Python> git config --global user.name "Vishnu"
PS D:\Python> echo "# python_code" >> README.md
PS D:\Python> git init        
Initialized empty Git repository in D:/Python/.git/
PS D:\Python> git add README.md
PS D:\Python> git status
On branch master

No commits yet
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        anil/
        cam_demo.py
        record_video.py
        simple.py
        sum_example.py

PS D:\Python> git add .
warning: in the working copy of 'anil/.gitignore', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'anil/package-lock.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'anil/package.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'anil/public/index.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'anil/public/manifest.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'anil/public/robots.txt', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'anil/src/App.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'anil/src/App.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'anil/src/App.test.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'anil/src/index.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'anil/src/index.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'anil/src/reportWebVitals.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'anil/src/setupTests.js', LF will be replaced by CRLF the next time Git touches it
PS D:\Python> git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
        new file:   anil/.gitignore
        new file:   anil/README.md
        new file:   anil/package-lock.json
        new file:   anil/package.json
        new file:   anil/public/favicon.ico
        new file:   anil/public/index.html
        new file:   anil/public/logo192.png
        new file:   anil/public/logo512.png
        new file:   anil/public/manifest.json
        new file:   anil/public/robots.txt
        new file:   anil/src/App.js
        new file:   anil/src/App.test.js
        new file:   anil/src/index.css
        new file:   anil/src/index.js
        new file:   anil/src/logo.svg
        new file:   anil/src/reportWebVitals.js
        new file:   anil/src/setupTests.js
        new file:   cam_demo.py
        new file:   record_video.py
        new file:   simple.py
        new file:   sum_example.py

PS D:\Python> git commit -m "Implemented the python code"
[master (root-commit) 37422ca] Implemented the python code
 23 files changed, 20128 insertions(+)
 create mode 100644 README.md
 create mode 100644 anil/.gitignore
 create mode 100644 anil/README.md
 create mode 100644 anil/package-lock.json
 create mode 100644 anil/package.json
 create mode 100644 anil/public/favicon.ico
 create mode 100644 anil/public/index.html
 create mode 100644 anil/public/logo192.png
 create mode 100644 anil/public/logo512.png
 create mode 100644 anil/public/manifest.json
 create mode 100644 anil/src/App.css
 create mode 100644 anil/src/App.js
 create mode 100644 anil/src/index.css
 create mode 100644 anil/src/index.js
 create mode 100644 anil/src/logo.svg
 create mode 100644 anil/src/reportWebVitals.js
 create mode 100644 anil/src/setupTests.js
 create mode 100644 cam_demo.py
 create mode 100644 record_video.py
PS D:\Python> git stag 
The most similar command is
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?
PS D:\Python> git status
On branch master
nothing to commit, working tree clean
PS D:\Python> git branch
* master
PS D:\Python> git branch -M main
PS D:\Python> git branch 
* main
PS D:\Python> git remote add origin https://github.com/VISHNUROYAL2003/python_code.git
PS D:\Python> git remote -v
origin  https://github.com/VISHNUROYAL2003/python_code.git (fetch)
origin  https://github.com/VISHNUROYAL2003/python_code.git (push)
PS D:\Python> git push origin main
info: please complete authentication in your browser...
Enumerating objects: 28, done.
Counting objects: 100% (28/28), done.
Delta compression using up to 2 threads
Compressing objects: 100% (25/25), done.
Writing objects: 100% (28/28), 181.57 KiB | 4.13 MiB/s, done.
Total 28 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/VISHNUROYAL2003/python_code.git
 * [new branch]      main -> main
PS D:\Python>