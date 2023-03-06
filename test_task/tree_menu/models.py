from django.db import models


class TreeMenuModel(models.Model):
    title = models.CharField(max_length=200)
    base_tree_menu_item = models.OneToOneField(
        'TreeMenuItemModel',
        related_name='main_parent',
        on_delete=models.CASCADE
    )


class TreeMenuItemModel(models.Model):
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='tree_menu_child_items',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    text_content = models.TextField(max_length=4000)