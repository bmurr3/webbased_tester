-- db/case.sql

-- Table to store case information
CREATE TABLE IF NOT EXISTS cases (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  section_id INTEGER NOT NULL REFERENCES sections(id) ON DELETE CASCADE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
-- Note: The 'sections' table must exist before creating this table due to the foreign key constraint.
