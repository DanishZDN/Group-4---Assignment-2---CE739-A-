from network_comm_lib import NetworkCommLib

def monitored():
    node = NetworkCommLib(broker="localhost", port=1883, node_id="monitored")
    node.connect()

    def on_ping_received(client, userdata, message):
        print("Ping received. Sending ACK...")
        node.send_unicast(target_id="detector", message="ack")
    
    node.subscribe(f'unicast/{node.node_id}', on_ping_received)

    while True:
        pass  # Simulate running state

if __name__ == "__main__":
    monitored()
