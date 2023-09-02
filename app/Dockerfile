# pull official base image
FROM python:3.10-bullseye

ARG workdir_prefix=/usr/src
ENV WORKDIR_PREFIX $workdir_prefix

# set work directory
WORKDIR $WORKDIR_PREFIX/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN \
  --mount=type=cache,target=/var/cache/apt,sharing=locked \
  --mount=type=cache,target=/var/lib/apt,sharing=locked \
  apt-get update \
  && apt-get --no-install-recommends install -y \
  netcat=1.10-46 \
  gcc=4:10.2.1-1 \
  postgresql=13+225 \
  graphviz=2.42.2-5
# no need to do the following since it's also cached
#  rm -rf /var/lib/apt/lists/*

# install dependencies
RUN \
  --mount=type=cache,target=/root/.cache \
  pip install pip~=21.3.1
COPY ./requirements.txt .
RUN \
  --mount=type=cache,target=/root/.cache \
  pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' $WORKDIR_PREFIX/app/entrypoint.sh \
  && chmod +x $WORKDIR_PREFIX/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["sh", "-c", "$WORKDIR_PREFIX/app/entrypoint.sh $0 $@"]
