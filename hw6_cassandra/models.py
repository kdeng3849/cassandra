from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

# Create your models here.
filename = columns.Text(primary_key=True)
content = columns.Blob()
