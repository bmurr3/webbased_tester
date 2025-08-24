-- db/status.sql

-- Table to store status information
CREATE TABLE IF NOT EXISTS statuses (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  importance_level INTEGER NOT NULL DEFAULT -1
);
-- Note: This table does not have foreign key constraints, so it can be created independently.

-- In case the statuses table is pre-existing, we clear it to avoid duplicates.
DELETE FROM statuses;

INSERT INTO statuses (name, description) VALUES
( 'Untested', 'This test case has not been tested yet.'),
( 'Passed', 'This test case has been executed and passed successfully.'),
( 'Failed', 'This test case has been executed and failed.'),
( 'Blocked', 'This test case cannot be executed due to external dependencies or issues.'),
( 'Retest', 'This test case needs to be re-executed due to changes or fixes.'),
( 'Not Applicable', 'This test case is not applicable in the current context.'),
( 'Excluded', 'This test case is excluded from the current testing cycle.');

UPDATE statuses
SET importance_level = CASE name
    WHEN 'Untested' THEN 0
    WHEN 'Passed' THEN 1
    WHEN 'Blocked' THEN 2
    WHEN 'Retest' THEN 3
    WHEN 'Failed' THEN 4
    ELSE -1
END;
-- Note: The importance_level is set based on the typical significance of each status in a testing workflow.
-- 'Untested' is the least important as it indicates no action has been taken.
-- 'Passed' is next as it indicates success.
-- 'Blocked' follows since it requires attention to resolve dependencies.
-- 'Retest' is more important as it indicates that action has been taken but needs verification.
-- 'Failed' is the most important as it indicates a problem that needs to be addressed.
