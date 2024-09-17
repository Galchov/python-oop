"""
Now the code has been refactored so the appliances are not dependent on a single class and
its functionality, which obviously does not apply to all of them.

New classes for each functionality has been created so each appliance can inherit what they really need.
Reminds us of the Single-Responsibility Principle, doesn't it...

Interface Segregation Principle -> Clients (classes and subclasses) should not be forced to
depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies.
"""


# class EntertainmentDevice:
#     def connect_to_device_via_hdmi_cable(self, device): pass
#     def connect_to_device_via_rca_cable(self, device): pass
#     def connect_to_device_via_ethernet_cable(self, device): pass
#     def connect_device_to_power_outlet(self, device): pass


class HDMIConnector:
    def connect_to_device_via_hdmi_cable(self, device): pass


class RCAConnector:
    def connect_to_device_via_rca_cable(self, device): pass


class EthernetConnector:
    def connect_to_device_via_ethernet_cable(self, device): pass


class PowerConnector:
    def connect_device_to_power_outlet(self, device): pass


class Television(RCAConnector, HDMIConnector, PowerConnector):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(HDMIConnector, PowerConnector):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(HDMIConnector, EthernetConnector, PowerConnector):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EthernetConnector, PowerConnector):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
