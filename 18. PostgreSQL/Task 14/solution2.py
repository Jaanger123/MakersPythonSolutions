"""
SELECT p.paragraphnum, c.charname, c.speechcount FROM paragraph AS p INNER JOIN character AS c ON c.charid = p.charid;
"""