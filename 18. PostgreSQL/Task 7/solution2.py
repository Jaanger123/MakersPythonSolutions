"""
SELECT ROUND(AVG(c.speechcount)), w.title FROM character c INNER JOIN character_work cw ON c.charid = cw.charid INNER JOIN work w ON cw.workid = w.workid GROUP BY title HAVING title LIKE 'Romeo and Juliet';
"""