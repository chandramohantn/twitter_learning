from extractor.whatsapp_parser import parse_whatsapp_export
from extractor.deduplicator import filter_new_urls

urls = parse_whatsapp_export("chat.txt")

new_urls = filter_new_urls(urls)

print("New tweets found:")

for u in new_urls:
    print(u)