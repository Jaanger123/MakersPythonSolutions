"""
SELECT title FROM work WHERE totalwords > (SELECT SUM(totalwords) FROM work) / (SELECT COUNT(*) FROM work);
"""