import json

general = 'suricata_alert.json'
events = 'WinEventLog.json'


def file_to_json(file_name):
    with open(file_name, 'r') as file:
        return json.loads(file.read())


def map_to_entries(output, json, sublist_name):
    for item in json:
        time = item['_time']

        if time not in output:
            output[time] = {}

        if sublist_name not in output[time]:
            output[time][sublist_name] = []

        output[time][sublist_name].append(item)


general_data = file_to_json(general)
events_data = file_to_json(events)

entries = {}
map_to_entries(entries, general_data, 'g')
map_to_entries(entries, events_data, 'e')

collision = []

for entry in entries:
    item = entries[entry]

    if 'g' in item and 'e' in item:
        collision.append(item)

with open('output.json', 'w') as out_file:
    out_file.write(json.dumps(collision, indent=2))