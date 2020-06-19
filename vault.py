import hvac
#
# client = hvac.Client(url='http://192.168.10.10:8200', token='s.3F3ksyYxNo5J1iyEohZuADFC')
# r = client.is_authenticated()
# print(r)
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


client = hvac.Client(url='http://192.168.10.10:8200')
print(client.sys.is_initialized()) # => False

shares = 5
threshold = 3

result = client.sys.initialize(shares, threshold)
print(result)
root_token = result['root_token']
print(root_token)
keys = result['keys']
print(keys)

print(client.sys.is_initialized()) # => True

client.token = root_token

print(client.sys.is_sealed()) # => True

# unseal with individual keys
print((keys[0]))
print((keys[1]))
print((keys[2]))

# Unseal a Vault cluster with individual keys
unseal_response1 = client.sys.submit_unseal_key(keys[0])
unseal_response2 = client.sys.submit_unseal_key(keys[1])
unseal_response3 = client.sys.submit_unseal_key(keys[2])
print(client.sys.is_sealed())

print(client.sys.seal()) # <Response [204]>
print(client.sys.is_sealed()) # True

# Unseal with multiple keys until threshold met
unseal_response = client.sys.submit_unseal_keys(keys)

client.sys.is_sealed() #False