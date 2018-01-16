from abc import abstractmethod

class Camel(object):

    def __init__(self, id):
        self.__id = id
        # self.__position = -1
        self.__distance = 0

    def move(self, distance):
        self.set_distance(self.get_distance() + distance)
        print("Camel %i moved %f meters" % (self.get_id(), distance))

    @abstractmethod
    def turbo_boost(self): pass

    @abstractmethod
    def weapon(self): pass

    @abstractmethod
    def strength(self): pass

    def get_id(self):
        return self.__id

    def get_distance(self):
        return self.__distance

    def set_distance(self, distance):
        self.__distance = distance

    # def get_position(self):
    #     return self.__position
    #
    # def set_position(self, position):
    #     self.__position = position


class BactrianCamel(Camel):

    default_boost = 0.15
    mud_boost = 0.3

    def use_turbo_boost(self, distance, terrain):
        if terrain == 'Mud':
            print('Bactrian Camel %i is now moving 30% faster' % self.get_id())
            return self.default_boost
        else:
            print('Bactrian Camel %i is now moving 15% faster' % self.get_id())
            return self.mud_boost

    def use_weapon(self, camel, steps):
        camel.move(camel.use_strength(-steps))

    def use_strength(self, steps):
        return steps * 0.8


class DomesticCamel(Camel):

    default_boost = 0.15
    mud_boost = 0.3

    def use_turbo_boost(self, distance, terrain):
        if terrain == 'Mud':
            print('Bactrian Camel %i is now moving 30% faster' % self.get_id())
            return self.default_boost
        else:
            print('Bactrian Camel %i is now moving 15% faster' % self.get_id())
            return self.mud_boost

    def use_weapon(self, camel, steps):
        camel.move(camel.use_strength(-steps))

    def use_strength(self, steps):
        return steps * 0.8


class Dromedary(Camel):

    default_boost = 0.15
    mud_boost = 0.3

    def use_turbo_boost(self, distance, terrain):
        if terrain == 'Mud':
            print('Bactrian Camel %i is now moving 30% faster' % self.get_id())
            return self.default_boost
        else:
            print('Bactrian Camel %i is now moving 15% faster' % self.get_id())
            return self.mud_boost

    def use_weapon(self, camel, steps):
        camel.move(camel.use_strength(-steps))

    def use_strength(self, steps):
        return steps * 0.8


class CamelFactory(object):
    @staticmethod
    def get_camel(type, i):
        if type == 'BactrianCamel':
            return BactrianCamel(i)
        if type == 'DomesticCamel':
            return DomesticCamel(i)
        if type == 'Dromedary':
            return Dromedary(i)
        assert 0, 'There is no such type of camel'