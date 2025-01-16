import anthropic
import base64

with open("Planwerk JF 28.pdf", "rb") as f:
    pdf_bytes = f.read()
    pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=8192,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Please parse all the data from the PDF to JSON. Make sure to differentiate between the subheadings. Do not include other text, so I can just write your response to a file. Make sure you include every row."
            },
            {
                "type": "document",
                "source": {
                    "type": "base64",
                    "media_type": "application/pdf",
                    "data": pdf_base64
                }
            }
        ]
    }]
)

print(message.content[0].text)

with open("result", "w") as f:
    f.write(message.content[0].text)
