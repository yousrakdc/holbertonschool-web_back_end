-- Creates a stored procedure ComputeAverageScoreForUser that computes and stores the average score for a student
-- Procedure ComputeAverageScoreForUser takes 1 input: user_id

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;
    
    -- Calculate the average score for the user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE corrections.user_id = user_id;
    
    -- Update the user's average_score
    UPDATE users
    SET average_score = IFNULL(avg_score, 0)
    WHERE id = user_id;
END$$

DELIMITER ;