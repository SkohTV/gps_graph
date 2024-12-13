import json
import logging
import logging.config
import os
from typing import override
import datetime as dt

from src.args import arguments



logger = logging.getLogger(__name__)



def setup_logging() -> None:
  '''Init the logger with correct params'''

  filename = 'verbose.json' if arguments.verbose else 'normal.json'
  config_file = os.path.join(os.getcwd(), 'src', 'logging', filename)
  with open(config_file) as f:
    config = json.load(f)

  logging.config.dictConfig(config)



LOG_RECORD_BUILTIN_ATTRS = {
  "args",
  "asctime",
  "created",
  "exc_info",
  "exc_text",
  "filename",
  "funcName",
  "levelname",
  "levelno",
  "lineno",
  "module",
  "msecs",
  "message",
  "msg",
  "name",
  "pathname",
  "process",
  "processName",
  "relativeCreated",
  "stack_info",
  "thread",
  "threadName",
  "taskName",
}



class JSONFormatter(logging.Formatter):
  '''
  Custom formatter for logging to print in .cache/logs/log.jsonl
  Stolen from here
  https://github.com/mCodingLLC/VideosSampleCode/blob/master/videos/135_modern_logging/mylogger.py
  '''

  def __init__(self, *, fmt_keys: dict[str, str] | None = None):
      super().__init__()
      self.fmt_keys = fmt_keys if fmt_keys is not None else {}


  @override
  def format(self, record: logging.LogRecord) -> str:
    '''Format a string to log into proper json'''
    message = self._prepare_log_dict(record)
    return json.dumps(message, default=str)


  def _prepare_log_dict(self, record: logging.LogRecord):
    '''Done BEFORE the json conversion'''

    always_fields = {
      "message": record.getMessage(),
      "timestamp": dt.datetime.fromtimestamp(
        record.created, tz=dt.timezone.utc
      ).isoformat(),
    }

    if record.exc_info is not None:
      always_fields["exc_info"] = self.formatException(record.exc_info)

    if record.stack_info is not None:
      always_fields["stack_info"] = self.formatStack(record.stack_info)

    message = {
      key: msg_val
      if (msg_val := always_fields.pop(val, None)) is not None
      else getattr(record, val)
      for key, val in self.fmt_keys.items()
    }
    message.update(always_fields)

    for key, val in record.__dict__.items():
      if key not in LOG_RECORD_BUILTIN_ATTRS:
        message[key] = val

    return message

