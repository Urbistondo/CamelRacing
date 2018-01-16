class Race(object):

    def __init__(self, camels, terrain, total_distance, step_distance):
        self.camels = camels
        self.terrain = terrain
        self.total_distance = total_distance
        self.step_distance = step_distance

    def get_camels(self):
        return self.camels

    def set_camels(self, camels):
        self.camels = camels

    def get_terrain(self):
        return self.terrain

    def set_terrain(self, terrain):
        self.terrain = terrain

    def get_total_distance(self):
        return self.total_distance

    def set_total_distance(self, total_distance):
        self.total_distance = total_distance

    def get_step_distance(self):
        return self.step_distance

    def set_step_distance(self, step_distance):
        self.step_distance = step_distance

    def update_positions(self):
        self.camels.sort(key=lambda camel: camel.get_distance(), reverse=True)

    def is_finished(self):
        return self.camels[0].get_distance() >= self.total_distance
