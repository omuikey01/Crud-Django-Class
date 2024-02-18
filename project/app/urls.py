from django.urls import path
from .views import homepage, formsave, show, editform, editformsave, delete

urlpatterns = [
    path("", homepage),
    path("formsave/", formsave, name="uikey"),
    path("show/", show, name="show"),
    path("editform/<int:mil>/", editform, name="editform"),
    path("editform/", editformsave, name="editform"),
    path("delete/<int:id>/", delete, name="delete")
]
