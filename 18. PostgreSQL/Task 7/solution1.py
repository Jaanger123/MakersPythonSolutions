"""
SELECT ROUND(AVG(character.speechcount)), work.title FROM character JOIN character_work ON character.charid = character_work.charid JOIN work ON work.workid = character_work.workid GROUP BY title HAVING title = 'Romeo and Juliet';
"""