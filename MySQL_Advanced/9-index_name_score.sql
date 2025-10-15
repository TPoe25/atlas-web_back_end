-- SQL script which creates an index on first letter of name
-- Only the first Character of the name and the score should be indexed

CREATE INDEX idx_name_first_score
ON names (name(1), score);
