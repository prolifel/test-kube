build:
		docker build -t python-kube-app .

run:
		docker run -p 80:80 python-kube-app