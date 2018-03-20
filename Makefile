devserver: html
	jekyll serve

html:
	jekyll build

# generate html and publish to master branch
publish: html
	ghp-import -f -p -b master _site

clean:
	rm _site/* -rf
