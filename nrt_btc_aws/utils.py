from datetime import datetime


def get_ingest_date():
    """Capture date and time for quote ingestion.
    Local time is the reference"""
    ingest_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return ingest_date
