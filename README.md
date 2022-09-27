run `uvicorn main:app --reload ` in terminal

go to `http://127.0.0.1:8000/docs` for swagger ui

pg_dump ` pg_dump --host localhost --port 5432 --username root --format plain --verbose --file "/Users/jaykangheo/stock-backtesting-server/stock.sql" --table public.stocks postgres`

pg_restore ` psql --host localhost --port 5432 --username root --dbname postgres -f "/Users/jaykangheo/stock-backtesting-server/stock.sql"`