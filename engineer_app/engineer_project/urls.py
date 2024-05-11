from django.urls import path
from . import views
from static.files.first_unit.procedures import *
from static.files.second_unit.procedures import *

urlpatterns = [
    path("", views.home, name="home"),
    # FIRST UNIT
    path("first_unit/", views.selector1, name="first_unit"),
    path("first_unit/simple_tax/", views.first_unit_page1, name="simpletax"),
    path("first_unit/simple_tax/ex1/", views.first_unit_page1_exce1, name="simpletax_ex1"),
    path("first_unit/simple_tax/ex1/result/", calculate_capital_value, name="capital_value"),
    # SECOND UNIT
    path("second_unit/", views.selector2, name="second_unit"),
    path("second_unit/capitalization_amortization/", views.second_unit_page1, name="capitalization_amortization"),
    path("second_unit/return_tax/", views.second_unit_page2, name="return_tax"),
    path("second_unit/gradients/", views.second_unit_page3, name="gradients"),
    path("second_unit/gradients/arithmethic_gradient/", views.second_unit_page3_exce1, name="gradients_topic1"),
    path("second_unit/gradients/arithmethic_gradient/result/", calculate_arithmethic_gradient, name="arith_gradient"),
]
