from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from post.models import Post, Comment
from post.api.serializers import PostSerializer, CommentSerializer

User = get_user_model()

class TestPostSerializer(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@test.com', password='password')
        self.post = Post.objects.create(creator=self.user, content="Test post content")
        self.client.login(username='testuser', password='password')  # Autenticación del usuario

    def test_post_serializer_valid_data(self):
        serializer = PostSerializer(instance=self.post, context={"request": self.client.request().wsgi_request})  # Pasar el contexto
        serialized_data = serializer.data
        self.assertEqual(serialized_data['creator']['username'], self.user.username)
        self.assertEqual(serialized_data['content'], self.post.content)
        self.assertEqual(serialized_data['likes'], 0)
    def test_post_serializer_invalid_data(self):
        data = {"content": ""}
        serializer = PostSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('content', serializer.errors)

class TestCommentSerializer(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@test.com', password='password')
        self.post = Post.objects.create(creator=self.user, content="Test post content")
        self.comment = Comment.objects.create(post=self.post, creator=self.user, content="Test comment")
        self.client.login(username='testuser', password='password')
    

    def test_comment_creation(self):
        data = {"content": "New comment"}
        context = {"request": self.client.request().wsgi_request, "post_id": self.post.id}
        serializer = CommentSerializer(data=data, context=context)
        self.assertTrue(serializer.is_valid())
        comment = serializer.save()
        self.assertEqual(comment.content, "New comment")
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.creator, self.user)
    
    def test_comment_serializer_valid_data(self):
        serializer = CommentSerializer(instance=self.comment)
        serialized_data = serializer.data
        self.assertEqual(serialized_data['creator']['username'], self.user.username)
        self.assertEqual(serialized_data['post_content'], self.post.content)