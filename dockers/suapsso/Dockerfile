FROM python:3.7
ENV PYTHONUNBUFFERED 1
ADD requirements-build.txt . 
ADD startup.sh . 
RUN pip install --upgrade pip
RUN pip install -r requirements-build.txt
WORKDIR /apps/suapsso
CMD /startup.sh

