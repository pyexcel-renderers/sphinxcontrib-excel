

pip freeze
nosetests --with-cov --cover-package pyexcel_spexcel --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source pyexcel_spexcel && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
