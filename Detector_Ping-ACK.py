from network_comm_lib import NetworkCommLib

import time

def detector():
    node = NetworkCommLib(broker="localhost", port=1883, node_id="detector")
    node.connect()
    target_id = "monitored"
    
    def on_ack_received(client, userdata, message):
        print("ACK received from monitored process.")
    
    node.subscribe(f'unicast/{node.node_id}/ack', on_ack_received)
    
    while True:
        print("Sending ping...")
        node.send_unicast(target_id=target_id, message="ping")
        time.sleep(2)  # Waits for ACK
        # Check if ACK is received, else declare fail
        print("No ACK received. Declaring fail...")
        break
    
if __name__ == "__main__":
    detector()
