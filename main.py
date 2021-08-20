# Load dependencies
import json

# Load data
print("Loading data...")
with open('report.ndjson', 'r') as myfile:
  data = myfile.read().split('\n')
apps = {}
types = {}
print("Processing data...")
for entry in data:
  if 'accessor' in entry:
    entry = json.loads(entry)
    #print(entry)
    name = entry["accessor"]["identifier"]
    name = name.split(".")
    name.reverse()
    domain = name[0] + " - "
    del name[0]
    for i in name:
      domain += i + "."
    name = domain[:-1]
    category = entry["category"]
    if name in apps:
      apps[name]["total"] = apps[name]["total"] + 1
      if category in apps[name]["types"]:
        apps[name]["types"][category] += 1
      else:
        apps[name]["types"][category] = 1
    else:
      apps[name] = {
        "total":1,
        "types":{
          category:1
        }
      }
    if category in types:
      types[category] += 1
    else:
      types[category] = 1
#apps = dict(sorted(apps.items(), key=lambda x: x[1], reverse=True))
types = dict(sorted(types.items(), key=lambda x: x[1], reverse=True))
#print("Saving names to file...")
output = {
  "apps":apps,
  "categories":types
}
with open('output.json', 'w+') as file:
  json.dump(output, file, indent=2)
print("\nDone! Sorted list of apps. There were " + str(len(apps)) + " individual apps out of the total " + str(len(data)) + " data entrys.")
print("Check output.json for a more detailed report.")