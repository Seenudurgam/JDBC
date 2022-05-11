import adal

resource_app_id_url = "https://database.windows.net/"

service_principal_id = dbutils.secrets.get(scope = "defaultScope", key = "DatabricksSpnId")
service_principal_secret = dbutils.secrets.get(scope = "defaultScope", key = "DatabricksSpnSecret")
tenant_id = dbutils.secrets.get(scope = "defaultScope", key = "TenantId")
authority = "https://login.windows.net/" + tenant_id


azure_sql_url = "jdbc:sqlserver://thedataswamp.database.windows.net"
database_name = "dev"
db_table = "dbo.Emperor" 


encrypt = "true"
host_name_in_certificate = "*.database.windows.net"

context = adal.AuthenticationContext(authority)
token = context.acquire_token_with_client_credentials(resource_app_id_url, service_principal_id, service_principal_secret)
access_token = token["accessToken"]

emperorDf = spark.read \
             .format("com.microsoft.sqlserver.jdbc.spark") \
             .option("url", azure_sql_url) \
             .option("dbtable", db_table) \
             .option("databaseName", database_name) \
             .option("accessToken", access_token) \
             .option("encrypt", "true") \
             .option("hostNameInCertificate", "*.database.windows.net") \
             .load()
             
display(emperorDf)             