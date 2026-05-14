#!/usr/bin/env python3

import os
import logging
from logging import handlers

# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("Juliene", log_level)
#ch = logging.StreamHandler() # CONSOLE/TERMINAL/STERR
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=10**6, 
    backupCount=10,
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)s f:%(filename)s: %(message)s'
)
fh.setFormatter(fmt)
log.addHandler(fh)

"""
log.debug("[DEBUG] Mensagem pro dev, qe, sysadmin.")
log.info("[INFO] Mensagem geral para usuários.")
log.warning("[WARNING] Aviso que não causa erro.")
log.error("[ERROR] Erro que afeta uma única execução.")
log.critical("[CRITICAL] Erro crítico")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
