-- db/step.sql

-- Table to store step information
CREATE TABLE IF NOT EXISTS steps (
  id SERIAL PRIMARY KEY,
  description TEXT NOT NULL,
  case_id INTEGER NOT NULL REFERENCES cases(id) ON DELETE CASCADE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
-- Note: The 'cases' table must exist before creating this table due to the foreign key
-- constraint.
