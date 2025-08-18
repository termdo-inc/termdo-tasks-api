GET_TASKS_1AID = """SELECT * FROM task WHERE account_id = $1"""

GET_TASK_1AID_2TID = (
    """SELECT * FROM task WHERE account_id = $1 AND task_id = $2"""
)

INSERT_TASK_RT_1AID_2TITLE_3DESC = """
    INSERT INTO task (account_id, title, description)
    VALUES ($1, $2, $3)
    RETURNING *
"""

UPDATE_TASK_RT_1AID_2TID_3TITLE_4DESC_5ISCMP = """
    UPDATE task
    SET title = $3, description = $4, is_completed = $5, updated_at = NOW()
    WHERE account_id = $1 AND task_id = $2
    RETURNING *
"""

DELETE_TASK_1AID_2TID = (
    """DELETE FROM task WHERE account_id = $1 AND task_id = $2"""
)
