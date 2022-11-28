from logging import Logger


class ErrorProcessorMixin:
    logger: Logger

    def _process_error_response(self, exception: Exception, url, inst_id: str):
        self.logger.error(exception(url=url, inst_id=inst_id))
        raise exception(url=url, inst_id=inst_id)
