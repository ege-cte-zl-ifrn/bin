FROM ifrn/ege_django_base:1.0

ADD requirements-custom-build.txt /
RUN pip install -r /requirements-custom-build.txt

ADD startup.sh / 
WORKDIR /apps/app
CMD /startup.sh
