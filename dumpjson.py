import json

from rules import RULES

print(json.dumps(RULES, indent=4))

with open('rules.json', 'w') as rules_json:
    json.dump(RULES, rules_json, indent=4)
