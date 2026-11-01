FROM fluent/fluentd:v1.16-1
USER root
RUN apk add --no-cache --virtual .build-deps build-base ruby-dev \
    && gem install fluent-plugin-elasticsearch --no-document \
    && apk del .build-deps
USER fluent
