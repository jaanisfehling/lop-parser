# lop-parser
Construction Project List of Open Points (LOP) Parser

I tried using a traditional PDF parsing library, in my case I chose `pyMuPDF`, which seems to be a widely used python library for content extraction in PDF documents.
First I just tried to extract all textual content from the PDF. Because of some missing data in some rows of the PDF, its almost impossible to structurally parse such text content.
Next, I tried the table extraction feature from `pyMuPDF`. This did not work out at all.

Then, I moved to the LLM approach using Claude. Here I read the PDF file as bytes and encode it with Base64 and then append it to the messages. Then, I ask the LLM to parse all data as JSON, emphasizing to not output any other text in the reponse such that I can directly save the response to a text file. It is also important to emphasize to include all data. 

I am using JSON as a output format, since the PDF contains subheadings. If they were not there, I would choose CSV, but a JSON file can contain multiple datasets from the different subheadings.
