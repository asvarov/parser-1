import hvac

client = hvac.Client(url='http://192.168.10.10:8200')
client.sys.is_initialized()
# False
if client.sys.is_sealed() is True and client.sys.is_initialized() is False:
    shares = 5
    threshold = 3

    result = client.sys.initialize(shares, threshold)
    root_token = result['root_token']
    print(f'root token: {root_token}')
    with open('root_token_vault.json', mode='w') as f:
        f.write(root_token)

    keys = result['keys']
    for i in keys:
        with open(f'individual_key_{keys.index(i)+1}_vault.json', mode='w') as f:
            f.write(i)
    client.sys.is_initialized()
    # True
    client.token = root_token

    print(f'Storage is sealed?: {client.sys.is_sealed()}') # True
    # unseal with individual keys
    for i in keys:
        print(f'individual key #{keys.index(i)+1}: {keys[keys.index(i)]}')

    for i in range(threshold):
        # Unseal a Vault cluster with individual keys
        unseal_response = client.sys.submit_unseal_key(keys[i])

    client.sys.seal()
    # <Response [204]>
    # Unseal with multiple keys until threshold met
    unseal_response = client.sys.submit_unseal_keys(keys)
    print(f'Storage is sealed?: {client.sys.is_sealed()}')
    # False
else:
    print(f'Storage is unsealed and client is_initialized!')

