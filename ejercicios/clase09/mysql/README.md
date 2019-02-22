# Postgres

Para ejecutar un módulo de Postgres Local

```bash
docker run \
    --name mariadb \
    -e MYSQL_ROOT_PASSWORD=my-secret-pw \
    -p 3306:3306 \
    -d mariadb
```
