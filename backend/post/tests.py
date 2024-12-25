from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class PostModelTest(TestCase):
    
    def setUp(self):
        user = get_user_model()
        self.user1 = user.objects.create_user(username="user1", password="password1")
        self.user2 = user.objects.create_user(username="user2", password="password2")
        self.post = Post.objects.create(creator=self.user1, content="Este es un post de prueba.")
    
    
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
    def test_post_creation_valid_content(self):
        """Verificar que el post se crea correctamente con contenido válido."""
        self.assertEqual(self.post.creator.username, "user1")
        self.assertEqual(self.post.content, "Este es un post de prueba.")
        self.assertFalse(self.post.isEdited)
    
    def test_post_like_once(self):
        """Verificar que un usuario puede dar like solo una vez."""
        self.post.likes.add(self.user2)
        self.post.likes.add(self.user2)
        self.assertEqual(self.post.likes.count(), 1)
    
    def test_post_save_once(self):
        """Verificar que un usuario puede guardar un post solo una vez."""
        self.post.saves.add(self.user2)
        self.post.saves.add(self.user2)
        self.assertEqual(self.post.saves.count(), 1)
    
    def test_post_multiple_likes_and_saves(self):
        """Verificar múltiples interacciones de usuarios."""
        self.post.likes.add(self.user2, self.user1)
        self.post.saves.add(self.user2)
        self.assertEqual(self.post.likes.count(), 2)
        self.assertEqual(self.post.saves.count(), 1)
    
    def test_post_edit(self):
        """Verificar la edición de un post."""
        self.post.content = "Este es un post editado."
        self.post.isEdited = True
        self.post.save()
        self.assertEqual(self.post.content, "Este es un post editado.")
        self.assertTrue(self.post.isEdited)
    
    def test_post_str_method(self):
        """Verificar el método __str__."""
        expected_str = f"{self.user1.username} at {self.post.created}"
        self.assertEqual(str(self.post), expected_str)
    
    
    def test_post_delete_user_cascade(self):
        """Verificar que los posts se eliminan cuando se elimina el usuario."""
        self.user1.delete()
        self.assertEqual(Post.objects.filter(creator=self.user1).count(), 0)