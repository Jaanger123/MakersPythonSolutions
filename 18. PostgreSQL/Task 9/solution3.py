"""
SELECT charname, speechcount FROM character WHERE speechcount IN (SELECT * FROM GENERATE_SERIES(15, 30));
"""