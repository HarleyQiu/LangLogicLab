from redis import Redis
import json

redis_client = Redis(host='localhost', port=6379, decode_responses=True)

key = 'f7538db6-251b-4848-8a0f-2a9baff1f07b'

value = redis_client.lrange(key, 0, -1)
combined_content = ""
for item in value:
    item_json = json.loads(item)
    content = item_json.get('content', '')
    combined_content += content + " "

print(combined_content)
