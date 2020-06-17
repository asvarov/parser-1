import hvac

client = hvac.Client(url='http://192.168.10.10:8200', token='s.3F3ksyYxNo5J1iyEohZuADFC')
r = client.is_authenticated()
print(r)
client.secrets.kv.v2.configure(max_versions=20, mount_point='secret',)
client.secrets.kv.v2.create_or_update_secret(path='foo', secret=dict(baz='bar', az='ar'),)

read_response = client.secrets.kv.read_secret_version(path='foo')
print('Value under path "secret/foo" / key "baz": {val}'.format(val=read_response['data']['data']['baz'],))