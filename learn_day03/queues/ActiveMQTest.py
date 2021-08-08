import stomp

host =  "localhost"
port = 61613
message = "This is Test Message "
dest_queue = "/queue/TEST.KK.WEEKEND.AUGUST"

conn = stomp.Connection(host_and_ports = [(host, port)])
conn.connect()

for i in range(1, 10):
    conn.send(destination=dest_queue, body=message+str(i), persistent='true')

conn.disconnect()