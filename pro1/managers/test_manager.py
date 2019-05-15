from ..models import Test

class TestManager(object):

   def create(self, name):
       Test.objects.create(
           name=name
       )

   def filter_by_name(self, name):
      return Test.objects.filter(
          name=name
      )

   def get_all(self):
       return Test.objects.filter()