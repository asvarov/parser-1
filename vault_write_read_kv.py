import hvac


client = hvac.Client(url='http://192.168.10.10:8200', token='s.3F3ksyYxNo5J1iyEohZuADFC')
r = client.is_authenticated()
print(r)
print(client.sys.is_sealed())
#
# client.secrets.kv.v2.configure(max_versions=20, mount_point='secret',)
# client.secrets.kv.v2.create_or_update_secret(path='pythonapp', secret=dict(login='username', password='userpassword'),)
#
# read_response = client.secrets.kv.read_secret_version(path='pythonapp')
# login = read_response['data']['data']['login']
# password = read_response['data']['data']['password']
# print(f'Value under path "secret/pythonapp" / key "login": {login}')
# print(f'Value under path "secret/pythonapp" / key "password": {password}')
#
# list_response = client.secrets.kv.v2.list_secrets(
#     path='pythonapp/login',
# )
#
# print('The following paths are available under "hvac" prefix: {keys}'.format(
#     keys=','.join(list_response['data']['keys']),
# ))