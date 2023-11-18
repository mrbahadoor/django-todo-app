from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    
    # Mark as done
    path('mark-as-done/<int:pk>/', views.markAsDone, name='markAsDone'),

    # Mark as undone
    path('mark-as-undone/<int:pk>/', views.markAsDone, name='markAsUndone'),

    # EDIT feature
    path('edit-task/<int:pk>/', views.editTask, name='editTask'),
]
