-- 8_index_my_names.sql
-- Creates an index on the first letter of names in table

CREATE INDEX idx_first_letter_names
ON names (name(1));
