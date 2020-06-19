import hvac

client = hvac.Client(url='http://192.168.10.10:8200')
client.sys.is_initialized()
# False

shares = 5
threshold = 3

result = client.sys.initialize(shares, threshold)
root_token = result['root_token']
print('root token: ', root_token)
with open('root_token_vault.json', mode='w') as f:
    f.write(root_token)

keys = result['keys']
for i in keys:
    with open(f'individual_key_{keys.index(i)+1}_vault.json', mode='w') as f:
        f.write(i)
client.sys.is_initialized()
# True

client.token = root_token

print('Storage is sealed?: ', client.sys.is_sealed()) # True

# unseal with individual keys
print('individual key #1: ', (keys[0]))
print('individual key #2: ', (keys[1]))
print('individual key #3: ', (keys[2]))
print('individual key #4: ', (keys[3]))
print('individual key #5: ', (keys[4]))

# Unseal a Vault cluster with individual keys
unseal_response1 = client.sys.submit_unseal_key(keys[0])
unseal_response2 = client.sys.submit_unseal_key(keys[1])
unseal_response3 = client.sys.submit_unseal_key(keys[2])

client.sys.seal()
# <Response [204]>

# Unseal with multiple keys until threshold met
unseal_response = client.sys.submit_unseal_keys(keys)

print('Storage is sealed?: ', client.sys.is_sealed())
# False
