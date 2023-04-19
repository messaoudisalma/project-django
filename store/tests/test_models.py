from django.test import TestCase

from store.models import Category, Product

from django.contrib.auth.models import User

class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='phone', slug='phone')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test Cetegory model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'phone')


class TestProductModel(TestCase):
    
    def setUp(self):
        Category.objects.create(name='phone', slug='phone')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='phone', created_by_id=1, slug='phone', price='1222.25', image='django')
    
    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'phone')
