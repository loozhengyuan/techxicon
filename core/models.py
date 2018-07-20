from django.db import models


class Term(models.Model):
    term = models.CharField(max_length=255, help_text="Terms should ideally be in lowercase and in non-abbreviated format")
    acronym = models.CharField(max_length=255, blank=True, null=True, help_text="Include official acronyms only")
    definition = models.TextField(max_length=65535, help_text="Markdown links will automatically be converted to HTML format")
    explanation = models.TextField(max_length=65535, blank=True, null=True, help_text="Markdown links will automatically be converted to HTML format")
    examples = models.TextField(max_length=65535, blank=True, null=True, help_text="Markdown links will automatically be converted to HTML format")
    see_also = models.TextField(max_length=65535, blank=True, null=True, help_text="Markdown links will automatically be converted to HTML format")
    tags = models.CharField(max_length=255, blank=True, null=True, help_text="Use this field to improve the search relatedness of this term")

    def __str__(self):
        return self.term

    def save(self, *args, **kwargs):
        import re
        self.definition = re.sub(r"\[(.*?)\]\((.*?)\)", r"<a href='\2'>\1</a>", self.definition.strip())
        self.explanation = re.sub(r"\[(.*?)\]\((.*?)\)", r"<a href='\2'>\1</a>", self.explanation.strip())
        self.examples = re.sub(r"\[(.*?)\]\((.*?)\)", r"<a href='\2'>\1</a>", self.examples.strip())
        self.see_also = re.sub(r"\[(.*?)\]\((.*?)\)", r"<a href='\2'>\1</a>", self.see_also.strip())
        if self.acronym == '':
            self.acronym = None
        if self.explanation == '':
            self.explanation = None
        if self.examples == '':
            self.examples = None
        if self.see_also == '':
            self.see_also = None
        super().save(*args, **kwargs)


class SearchLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    search_phrase = models.CharField(max_length=255)

    def __str__(self):
        return self.search_phrase


class ImproveLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    comments = models.TextField(max_length=65535)

    def __str__(self):
        return self.term


class SuggestLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    dept = models.CharField(max_length=255)
    suggestion = models.TextField(max_length=65535)

    def __str__(self):
        return self.suggestion


class FeedbackLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    dept = models.CharField(max_length=255)
    feedback = models.TextField(max_length=65535)

    def __str__(self):
        return self.feedback

