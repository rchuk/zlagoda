FROM openapitools/openapi-generator-cli

CMD /usr/local/bin/docker-entrypoint.sh generate \
    -i /in/api/_index.yaml \
    -g typescript-fetch \
    -o /out/web_src/generated;
