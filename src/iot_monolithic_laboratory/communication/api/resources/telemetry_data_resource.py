from typing import Any

from flask_restful import Resource

from iot_monolithic_laboratory.application.core_manager import CoreManager


class TelemetryDataResource(Resource):
    """Resource to handle the Telemetry Data of a specific Device"""

    def __init__(self, **kwargs: Any) -> None:
        # Inject the CoreManager instance
        self.core_manager: CoreManager = kwargs['core_manager']

    def get(self, device_id: str) -> Any:
        """GET Request to retrieve the Telemetry Data of a target device"""

        device_telemetry_data = self.core_manager.get_telemetry_data_by_device_id(device_id)

        if device_telemetry_data is None:
            return {'error': "Device Not Found !"}, 404

        # Build a serializable list transforming each telemetry data into a dictionary:
        # Flask-RESTful then serializes it into JSON
        telemetry_data_list = [telemetry_data.__dict__ for telemetry_data in device_telemetry_data]

        return telemetry_data_list, 200
