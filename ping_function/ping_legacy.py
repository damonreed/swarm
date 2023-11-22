import subprocess
import re

# from influxdb import InfluxDBClient 
# influxdb = InfluxDBClient(host='influxdb', port=8086, database='internet')
# def insert_ping(host, latency):
#    influxdb.write_points([{'measurement': "ping", 'tags': {'host': host}, 'fields': {'latency': latency}}])

hosts = [
    "1.1.1.1",
    "8.8.8.8"
]
count = "10"
interval = ".2"

for host in hosts:
    ping_cmd = ['ping','-q','-i',interval,'-c', count,host]
    p = subprocess.Popen(ping_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    output = output.decode("utf-8")
    if p.returncode == 1 and '0 received' in output:
        latency = 0.0
    elif p.returncode == 0 and '1 received' in output:
        latency_pattern = r"rtt .* = ([^\/]+)"
        latency = float(re.findall(latency_pattern, output).pop())
    else:
        print(p.returncode)
        print(output)
        raise NotImplementedError('Unknown state')
    print(host, latency)
    # insert_ping(host, latency)
# time.sleep(ping_interval_seconds)