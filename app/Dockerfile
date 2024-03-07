# pull official base image
FROM python:3.10-bullseye

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPYCACHEPREFIX=/root/.cache/pycache/

RUN rm -f /etc/apt/apt.conf.d/docker-clean

# install system dependencies
RUN \
  --mount=type=cache,target=/var/cache/apt \
  apt-get update \
  && apt-get install --no-install-recommends -yqq \
  graphviz=2.42.2-5 \
  && rm -rf /var/lib/apt/lists/*

# install dependencies
COPY ./requirements.txt .
# hadolint ignore=DL3042
RUN \
  --mount=type=cache,target=/root/.cache/ \
  pip install uv==0.1.15 \
  && uv pip install --system -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh \
  && chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
