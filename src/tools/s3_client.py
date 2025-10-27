def safe_put_object(bucket, key, data: bytes):
    # stub; prints instead of writing
    return {"bucket": bucket, "key": key, "bytes": len(data), "status": "dry-run"}
