def log_nfc_event(tag_id, status):
    # Mock NFC handling
    print(f"NFC Tag {tag_id} {status}")
    return {"tag_id": tag_id, "status": status, "timestamp": "now"}
