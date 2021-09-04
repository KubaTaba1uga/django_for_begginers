from unittest.case import expectedFailure
from django.test import TestCase
from django.test.testcases import SimpleTestCase
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(content='test test test')

    def test_text_content(self):
        """
        ensure that post is created properly in db
        by checking the post's content, created during 'setUp'
        """
        post = Post.objects.get(id=1)
        self.assertEqual(str(post.content), 'test test test')


class PostPageTest(TestCase):
    def setUp(self):
        Post.objects.create(content='test test test 2')

    def test_response_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_additional_urls(self):
        """
        ensure that all urls pointing to the 'posts' app are working
        """
        posts = self.client.get(reverse('posts'))
        self.assertEqual(posts.status_code, 200)

    def test_view_template_usage(self):
        """
        ensure that view class is using appropriate template
        """
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts.html')
