"""
SELECT c.chapterid, c.description, w.title FROM chapter c FULL JOIN work w ON c.workid = w.workid;
"""