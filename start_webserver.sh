#!/bin/bash

# Start the PostgreSQL webtesterdb database server.
sudo -s su - postgres -c "/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data -l logfile start"

# Build the project database schema.
./db/create_db.sh

