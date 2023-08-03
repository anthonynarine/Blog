from django.db import models
from django.conf import settings

class Post(models.Model):
    """
    Model representing a blog post.

    Fields:
        title (CharField): The title of the blog post, limited to a maximum of 50 characters.
        body (TextField): The main content of the blog post.
        author (ForeignKey): A foreign key relationship to the User model, representing the author of the post.
        created_at (DateTimeField): The date and time when the post was created, set automatically when the post is saved.
        updated_at (DateTimeField): The date and time when the post was last updated, automatically updated when the post is modified.

    Methods:
        __str__(): Returns the string representation of the blog post, which is the title of the post.

    Note:
        The 'settings.AUTH_USER_MODEL' refers to the custom user model set in the project's settings. It allows
        for flexibility in using a custom user model instead of the default Django User model.

    Foreign Key (author):
        The 'author' field establishes a many-to-one relationship between the 'Post' model and the 'User' model.
        It represents the author of the blog post. The 'ForeignKey' field is used to create this relationship.

        When defining a 'ForeignKey', we specify the related model as the first argument. In this case, the
        'User' model is referenced. The 'on_delete' argument is used to specify the behavior when the referenced
        user is deleted. Here, 'on_delete=models.CASCADE' means that if the author (User) is deleted, all their
        associated posts (Post) will also be deleted. This is known as the "cascade" behavior.

        The 'author' field allows us to access the related user's information from a 'Post' object. For example,
        if 'post_obj' is an instance of the 'Post' model, we can access the author's username using 'post_obj.author.username'.
        We can also traverse the relationship in reverse and get all posts authored by a specific user. For instance,
        if 'user_obj' is an instance of the 'User' model, we can get all posts authored by that user using 'user_obj.post_set.all()'.

        The 'ForeignKey' field creates an index on the 'author' column in the database table for efficient lookup and
        querying of related posts by the author.

    """

    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the blog post.

        Returns:
            str: The title of the post.
        """
        return self.title
