# Spanin Backend [![Docker Repository on Quay](https://quay.io/repository/tamu_cpt/spanindb/status "Docker Repository on Quay")](https://quay.io/repository/tamu_cpt/spanindb)

Backend to showcase Rohit Kongari's Spanin Data. Published on the [CPT Site](https://cpt.tamu.edu/spanindb/)

## How to rebuild database
First, delete db and migrate
```console
$ rm db.sqlite3
$ python manage.py migrate
```
Next, download the biomolecular ('2CS') and unimolecular ('1CS') sheets inside the master spanindb google sheet as CSV.
Import these into the database by running:
```console
$ python manage.py import_biomol_spanins path/to/biomol.csv
$ python manage.py import_unimol_spanins path/to/unimol.csv
```
Finally, clear and rebuild stuff for Haystack sorting
```console
$ python manage.py clear_index
$ python manage.py rebuild_index
```
Redeploy.

## License

Code: AGPLv3

Data: Proprietary. Applies to contents of db.sqlite3.
