import fitz

fname = "Planwerk JF 28.pdf"
doc = fitz.open(fname)

result = []
for i, page in enumerate(doc):
    tabs = page.find_tables()
    print(f"Page {i+1} has {len(tabs.tables)} tables")
    tab = tabs[0]
    result.append(tab.extract())

print(result)
