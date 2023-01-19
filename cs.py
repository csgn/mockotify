from cassandra.cluster import Cluster

suggest_table = """
CREATE TABLE IF NOT EXISTS Suggest (
     refer_id       VARCHAR
    ,target_id      VARCHAR
    ,referred_at     TIMESTAMP
    ,PRIMARY KEY (refer_id, target_id)
);
"""


def session(keyspace):
    cluster = Cluster(['0.0.0.0'], port=9042)
    session = cluster.connect(keyspace)

    session.execute(suggest_table)

    return session
