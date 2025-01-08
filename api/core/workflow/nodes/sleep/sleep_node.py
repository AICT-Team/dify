import logging

from core.workflow.entities.node_entities import NodeRunResult
from core.workflow.nodes.base import BaseNode
from core.workflow.nodes.enums import NodeType
from core.workflow.nodes.sleep.entities import SleepNodeData
from models.workflow import WorkflowNodeExecutionStatus
import time

logger = logging.getLogger(__name__)

class SleepNode(BaseNode[SleepNodeData]):
    _node_data_cls = SleepNodeData
    _node_type = NodeType.SLEEP

    def _run(self) -> NodeRunResult:
        sleep_time_ms = self.node_data.sleep_time_ms
        time.sleep(sleep_time_ms / 1000.0)  # Convert milliseconds to seconds
        return NodeRunResult(status=WorkflowNodeExecutionStatus.SUCCEEDED)