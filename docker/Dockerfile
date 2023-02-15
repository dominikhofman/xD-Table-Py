# during docker build the container has incorrectly set date
# it could be because docker is outdated, alpine 3.13 requires docker 20.0+
# and currently installed version is 19.0
# FROM arm32v7/python:3.11.2-alpine
FROM arm32v7/python:3.7-stretch

RUN date
RUN apt update && apt install -y vim gcc

# PIL deps
RUN apt-get install -y libtiff5-dev libjpeg62-turbo-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    libharfbuzz-dev libfribidi-dev libxcb1-dev

# Timezone stuff
ENV TZ=Europe/Warsaw
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# force stdout and stderror to be unbuffered
ENV PYTHONUNBUFFERED 1

# prepare code folder
RUN mkdir /code
WORKDIR /code

# install needed modules
RUN python3 -m pip install --upgrade pip

COPY requirements.txt /tmp/
RUN python3 -m pip install -r /tmp/requirements.txt


CMD ["tail", "-f", "/dev/null"]
