from datetime import datetime
from functools import lru_cache

import pandas as pd

from cs import session

import tables

session.execute(tables.suggest_table)

N = 5
df = pd.read_parquet("./assets/final_matrix")


@lru_cache
def recommend(track_id):
    try:
        c = df.loc[track_id][1:]
    except KeyError:
        return False, f"IS_NOT_EXISTS"

    si = c.to_numpy().argpartition(range(-1, -N, -1))
    ind = c.index

    similarity_df = ind[si[-1:-(N+2):-1]].drop(c, errors="ignore")

    return True, list(similarity_df.to_numpy())

def run(refer_id):
    status, data = recommend(refer_id)

    if not status:
        return

    rows = session.execute(f"""
        SELECT * FROM suggest
        WHERE refer_id = '{refer_id}'
    """)

    rows = [i for i in rows]
    targets = [i.target_id for i in rows]

    for d in data:
        # not exist
        if d not in targets:
            session.execute(f"""
                INSERT INTO suggest (refer_id, target_id, referred_at)
                VALUES ('{refer_id}', '{d}', toTimeStamp(now()))
            """)
        # exist
        else:
            old = list(filter(lambda x: x.target_id == d, rows))[0]

            # refresh referred_at after 60 minute
            if (datetime.now() - old.referred_at).total_seconds() / 60.0 % 18 >= 60.0:
                session.execute(f"""
                    UPDATE suggest SET referred_at = toTimeStamp(now())
                    WHERE target_id = '{d}' and refer_id = '{refer_id}'
                """)
