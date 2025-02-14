import json

with open("a.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 80)

for i in data["imdata"]:
    attributes = i["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "")  
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}")