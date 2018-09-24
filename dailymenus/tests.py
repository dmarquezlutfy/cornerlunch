from django.test import TestCase
from .models import DailyMenu, MenuAlternative

import datetime


class DailyMenuTestCase(TestCase):


    def setUp(self):
        pass

    def test_create_daily_menu(self):
        daily_menu = DailyMenu(availability_day=datetime.date.today())
        daily_menu.save()

        MenuAlternative.objects.bulk_create([
            MenuAlternative(description='Pastel de choclo, Ensalada y Postre', daily_menu=daily_menu),
            MenuAlternative(description='Arroz con nugget de pollo, Ensalada y Postre', daily_menu=daily_menu),
            MenuAlternative(description='Arroz con hamburguesa, Ensalada y Postre', daily_menu=daily_menu),
        ])

        self.assertEqual(MenuAlternative.objects.filter(daily_menu=daily_menu).count(), 3)

