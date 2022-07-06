#!/usr/bin/python3

import unittest

from console import Airbnb_Shell

class TestAirbnbShellCommands(unittest.TestCase):
	"""
	Should test the following:
		create
		show
		destroy
		all
		update
		quit
	"""
	def setUp(self):
		self.arbnb_methods = Airbnb_Shell.__dict__

	def test_should_exist_create(self):
		self.assertTrue(self.arbnb_methods.get("do_create"))

	def test_should_exist_show(self):
		self.assertTrue(self.arbnb_methods.get("do_show"))

	def test_should_exist_destroy(self):
		self.assertTrue(self.arbnb_methods.get("do_destroy"))

	def test_should_exist_all(self):
		self.assertTrue(self.arbnb_methods.get("do_all"))

	def test_should_exist_update(self):
		self.assertTrue(self.arbnb_methods.get("do_update"))

	def test_should_exist_quit(self):
		self.assertTrue(self.arbnb_methods.get("do_quit"))
