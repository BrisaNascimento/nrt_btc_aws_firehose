import time

from nrt_btc_aws.scraper import Quote
from nrt_btc_aws.sender import send_to_firehose
from nrt_btc_aws.utils import get_ingest_date


def ingest_data(
    currency: str, exchange: str, max_ingestions: int, time_delay: int
):
    """
    Ingests data collected from webpage to firehose/S3 resource group.
    The data ingestion is limited a set of collections configured
    as parameter max_ingestions and time delay for ingestion.


    Arguments
    ---------
    currency: str, acronym used in website source for the currency quotation,
        for example BTC for Bitcoin, ETH for Ethereum.

    exchange: str, acronym used in website source for the exchange quotation,
        for example, BRL for Brazilian Real, USD for American Dolar,
        EUR for Euro.

    max_ingestions: int, total of data collections ingestions intended.

    time_delay: optional, default is 1 second. Delay for capture data
    from source in seconds.
    """
    n_ingestions = 0
    while n_ingestions < max_ingestions:
        # Capture current quote for ingestion
        quote = Quote()
        current_price = quote.get_current_quote(currency, exchange)
        # Capture date and time for quote ingestion
        ing_date = get_ingest_date()
        # Upload data to AWS Firehose, later S3
        stream_name = 'fh-brisa-general'
        send_to_firehose(stream_name, current_price, ing_date)
        n_ingestions += 1
        print(current_price, ing_date)
        time.sleep(time_delay)
    print('Ingestion sucessful!')
    return True
