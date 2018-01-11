from __future__ import unicode_literals
import json

from django.test import TestCase


# Create your tests here.
class BookingViewsTestCase(TestCase):

    def test_booking_list_view(self):
        url = '/api/bookings/'
        payload_1 = {
            'name': 'test',
            'email': 'test@test.com',
            'description': 'test',
            'phone': '0406756447',
            'company_name': 'test co',
            'meetup_location': 'test place',
            'date': '2018-01-05',
            'time_slot': '9:30-10:00',
        }

        payload_2 = {
            'name': 'James',
            'email': 'james@test.com',
            'description': 'james is great.',
            'phone': '0406756467',
            'company_name': 'James co',
            'meetup_location': 'Test Coffee S',
            'date': '2018-01-05',
            'time_slot': '9:30-10:00',
        }

        # create both bookings
        # resp = self.client.get(url)
        # self.assertEqual(resp.status_code, 200)
        # self.assertIn(..., resp.content)
        # count/length == 2?

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
            resp_json['time_slot'][0], 'This field may not be null.')

    def test_booking_post_with_blank_data_fails(self):
        url = '/api/bookings/'
        payload = {
            'name': '',
            'email': '',
            'description': '',
            'phone': '',
            'company_name': '',
            'meetup_location': '',
            'date': '2018-01-05',
            'time_slot': '',
        }
        resp = self.client.post(
            url, json.dumps(payload), content_type='application/json')
        self.assertEqual(resp.status_code, 400)
        resp_json = resp.json()
        self.assertEqual(
            resp_json['name'][0], 'This field may not be blank.')
        self.assertEqual(
            resp_json['email'][0], 'This field may not be blank.')
        self.assertEqual(
            resp_json['description'][0], 'This field may not be blank.')
        self.assertEqual(
            resp_json['phone'][0], 'This field may not be blank.')
        self.assertEqual(
            resp_json['company_name'][0], 'This field may not be blank.')
        self.assertEqual(
            resp_json['meetup_location'][0], 'This field may not be blank.')
        self.assertEqual(
            resp_json['time_slot'][0], 'This field may not be blank.')

    def test_booking_post_with_incorrect_email_format_fails(self):
        url = '/api/bookings/'
        payload = {
            'name': 'test',
            'email': 'test',
            'description': 'test',
            'phone': '0406756447',
            'company_name': 'test co',
            'meetup_location': 'test place',
            'date': '2018-01-05',
            'time_slot': '9:30-10:00',
        }
        resp = self.client.post(
            url, json.dumps(payload), content_type='application/json')
        self.assertEqual(resp.status_code, 400)
        resp_json = resp.json()
        self.assertEqual(
            resp_json['email'][0], 'Enter a valid email address.')

    def test_booking_post_with_incorrect_date_format_fails(self):
        url = '/api/bookings/'
        payload = {
            'name': 'test',
            'email': 'test',
            'description': 'test',
            'phone': '0406756447',
            'company_name': 'test co',
            'meetup_location': 'test place',
            'date': '2018',
            'time_slot': '9:30-10:00',
        }
        resp = self.client.post(
            url, json.dumps(payload), content_type='application/json')
        self.assertEqual(resp.status_code, 400)
        resp_json = resp.json()
        self.assertEqual(
            resp_json['date'][0], 'Date has wrong format. Use one of these formats instead: YYYY[-MM[-DD]].')

    # TO DO
    # def test_booking_post_with_incorrect_phone_format_fails(self):
