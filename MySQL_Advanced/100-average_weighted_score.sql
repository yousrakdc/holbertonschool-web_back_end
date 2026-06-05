-- Creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and stores the average weighted score for a student.
DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser$$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;

    SELECT SUM(c.score * p.weight), SUM(p.weight)
        INTO total_weighted_score, total_weight
        FROM corrections AS c
        INNER JOIN projects AS p
            ON c.project_id = p.id
        WHERE c.user_id = user_id;

    IF total_weight = 0 THEN
        UPDATE users SET average_score = 0 WHERE id = user_id;
    ELSE
        UPDATE users
            SET average_score = total_weighted_score / total_weight
            WHERE id = user_id;
    END IF;
END$$

DELIMITER ;