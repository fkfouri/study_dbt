#!/bin/bash

POSTGRES_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
echo "Creating database ${POSTGRES_DB}..."

psql ${POSTGRES_URL} -f .devcontainer/setup-postgres.sql 
