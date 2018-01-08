from __future__ import unicode_literals
import json

from django.test import TestCase


# Create your tests here.
class BookingModelTestCase(TestCase):

    def test_booking_post_with_no_data_fails(self):
        url = '/api/bookings/'
        payload = {
            'name': None,
            'email': None,
            'description': None,
            'phone': None,
            'company_name': None,
            'meetup_location': None,
            'date': None,
            'time_slot': None,
        }
        resp = self.client.post(
            url, json.dumps(payload), content_type='application/json')
        self.assertEqual(resp.status_code, 400)
        resp_json = resp.json()
        self.assertEqual(
            resp_json['name'][0], 'This field may not be null.')
        self.assertEqual(
            resp_json['email'][0], 'This field may not be null.')
        self.assertEqual(
            resp_json['description'][0], 'This field may not be null.')
        self.assertEqual(
            resp_json['phone'][0], 'This field may not be null.')
        self.assertEqual(
            resp_json['company_name'][0], 'This field may not be null.')
        self.assertEqual(
            resp_json['meetup_location'][0], 'This field may not be null.')
        self.assertEqual(
            resp_json['date'][0], 'This field may not be null.')
        self.assertEqual(
            resp_json['time_slot'][0], 'This field may not be null')
