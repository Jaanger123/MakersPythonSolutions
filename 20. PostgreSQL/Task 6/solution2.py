"""
SELECT c.charname, c.speechcount, w.title FROM character as c INNER JOIN character_work as cw ON c.charid = cw.charid INNER JOIN work as w ON cw.workid = w.workid;
"""