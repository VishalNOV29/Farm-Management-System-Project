from unicodedata import name
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("",views.index,name="home"),
    path("home",views.index,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("farm_management_solution",views.farm_management_solution,name="Farm management solution"),
    path("farm_risk_assessment",views.farm_risk_assessment,name="Farm risk assessment"),
    path("supply_chain_traceability_solution",views.scts,name="supply chian traceability solution"),
    path("farming",views.farming,name="farming"),
    path("seed_companies",views.seed_companies,name="seed companies."),
    path("food_processing",views.food_processing,name="food processing"),
    path("blogs",views.blogs,name="blogs"),
    path("news",views.news,name="news"),
    path("webinars",views.webinars,name="webinars"),
    path("case_study",views.case_study,name="case study"),
    path("about",views.about,name="about"),
    path("carrers",views.carrers,name="carrers"),
    path("contact",views.contact,name="contact"),

]
