from django.test import TestCase
from .models import BucketList
# Create your tests here.

class ModelTestCase(TestCase):
	def setUp(self):
		self.bucketlist_name = "Write world class code"
		self.bucketlist = BucketList(name=self.bucketlist_name)

	def test_model_can_create_a_bucketlist(self):
		old_count = BucketList.objects.count()
		self.bucketlist.save()
		new_count = BucketList.objects.count()
		self.assertNotEqual(old_count, new_count)