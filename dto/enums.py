from enum import Enum


class StatusEnum(str, Enum):
    finish = 'FINISH'
    task_done = 'TASK_DONE'
    error = 'ERROR'
    pending = 'PENDING'


class FinishReasonEnum(str, Enum):
    finish = 'message_done'
    server_error = 'third_party_error'
    internal_error = 'internal_error'
