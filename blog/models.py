from django.db import models
from django.utils import timezone


options = {
('Self Esteem', 'Self Esteem'),
('Body Image', 'Body Image'),
('Stress', 'Stress'),
('Bullying', 'Bullying'),
('Depression', 'Depression'),
('Cyber Addiction', 'Cyber Addiction'),
('Drinking and Smoking', 'Drinking and Smoking'),
('Teen Pregnancy', 'Teen Pregnancy'),
('Underage Sex', 'Underage Sex'),
('Child Abuse', 'Child Abuse'),
('Peer Pressure', 'Peer Pressure'),
('Eating Disorder', 'Eating Disorder'),
('LGBTQ', 'LGBTQ'),
('Strict Parents', 'Strict Parents'),
('Sleep', 'Sleep'),
}

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    category = models.CharField(max_length=200, choices=options, default='other')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

def approved_comments(self):
    return self.comments.filter(approved_comment=True)
