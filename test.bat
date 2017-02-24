pip freeze
nosetests --with-cov --cover-package sphinxcontrib --cover-package tests  tests  sphinxcontrib && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
