def test_es_1(input_param, get_es_handle):
    query = {
        "query": {
            "match": {
                "skills": "Python"
            }
        }
    }

    response = get_es_handle.search(index="user_data", body=query)
    for hit in response["hits"]["hits"]:
        if hit["_source"] ==input_param.exp_es_data:
            break
    else:
        assert False, f"{input_param.exp_es_data} not present in es"
    

def test_es_2(input_param, get_es_handle):
    query = {
        "query": {
            "match": {
                "skills": "Java"
            }
        }
    }

    response = get_es_handle.search(index="user_data", body=query)
    for hit in response["hits"]["hits"]:
        if hit["_source"] ==input_param.exp_es_data:
            break
    else:
        assert False, f"{input_param.exp_es_data} not present in es"