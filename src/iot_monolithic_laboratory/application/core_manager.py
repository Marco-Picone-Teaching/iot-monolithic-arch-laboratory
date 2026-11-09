from iot_monolithic_laboratory.application.model.telemetry_model import TelemetryModel
from iot_monolithic_laboratory.data.data_manager import DataManager


class CoreManager:
    """
    Core Manager class that handles the core functionality of the application
    Main methods re-call the data manager methods to decouple the core functionality from the data management
    Additional dedicated methods are used to handle telemetry data from devices with a specific application logic
    """

    def __init__(self, data_manager: DataManager) -> None:
        """Initialize the CoreManager with a Data Manager"""
        self.data_manager = data_manager

    def handle_device_telemetry_data(self, device_id: str, telemetry_data: TelemetryModel) -> None:
        """ Handle telemetry data received from a device """

        # Check that the telemetry data is valid
        if telemetry_data is None or not isinstance(telemetry_data, TelemetryModel):
            raise ValueError("Invalid Telemetry Data")

        self.data_manager.add_device_telemetry_data(device_id, telemetry_data)
        print(f'Telemetry data received from device {device_id}')

    def get_telemetry_data_by_device_id(self, device_id: str) -> list[TelemetryModel] | None:
        """
        Get telemetry data by device id from data manager
        :param device_id: Device id associated with telemetry data
        :return: List of telemetry data
        """
        return self.data_manager.get_telemetry_data_by_device_id(device_id)
