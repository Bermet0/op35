
class SuperHero:
    people = 'people'

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


Hero = SuperHero('Tony', 'IronMan', 'Smart',
               100, 'Я Железный человек')

print(f'Hero name is: {Hero.name}')
Hero.double_health()
print(Hero)
print(f'Lencht catchphrase: {len(Hero)}')

