# Axelspace Coding Test

- [Algorithm test](./algorithm-test/)
- [SQL test](./sql-test/)

## Memo

### SQL test

- I had to update the `psycopg2-binary` package to include the following commit: https://github.com/psycopg/psycopg2/commit/c96f991a8da73d9bebffe7fe9e69b191d36cceef
- When composing geometry form GeoJSON in PostGIS, I needed specify CRS to be EPSG:4326 in the JSON to match with what's compared.
