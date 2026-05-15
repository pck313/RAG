from openai import OpenAI

client = OpenAI(
    api_key="sk-7v01joFHtMTQaMHtT0usLw",
    base_url="https://ai.dxhub.com.vn/v1"
)

models = client.models.list()

for m in models.data:
    print(m.id)