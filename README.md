- Druid setup adopted from https://github.com/apache/druid/blob/27.0.0/distribution/docker/docker-compose.yml
- Superset should adopt - https://github.com/apache/superset/blob/master/docker-compose-non-dev.yml

## How to setup

```sh
docker compose up -d
poetry run python setup_druid_users.py
poetry run python setup_superset.py
```

## How to use


Component | URL | Auth
----------|-----|-----
Droid | http://localhost:8888 | admin/password1
Superset | http://localhost:8080 | admin/password1
Ozone UI | http://localhost:9876/ | -


## Notes

- Uses version 25, just because I was able to find ARM images for that version.
