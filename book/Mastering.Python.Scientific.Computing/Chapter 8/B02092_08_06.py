from IPython import parallel
from datetime import datetime, timedelta
clients = parallel.Client(profile=’testprofile’)
incomplete_task = clients.db_query({’complete’ : None}, keys=[’msg_id’, ’started’])
one_hourago = datetime.now() - timedelta(1./24)
tasks_started_hourago = clients.db_query({’started’ : {’$gte’ : one_hourago },’client_uuid’ : clients.session.session})
tasks_started_hourago_other_client = clients.db_query({’started’ : {’$le’ : hourago }, ’client_uuid’ : {’$ne’ : clients.session.session}})
uuids_of_3_n_4 = map(clients._engines.get, (3,4))
headers_of_3_n_4 = clients.db_query({’engine_uuid’ : {’$in’ : uuids_of_3_n_4 }}, keys=’result_header’)