suggest_table = """
CREATE TABLE IF NOT EXISTS Suggest (
     refer_id       VARCHAR
    ,target_id      VARCHAR
    ,referred_at     TIMESTAMP
    ,PRIMARY KEY (refer_id, target_id)
);
"""

