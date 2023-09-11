from django.shortcuts import render
from django.core.paginator import Paginator
from datetime import datetime

def home(request):
     doctor=[
        {'name':"Dr. Sarah Smith",
        'image':"images//doctor3.jpg",
        'expert':"Cardiologist",
        'time':12,
         },
         
        {'name':"Dr. James Johnson",
        'image':"images//doctor5.png",
        'expert':"Orthopedic Surgeon",
        'time':9,
         },
         {'name':"Dr. Emily Williams",
        'image':"images//doctor5.jpg",
        'expert':"Pediatrician",
        'time':12,
         },
        {'name':"Dr. John Doe",
        'image':"images//doctor6.jpg",
        'expert':"Neurologist",
        'time':8,
         },
         
        {'name':"Dr. Amanda Lee",
        'image':"images//doctor4.jpg",
        'expert':"Dermatologist",
        'time':9,
         },
         {'name':"Dr. Michael Roberts",
        'image':"images//doctor7.jpg",
        'expert':"Psychiatrist",
        'time':7,
         }
        ]
     return render(request,"index.html",{'doctor':doctor})

def about(request):
    return render(request,"about.html")

def doctor(request):
    doctor=[
        {'name':"Dr. Sarah Smith",
        'expert':"Cardiologist",
        'thought':"Available for Your Health Journey 🌟",
        'image':"images//doctor3.jpg"
         },
         
        {'name':"Dr. James Johnson",
        'expert':"Orthopedic Surgeon",
        'thought':"Ready to Assist Your Health Needs 💼",
        'image':"images//doctor5.png"
         },
         {'name':"Dr. Emily Williams",
        'expert':"Pediatrician",
        'thought':"Focused on Your Wellness Journey 🌿",
        'image':"images//doctor5.jpg"
         }
        ]
    doctor2=[
        {'name':"Dr. John Doe",
        'expert':"Neurologist",
        'thought':"Committed to Your Brain Health 🧠",
        'image':"images//doctor6.jpg"
         },
         
        {'name':"Dr. Amanda Lee",
        'expert':"Dermatologist",
        'thought':"Caring for Your Skin's Health 🌸",
        'image':"images//doctor4.jpg"
         },
         {'name':"Dr. Michael Roberts",
        'expert':"Psychiatrist",
        'thought':"Supporting Your Mental Wellness 🧘‍♂️",
        'image':"images//doctor7.jpg"
         }
        ]
    return render(request,"doctor.html",{'doctor':doctor,'doctor2':doctor2})


def contact(request):
    return render(request,"contact.html")

def shop(request):
    product1=[
        {
            'name':"Thermometer Gun",
            'image':"images//6.png",
            'price':"$400.00"
        },
        {
            'name':"Blue Hand Gloves",
            'image':"images//7.png",
            'price':"$800.00"
        },
        {
            'name':"Digital Strthoscope",
            'image':"images//8.png",
            'price':"$600.00"
        }
    ]
    product2=[
        {
            'name':"Thermometer Gun",
            'image':"images//6.png",
            'price':"$400.00"
        },
        {
            'name':"Blue Hand Gloves",
            'image':"images//7.png",
            'price':"$800.00"
        },
        {
            'name':"Digital Strthoscope",
            'image':"images//8.png",
            'price':"$600.00"
        }
    ]
    product3=[
        {
            'name':"Thermometer Gun",
            'image':"images//6.png",
            'price':"$400.00"
        },
        {
            'name':"Blue Hand Gloves",
            'image':"images//7.png",
            'price':"$800.00"
        },
        {
            'name':"Digital Strthoscope",
            'image':"images//8.png",
            'price':"$600.00"
        }
    ]
    return render(request,"shop.html",{'product1':product1,'product2':product2,'product3':product3})

def userlogin(request):
    return render(request,"login.html")