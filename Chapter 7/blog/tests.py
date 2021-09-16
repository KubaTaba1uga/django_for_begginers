from django.contrib.auth import get_user_model
from django.http import response
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
        *6. Is 'C/R/U/D' operation performed sucesfully?

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
    status_code_success = 200
    status_code_fail = 404
    url_name = 'post_show_all'
    template_name = 'post_all.html'

    def test_response_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)

    def test_response_fail(self):
        response = self.client.get('/poasdkpoasdkpoakdpoakd')
        self.assertEqual(response.status_code, self.status_code_fail)

    def test_all_urls(self):
        response = self.client.get(reverse(self.url_name))
        self.assertEqual(response.status_code, self.status_code_success)

    def test_template(self):
        response = self.client.get(reverse(self.url_name))
        self.assertEqual(response.status_code, self.status_code_success)
        self.assertTemplateUsed(response, self.template_name)

    def test_site_content(self):
        response = self.client.get(reverse(self.url_name))
        self.assertEqual(response.status_code, self.status_code_success)
        self.assertContains(response, 'Blog')


class PostDetailsViewTest(TestCase):
    status_code_success = 200
    status_code_fail = 404
    url_name = 'post_show_details'
    template_name = 'post_details.html'

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username=USER_NAME, email=USER_EMAIL, password='****************')

        self.post = Post.objects.create(body=POST_CONTENT,
                                        author=self.user,
                                        title=POST_TITLE)

    def test_response_success(self):
        response = self.client.get(
            reverse(self.url_name, args=str(self.post.id)))
        self.assertEqual(response.status_code, self.status_code_success)

    def test_response_fail(self):
        no_response = self.client.get(reverse(self.url_name, args='0'))
        self.assertEqual(no_response.status_code, self.status_code_fail)

    def test_all_urls(self):
        response = self.client.get(
            reverse(self.url_name, args=str(self.post.id)))
        self.assertEqual(response.status_code, self.status_code_success)

    def test_template(self):
        response = self.client.get(
            reverse(self.url_name, args=str(self.post.id)))
        self.assertEqual(response.status_code, self.status_code_success)
        self.assertTemplateUsed(response, self.template_name)

    def test_content(self):
        response = self.client.get(
            reverse(self.url_name, args=str(self.post.id)))
        self.assertContains(response, self.post.body)
        self.assertContains(response, self.post.title)


class PostCreateViewTest(TestCase):
    form_failed = {
        'body': POST_CONTENT,
        'title': POST_TITLE,
    }

    status_code_success = 302
    status_code_fail = 200
    url_name = 'post_create'
    template_name_success = 'post_details.html'
    template_name_fail = 'post_create.html'

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username=USER_NAME, email=USER_EMAIL, password='****************')

        self.form_succeed = {
            'body': POST_CONTENT,
            'title': POST_TITLE,
            'author': self.user.id
        }

    def test_response_success(self):
        """
        ensure request is redirected to 'post_details.html' view,
        if post data is valid
        """
        response = self.client.post(reverse(self.url_name),
                                    data=self.form_succeed)
        self.assertEqual(response.status_code, self.status_code_success)

    def test_response_fail(self):
        """
        ensure request is redirected to 'post_create' view,
        if post data is not valid
        """
        response = self.client.post(reverse(self.url_name),
                                    data=self.form_failed)
        self.assertEqual(response.status_code, self.status_code_fail)
        self.assertTemplateUsed(response, self.template_name_fail)

    def test_all_urls(self):
        response = self.client.get(reverse(self.url_name))
        self.assertEqual(response.status_code, self.status_code_fail)

    def test_template_success(self):
        response = self.client.post(reverse('post_create'),
                                    data=self.form_succeed)
        self.assertEqual(response.status_code, self.status_code_success)
        response = self.client.get(response.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_name_success)

    def test_content(self):
        response = self.client.post(reverse('post_create'),
                                    data=self.form_succeed)
        self.assertEqual(response.status_code, self.status_code_success)

        response = self.client.get(response.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_name_success)

        post = Post.objects.last()
        for element in (post.title, post.body):
            self.assertContains(response, element)

    def test_create(self):
        self.client.post(reverse('post_create'), data=self.form_succeed)
        post = Post.objects.last()
        self.assertEqual(post.title, POST_TITLE)
        self.assertEqual(post.body, POST_CONTENT)
        self.assertEqual(str(post.author_id), str(self.user.id))


class PostDeleteViewTest(TestCase):
    status_code_confirm = 200
    status_code_success = 302
    url_name = 'post_delete'
    template_name_confirm = 'post_delete.html'

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username=USER_NAME, email=USER_EMAIL, password='****************')

        self.post = Post.objects.create(body=POST_CONTENT,
                                        author=self.user,
                                        title=POST_TITLE)

    def test_response_confirmation(self):
        response = self.client.get(
            reverse(self.url_name, args=str(self.post.id)))
        self.assertEqual(response.status_code, self.status_code_confirm)

    def test_response_success(self):
        response = self.client.post(
            reverse(self.url_name, args=str(self.post.id)))
        self.assertEqual(response.status_code, self.status_code_success)

    """
    No fail test, because only transmitted form data is csrf token
    """

    def test_all_urls(self):
        response = self.client.get(
            reverse(self.url_name, args=str(self.user.id)))
        self.assertEqual(response.status_code, self.status_code_confirm)

    def test_template_confirmation(self):
        response = self.client.get(
            reverse(self.url_name, args=str(self.post.id)))
        self.assertEqual(response.status_code, self.status_code_confirm)
        self.assertTemplateUsed(response, self.template_name_confirm)

    def test_content(self):
        response = self.client.get(
            reverse(self.url_name, args=str(self.post.id)))
        self.assertEqual(response.status_code, self.status_code_confirm)
        self.assertContains(response, 'Delete post')

    def test_delete(self):
        response = self.client.post(
            reverse(self.url_name, args=str(self.post.id)))
        self.assertEqual(response.status_code, self.status_code_success)
        self.assertIsNone(Post.objects.filter(id=self.post.id).first())


class PostUpdateViewTest(TestCase):
    status_code_confirm = 200
    status_code_success = 302
    url_name = 'post_update'
    template_name_confirm = 'post_update.html'

    form_succees = {
        'body': POST_CONTENT[:int(len(POST_CONTENT) / 2)],
        'title': POST_TITLE[::2]
    }
    form_fail = {
        'body': POST_CONTENT[:int(len(POST_CONTENT) / 2)],
    }

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username=USER_NAME, email=USER_EMAIL, password='****************')

        self.post = Post.objects.create(body=POST_CONTENT,
                                        author=self.user,
                                        title=POST_TITLE)

    def test_response_confirmation(self):
        response = self.client.get(
            reverse(self.url_name, args=str(self.post.id)))
        self.assertEqual(response.status_code, self.status_code_confirm)

    def test_response_success(self):
        response = self.client.post(
            reverse(self.url_name, args=str(self.post.id)), self.form_succees)
        self.assertEqual(response.status_code, self.status_code_success)

    def test_response_fail(self):
        """
        if invalid form transmitted, return Update page
        """
        response = self.client.post(
            reverse(self.url_name, args=str(self.post.id)), self.form_fail)
        self.assertEqual(response.status_code, self.status_code_confirm)

    def test_all_urls(self):
        response = self.client.get(
            reverse(self.url_name, args=str(self.user.id)))
        self.assertEqual(response.status_code, self.status_code_confirm)

    def test_template_confirmation(self):
        response = self.client.get(
            reverse(self.url_name, args=str(self.post.id)))
        self.assertEqual(response.status_code, self.status_code_confirm)
        self.assertTemplateUsed(response, self.template_name_confirm)

    def test_content(self):
        response = self.client.post(
            reverse(self.url_name, args=str(self.post.id)), self.form_succees)
        self.assertEqual(response.status_code, self.status_code_success)
        response = self.client.get(response.url)
        for value in self.form_succees.values():
            self.assertContains(response, value)

    def test_update(self):
        self.client.post(reverse(self.url_name, args=str(self.post.id)),
                         self.form_succees)
        post = Post.objects.get(id=self.post.id)

        for value, model_value in zip(self.form_succees.values(),
                                      (post.body, post.title)):
            self.assertEqual(value, model_value)
