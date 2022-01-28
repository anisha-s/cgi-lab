#!/usr/bin/env python3

import os, json

# print out all environment variables as plain text
print("Content-Type: text/plain")
print()
print("os.environ")

# print out all environment variables as json
#print("Content-Type: application/json")
#print()
#print(json.dumps(dict(os.environ), indent=2))

# print out query parameter data as plain text
#print("Content-Type: text/html")
#print()
#print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")
