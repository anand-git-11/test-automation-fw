def test_db_1(input_param, get_db_handle):
    cursor = get_db_handle.cursor()
    select_query = "SELECT * FROM users"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    for row in rows:
        if row == input_param.exp_db_data:
            break
    else:
        assert False, f"{input_param.exp_data} not present in db"

def test_db_2(input_param, get_db_handle):
    cursor = get_db_handle.cursor()
    select_query = "SELECT * FROM apps"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    for row in rows:
        if row == input_param.exp_data:
            break
    else:
        assert False, f"{input_param.exp_db_data} not present in db"
