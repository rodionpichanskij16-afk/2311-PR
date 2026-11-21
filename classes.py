class Warrior:
    def __init__(self, damage, **kwargs):
        super().__init__(**kwargs)
        self.damage = damage

    def sword_attack(self):
        print(f"Завдає удару мечем на {self.damage} одиниць шкоди")


class Mage:
    def __init__(self, mana, **kwargs):
        super().__init__(**kwargs)
        self.mana = mana

    def heal(self):
        if self.mana >= 20:
            self.mana -= 20
            print(f"Використано магію лікування Залишилось мани: {self.mana}")
        else:
            print("Недостатньо мани для лікування.")


class Paladin(Warrior, Mage):
    def __init__(self, name, damage, mana):
        super().__init__(damage=damage, mana=mana)
        self.name = name

    def battle_turn(self):
        print(f"Паладин {self.name} вступає в бій:")
        self.sword_attack()
        self.heal()


hero = Paladin(name="Артур", damage=45, mana=60)
hero.battle_turn()