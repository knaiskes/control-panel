from django.test import TestCase
from relays.models import Relay

class RelayTestCase(TestCase):
    def setUp(self):
        Relay.objects.create(name='relay1', state=False)
        Relay.objects.create(name='relay2') # state: gets the deafult value
        Relay.objects.create(name='relay3', state=True)

    def test_relay_update_state(self):
        relay1 = Relay.objects.get(name='relay1')
        relay2 = Relay.objects.get(name='relay2')
        relay3 = Relay.objects.get(name='relay3')

        self.assertEqual(relay1.update_state(relay1.state), True)
        self.assertEqual(relay2.update_state(relay2.state), True)
        self.assertEqual(relay3.update_state(relay3.state), False)

