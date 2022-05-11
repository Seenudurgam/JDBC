import adal

resource_app_id_url = "https://database.windows.net"

service_principal_id = "a494ca25-7abf-4482-a906-355c62361291"
service_principal_secret = "Y3kjWzSdGxRdLadgxt7WZuv7_fd0vQm-jH"
tenant_id = "c62b5b8d-4235-4aed-8119-c6716db47e1c"
authority = "https://login.windows.net/" + tenant_id


azure_sql_url = "jdbc:sqlserver://sql-weu-uc-sree54-test-01.database.windows.net"
database_name = "sqldb-weu-uc-sree54-test-01"
db_table = "dbo.JDBC" 


encrypt = "true"
host_name_in_certificate = "*.database.windows.net"

context = adal.AuthenticationContext(authority)
token = context.acquire_token_with_client_credentials(resource_app_id_url, service_principal_id, service_principal_secret)
access_token = token["accessToken"]
print (access_token)
tokenb = bytes(token["accessToken"], "UTF-8")

exptoken = b''
for i in tokenb:
    exptoken += bytes({i})
    exptoken += bytes(1)
tokenstruct = struct.pack("=i", len(exptoken)) + exptoken
tokenstruct

SQL_COPT_SS_ACCESS_TOKEN = 1256
CONNSTRING = "DRIVER={};SERVER={};DATABASE={}".format("ODBC Driver 17 for SQL Server", SERVER, DATABASE)

conn = pyodbc.connect(CONNSTRING, attrs_before = { SQL_COPT_SS_ACCESS_TOKEN:tokenstruct })
cursor = conn.cursor()
cursor.execute("SELECT 1")



          