from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls.base import reverse
from .models import Post
"""
TEST PLAN
    
    models
        1. Is instance created?
        2. Is instance attributes equal to creation values?
        3. Is instance string representation equal to one of attributes?

    views
        1. Is view returning 'xxx' status code if succeed?
        2. Is view returning 'yyy' status code if failed?
        3. Is all URLs pointing to 'xxx' view?
        4. Is view returning 'xxx' template?
        5. Has 'xxx' template 'aaa' information?

"""

USER_NAME = 'test'
USER_EMAIL = 'test@example.com'
POST_TITLE = "the song"
POST_CONTENT = "la la la"


class PostModelTest(TestCase):
    def setUp(self) -> None:
        """
        create user & post in term of tests
        """
        self.user = get_user_model().objects.create_user(
            username=USER_NAME, email=USER_EMAIL, password='****************')

        self.post = Post.objects.create(author=self.user,
                                        title=POST_TITLE,
                                        body=POST_CONTENT)

    def test_content(self):
        self.assertEqual(self.user.id, self.post.author_id)
        self.assertEqual(POST_TITLE, self.post.title)
        self.assertEqual(POST_CONTENT, self.post.body)

    def test_str_representation(self):
        self.assertEqual(self.post.title, str(self.post))


class HomePageViewTest(TestCase):
    def test_response_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_response_404(self):
        response = self.client.get('/poasdkpoasdkpoakdpoakd')
        self.assertEqual(response.status_code, 404)

    def test_all_urls(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_site_content(self):
        response = self.client.get(reverse('home_page'))
        self.assertContains(response, 'Blog')


class PostPageViewTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username=USER_NAME, email=USER_EMAIL, password='****************')

        self.post = Post.objects.create(body=POST_CONTENT,
                                        author=self.user,
                                        title=POST_TITLE)

    def test_response_200(self):
        response = self.client.get(f'/post/{self.post.id}')
        self.assertEqual(response.status_code, 200)

    def test_response_404(self):
        """
        ensure that no response when querying for non exsisting object
        """
        no_response = self.client.get(f'/post/10000')
        self.assertEqual(no_response.status_code, 404)

    def test_template(self):
        response = self.client.get(f'/post/{self.post.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post.html')

    def test_content(self):
        response = self.client.get(f'/post/{self.post.id}')
        self.assertContains(response, self.post.body)
