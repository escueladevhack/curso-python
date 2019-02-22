# Postgres

Para ejecutar un módulo de Postgres Local

```bash
docker run \
    --name postgres \
    -e POSTGRES_PASSWORD=your_secret_password \
    -v ${PWD}/pgdata:/var/lib/postgresql/data \
    -p 5432:5432 \
    -d postgres:9.6.8-alpine
```