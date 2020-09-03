import os
import logging
from findpapers.utils.outputfile_util import save, load
from findpapers.utils.search_util import run, _get_paper_metadata_by_url
from findpapers.utils.refinement_util import refine
from findpapers.utils.download_util import download


logging_level = os.getenv('LOGGING_LEVEL')
if logging_level is None:  # pragma: no cover
    logging_level = 'INFO'

logging.basicConfig(level=getattr(logging, logging_level),
                    format='%(asctime)s %(levelname)s: %(message)s')
