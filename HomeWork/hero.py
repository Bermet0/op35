
class SuperHero:
    people = 'people'
    fly = False

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def hero_name(self):
        print(f'Name is: {self.name}')

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return (f' nickname is: {self.nickname}\n'
                f' superpower is: {self.superpower}\n'
                f' health_point is: {self.health_points}')

    def __len__(self):
        return len(self.catchphrase)

    def true_fly(self):
        print(f'True in the {self.true_fly}')

Hero = SuperHero('Tony', 'IronMan', 'Smart',
               100, 'Я Железный человек')

print(f'Hero name is: {Hero.name}')
Hero.double_health()
print(Hero)
print(f'Lencht catchphrase: {len(Hero)}')


class HeroA(SuperHero):
    fly = True

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=True):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def double_health(self):
        self.health_points **= 2

    def catchphrase(self):
        super().catchphrase('True in the True_phrase')


class HeroE(SuperHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=True):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def double_health(self):
        self.health_points **= 2

    def catchphrase(self):
        super().catchphrase('True in the True_phrase')


class Villian(HeroE):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.people = 'monster'

    def gen_x(self):
        pass

    def crit(self, hp):
        hp.damage = hp.damage ** 2


air = HeroA('Aang', 'Быстрые ноги', 'Avatar', 112,
            'Ип-ип!', 25, False)
earth = HeroE('Tof', 'Слепой бандит', 'Earth', 100,
              'Я-великий маг земли', 20, False)
villian = Villian('Ozai', 'Phenix', 'Fire', 45,
                  'Kill the Avatar', 20)


air.double_health()
earth.double_health()

print(f'Hero name is: {air.name}')
print(air)
print(f'Hero name is: {earth.name}')
print(earth)

villian.crit(air)
print(f'Air damage after crit {air.damage}')

