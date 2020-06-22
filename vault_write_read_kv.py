import hvac

with open('root_token_vault.json', mode='r') as f:
    root_token = f.read()

client = hvac.Client(url='http://192.168.10.10:8200', token=root_token)
r = client.is_authenticated()
print(f'Client is authenticated: {r}')

secrets_engines_list = client.sys.list_mounted_secrets_engines()['data']

try:
    client.sys.enable_secrets_engine(
        backend_type='kv',
        path='hvac-kv',
    )
except hvac.exceptions.InvalidRequest as error:
    print(f'Creation {error} - skipped.')

print(secrets_engines_list.keys())
print('The following secrets engines are mounted: %s' % ', '.join(sorted(secrets_engines_list.keys())))


# client.secrets.kv.v2.configure(max_versions=20, mount_point='secret',)
# client.secrets.kv.v2.create_or_update_secret(path='pythonapp', secret=dict(login='username', password='userpassword'),)
#
# read_response = client.secrets.kv.read_secret_version(path='pythonapp')
# login = read_response['data']['data']['login']
# password = read_response['data']['data']['password']
# print(f'Value under path "secret/pythonapp" / key "login": {login}')
# print(f'Value under path "secret/pythonapp" / key "password": {password}')

# list_response = client.secrets.kv.v2.list_secrets(
#     path='pythonapp/login',
# )
#
# print('The following paths are available under "hvac" prefix: {keys}'.format(
#     keys=','.join(list_response['data']['keys']),
# ))