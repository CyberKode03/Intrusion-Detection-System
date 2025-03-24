from datetime import datetime
from db_connect import insert_alert

insert_alert(
    timestamp=datetime.now(),
    src_ip="192.168.1.100",
    dest_ip="192.168.1.1",
    message="⚠️ Suspicious activity detected"
)
