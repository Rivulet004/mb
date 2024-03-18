from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.



class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="just a test")
    
    def testTextContent(self):
        post = Post.objects.get(id=1)
        expected_obj_name = f"{post.text}"
        self.assertEqual(expected_obj_name, "just a test")
        
        
class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just another test')
        
    def test_view_exists_at_porper_url(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
        
