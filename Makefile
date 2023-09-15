push:
	git add -A .
	git commit -m "auto commit"
	git push origin master

deploy: push
	mkdocs gh-deploy