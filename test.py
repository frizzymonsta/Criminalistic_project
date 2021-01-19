import json

general = 'suricata_alert.json'
events = 'WinEventLog.json'
# update = 'WindowsUpdateLog.json'
# host = 'WinHostMon.json'
# pr = 'WinPrintMon.json'
# reg = 'WinRegistry.json'


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
# update_data = file_to_json(update)
# host_data = file_to_json(host)
# pr_data = file_to_json(pr)
# reg_data = file_to_json(reg)

entries = {}
map_to_entries(entries, general_data, 'g')
map_to_entries(entries, events_data, 'e')
# map_to_entries(entries, update_data, 'u')
# map_to_entries(entries, host_data, 'h')
# map_to_entries(entries, pr_data, 'p')
# map_to_entries(entries, reg_data, 'r')

collision = []

for entry in entries:
    item = entries[entry]

    count = 0

    if 'g' in item:
        count = count + 1

    # if 'e' in item:
    #     count = count + 1
    #
    # if 'u' in item:
    #     count = count + 1
    #
    # if 'h' in item:
    #     count = count + 1
    #
    # if 'p' in item:
    #     count = count + 1
    #
    # if 'r' in item:
    #     count = count + 1

    if count >= 1:
        collision.append(item)

with open('output.json', 'w') as out_file:
    out_file.write(json.dumps(collision, indent=2))