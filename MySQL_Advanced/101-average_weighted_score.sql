-- Creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and stores the average weighted score for all students.
DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers$$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS u
        INNER JOIN (
            SELECT c.user_id,
                   SUM(c.score * p.weight) / SUM(p.weight) AS weighted_avg
            FROM corrections AS c
            INNER JOIN projects AS p
                ON c.project_id = p.id
            GROUP BY c.user_id
        ) AS scores
        ON u.id = scores.user_id
        SET u.average_score = scores.weighted_avg;
END$$

DELIMITER ;