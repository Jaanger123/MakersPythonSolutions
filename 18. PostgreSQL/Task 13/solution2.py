"""
SELECT c.chapterid, c.description, w.title FROM chapter AS c INNER JOIN work AS w ON c.workid = w.workid;
"""