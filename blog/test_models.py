from django.test import TestCase
from allauth.utils import get_user_model
from .models import Blog, Category, Comment

class TestBlogModel(TestCase):

    def test_can_create_a_featured_blog_post(self):
        blog = Blog(title="Create a Test Blog", content="This is a test blog post", featured=True, tag="Test", user_id=1)
        user = get_user_model().objects.create(username='testuser')
        blog.save()
        self.assertEqual(blog.title, "Create a Test Blog")
        self.assertEqual(blog.content, "This is a test blog post")
        self.assertEqual(blog.tag, "Test")
        self.assertEqual(blog.user_id, 1)

    def test_can_create_a_category(self):
        category = Category(title="Fashion")
        category.save()
        self.assertEqual(category.title, "Fashion")
    
    def test_can_create_a_comment(self):
        comment = Comment(user_id=1, content="Testing", blog_id=2)
        comment.save()
        self.assertEqual(comment.user_id, 1)
        self.assertEqual(comment.content, "Testing")
        self.assertEqual(comment.blog_id, 2)