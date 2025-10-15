-- 8_index_my_names.sql
-- Creates an index on the first letter of names in table

CREATE INDEX idx_name_first
ON names (name(1));
