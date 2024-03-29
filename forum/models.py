from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User # Utenti che si sono registrati

class Sezione(models.Model):
    """
    Le sezioni dividono il sito per categorie di discussione
    Ciascuna sezione contiene svariate discussioni.
    Sono create dagli amministratori del sito

    """
    nome_sezione = models.CharField(max_length=80)
    descrizione = models.CharField(max_length=150, blank=True, null= True)
    logo_sezione = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome_sezione

    def get_absolute_url(self):
        return reverse("sezione", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Sezione"
        verbose_name_plural = "Sezioni"

class Discussione(models.Model):
    titolo = models.CharField(max_length=120)
    data_creazione = models.DateTimeField(auto_now_add=True)
    autore_discussione = models.ForeignKey(User, on_delete=models.CASCADE, related_name="discussioni")
    sezione_appartenenza = models.ForeignKey(Sezione, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("discussione", kwargs={"pk": self.pk})
    
    def get_last_discussions(self):
        return Discussione.objects.filter(sezione_appartenenza= self).ordered_by("-data_creazione")[:2]

    def get_number_of_posts_in_section(self):
        return Post.objects.filter(discussione__sezione_appartenenza = self).count()

    class Meta:
        verbose_name = "Discussione"
        verbose_name_plural = "Discussioni"

class Post(models.Model):
    autore_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    contenuto = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    discussione = models.ForeignKey(Discussione, on_delete=models.CASCADE)

    def __str__(self):
        return self.autore_post.username

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

