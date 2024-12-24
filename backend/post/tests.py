from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class PostModelTest(TestCase):
    
    def setUp(self):
        user = get_user_model()
        self.user1 = user.objects.create_user(username="user1", password="password1")
        self.user2 = user.objects.create_user(username="user2", password="password2")
        self.post = Post.objects.create(creator=self.user1, content="Este es un post de prueba.")
    
    def test_post_creation_without_image(self):
        self.assertEqual(self.post.creator.username, "user1")
        self.assertEqual(self.post.content, "Este es un post de prueba sin imagen.")
        self.assertEqual(self.post.image.name, '')
    
    def test_like_post(self):
        self.post.likes.add(self.user2)
        self.assertTrue(self.post.likes.filter(id=self.user2.id).exists())
    
    def test_save_post(self):
        self.post.saves.add(self.user2)
        self.assertTrue(self.post.saves.filter(id=self.user2.id).exists())
    
    def test_post_creation_multiple_likes_and_saves(self):
        self.post.likes.add(self.user2)
        self.post.likes.add(self.user1)
        self.post.saves.add(self.user2)
        self.assertTrue(self.post.likes.filter(id=self.user1.id).exists())
        self.assertTrue(self.post.likes.filter(id=self.user2.id).exists())
        self.assertTrue(self.post.saves.filter(id=self.user2.id).exists())
    
    def test_edit_post(self):
        self.post.content = "Este es un post editado."
        self.post.isEdited = True
        self.post.save()
        self.assertEqual(self.post.content, "Este es un post editado.")
        self.assertTrue(self.post.isEdited)
    
    def test_post_str_method(self):
        expected_str = f"{self.user1.username} at {self.post.created}"
        self.assertEqual(str(self.post), expected_str)