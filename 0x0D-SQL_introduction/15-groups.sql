-- Get counts of unique score values.

SELECT score, count(score) AS "number"
FROM second_table
GROUP BY score;
ORDER BY number DESC
