from bottle import route,run

@route('/analytics/query', method = 'POST')
def dummy_query_reponse():
    data = [  {
                "UuidKey": "f86f1b1b-aa44-46aa-a460-85af8518d00a",
                "action": "pass",
                "agg-packets": 5,
                "destip": "10.1.1.224",
                "destvn": "default-domain:admin:ext_04",
                "dport": 10050,
                "protocol": 6,
                "setup_time": 1462264499141705,
                "sourceip": "10.1.1.232",
                "sourcevn": "default-domain:admin:ext_04",
                "sport": 55567,
                "teardown_time": 'null',
                "vrouter": "node-28" },
              {
                "UuidKey": "a86f1b1b-aa44-46aa-a460-85af8511d00a",
                "action": "pass",
                "agg-packets": 5,
                "destip": "10.1.1.212",
                "destvn": "default-domain:admin:ext_04",
                "dport": 22,
                "protocol": 6,
                "setup_time": 1462264499141105,
                "sourceip": "10.1.1.215",
                "sourcevn": "default-domain:admin:ext_04",
                "sport": 55161,
                "teardown_time": 'null',
                "vrouter": "node-29"  }  
            ]
         
    return dict(value=data)

run (host='0.0.0.0', port=8081, debug=True, reloader=True) 
   
