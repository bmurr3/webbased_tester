git lfs install
npm install -g @angular/cli
sudo apt-get update && sudo apt-get install -y flex bison perl

mkdir -p /workspaces/downloads/postgresql && curl -o /workspaces/downloads/postgresql.tar.gz https://ftp.postgresql.org/pub/source/v17.6/postgresql-17.6.tar.gz && tar -xvf /workspaces/downloads/postgresql.tar.gz -C /workspaces/downloads/postgresql

cd /workspaces/downloads/postgresql/postgresql-17.6
./configure --with-python
make
sudo make install
sudo adduser --disabled-password --gecos "" postgres
sudo mkdir -p /usr/local/pgsql/data
sudo chown postgres /usr/local/pgsql/data
sudo -s su - postgres -c "/usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data"
sudo -s su - postgres -c "/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data -l logfile start"
sudo -s su - postgres -c "/usr/local/pgsql/bin/createdb webtesterdb"

export LD_LIBRARY_PATH=/usr/local/pgsql/lib:$LD_LIBRARY_PATH
export PATH=/usr/local/pgsql/bin:$PATH
