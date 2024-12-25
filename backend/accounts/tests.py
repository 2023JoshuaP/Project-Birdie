from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile

class UserModelTest(TestCase):

    def setUp(self):
        # Crear un usuario para las pruebas
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword123',
            email='testuser@example.com',
        )

    def test_user_creation(self):

        user = self.user
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpassword123'))
        self.assertEqual(user.email, 'testuser@example.com')

    def test_default_cover_image(self):

        user = self.user
        self.assertEqual(user.cover_pic.name, 'images/cover/coverphoto.jpg')

    def test_profile_pic_upload(self):
        with tempfile.NamedTemporaryFile(suffix='.jpg') as img:
            img.write(b"dummy content")
            img.flush()
            img.seek(0)
            profile_pic = SimpleUploadedFile(img.name, img.read())

        self.user.profile_pic = profile_pic
        self.user.save()
        self.assertTrue(self.user.profile_pic.name.startswith('images/profile/'))

    def test_follow_user(self):
        user2 = get_user_model().objects.create_user(
            username='testuser2',
            password='testpassword123',

        )
        self.user.following.add(user2)
        user2.followers.add(self.user)
        self.assertTrue(user2.followers.filter(id=self.user.id).exists())

        self.assertTrue(self.user.following.filter(id=user2.id).exists())
    
    def test_profile_pic_path(self):
        with tempfile.NamedTemporaryFile(suffix='.jpg') as img:
            img.write(b"dummy content")
            img.flush()
            img.seek(0)
            profile_pic = SimpleUploadedFile(img.name, img.read())

        self.user.profile_pic = profile_pic
        self.user.save()
        self.assertIn(f"images/profile/{self.user.username}_{self.user.id}/", self.user.profile_pic.name)
    def test_cover_pic_path(self):
        with tempfile.NamedTemporaryFile(suffix='.jpg') as img:
            img.write(b"dummy content")
            img.flush()
            img.seek(0)
            cover_pic = SimpleUploadedFile(img.name, img.read())

        self.user.cover_pic = cover_pic
        self.user.save()
    
    def test_remove_profile_pic(self):
        with tempfile.NamedTemporaryFile(suffix='.jpg') as img:
            img.write(b"dummy content")
            img.flush()
            img.seek(0)
            profile_pic = SimpleUploadedFile(img.name, img.read())

        self.user.profile_pic = profile_pic
        self.user.save()
        self.user.profile_pic.delete()
        self.assertIsNone(self.user.profile_pic.name)
    def test_multiple_followers_and_following(self):
        users = [
            get_user_model().objects.create_user(username=f'user{i}', password='password')
            for i in range(5)
        ]
        for user in users:
            self.user.following.add(user)
            user.followers.add(self.user)

        self.assertEqual(self.user.following.count(), 5)
        for user in users:
            self.assertTrue(user.followers.filter(id=self.user.id).exists())

    