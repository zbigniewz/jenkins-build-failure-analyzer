
build:
	docker build -t jenkins-build-failure-analyzer .

run:
	docker run --rm -t jenkins-build-failure-analyzer https://jenkins.zanox.com zx Zanox@Berlin z-de-graph01.zanox.com 8125 infrastructure.jenkins.failed_jobs