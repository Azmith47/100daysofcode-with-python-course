from unittest.mock import patch
import random
import pytest
from actors import Creature, Dragon, Wizard


def test_creature_init_():
    creature = Creature("Wolf", 20)
    assert creature.name == "Wolf"
    assert creature.level == 20


@patch.object(random, "randint")
def test_creature_defensive_roll(m):
    creature = Creature("Wolf", 20)
    m.return_value = 6
    assert creature.defensive_roll() == 120


def test_dragon_init_():
    creature = Dragon("Smaug", 70, 2, True)
    assert creature.name == "Smaug"
    assert creature.level == 70
    assert creature.scaliness == 2
    assert creature.breaths_fire == True


@patch.object(random, "randint")
def test_dragon_defensive_roll(m):
    creature = Dragon("Smaug", 70, 2, True)
    m.return_value = 5
    assert creature.defensive_roll() == 1_400


def test_wizard_init_():
    creature = Wizard("Gandalf", 1000)
    assert creature.name == "Gandalf"
    assert creature.level == 1000


@patch.object(random, "randint")
def test_wizard_attack(m):
    player = Wizard("Gandalf", 1000)
    creature = Dragon("Smaug", 70, 2, True)
    m.return_value = 10
    assert player.attack(creature) == True
