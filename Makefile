SHELL = /bin/bash
PACKAGE = mobsuccess-chalice-spec


test:
	pytest

black:
	docker run --rm -v $$PWD:/app -w /app public.ecr.aws/u9q7y3l4/github-actions-black

flake8:
	docker run --rm -v $$PWD:/app -w /app public.ecr.aws/u9q7y3l4/github-actions-flake8

pyright:
	pyright

stubs:
	@find ${PACKAGE} -name '*.pyi' | xargs rm -f && pyright --createstub ${PACKAGE} && \
	(docker run --rm -v $$PWD:/opt ubuntu:20.04 sh -c 'cd /opt && cd typings/${PACKAGE} && find . -type f | grep ''.pyi$$'' | xargs -r -n1 mv -t ../../${PACKAGE}') && \
	rm -rf typings/${PACKAGE} && (rmdir typings 2>/dev/null || true)
