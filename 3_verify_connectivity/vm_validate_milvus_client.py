import os
import time
import json
import cmlapi
from milvus import default_server
from pymilvus import connections, utility

try:
    port=str(os.environ.get('CDSW_APP_PORT', 8100))
    CDSW_DOMAIN = os.environ.get("CDSW_DOMAIN",'undefined')
    CDSW_APIV2_KEY = os.environ.get("CDSW_APIV2_KEY",'undefined')
    CDSW_PROJECT_ID = os.environ.get("CDSW_PROJECT_ID",'undefined')
    WORKSPACE_DOMAIN = f"https://{CDSW_DOMAIN}"
    cml_client = cmlapi.default_client(WORKSPACE_DOMAIN, CDSW_APIV2_KEY)
    app_list = cml_client.list_applications(CDSW_PROJECT_ID, search_filter=json.dumps({"name": "MilvusDB Server"}))
    app_subdomain = app_list.applications[0].subdomain
    app_id = app_list.applications[0].id
    cml_client.update_application({"bypass_authentication": True}, CDSW_PROJECT_ID, app_id)
    #cml_client.restart_application({"bypass_authentication": True}, CDSW_PROJECT_ID, app_id)
    time.sleep(30)
    app_endpoint=f"https://{app_subdomain}.{CDSW_DOMAIN}"
    with open('/home/cdsw/milvusdb.fqdn', 'w') as f:
        f.write(app_endpoint)
    if os.environ.get('MILVUS_AUTH', 'false').lower() == 'true':
        user = os.environ.get('MILVUS_USER', 'admin')
        password = os.environ.get('MILVUS_PASSWORD', 'admin')
        print(f"u:{user}, p:{password}, h:{app_endpoint}")
        client = milvus_client.MilvusClient(host=app_endpoint, port=port, user=user, password=password)
    else:
        client = milvus_client.MilvusClient(host=app_endpoint, port=port)
except Exception as e:
    print(f"Exception client connectivity: {str(e)}")

try:
    print(client.list_users())
    print(client.list_collections())
except Exception as e:
    print(f"Connectivity error: {str(e)}")
