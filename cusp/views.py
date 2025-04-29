from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuoteForm
from django.contrib import messages
from datetime import datetime
import smtplib
import ssl


def index(request):
    return render(request, "cusp/Home.html", )


def quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form_data = serialize_form_data(form)
            messages.success(request, f"Thank You {form_data['Name']}, Message successfully sent")
            print(form_data)
            send_email(form_data)
            return redirect('index')
        else:
            print("Form Errors:", form.errors)  # Print form validation errors
            messages.error(request, "Invalid Email or Cell. Please check your Email/Cell.")

    else:
        form = QuoteForm(initial={'created_date': datetime.now()})

    return render(request, "cusp/quote.html", {'form': form})


# Functions


def serialize_form_data(form):
    """
    Serialize Django form data into JSON format.
    """
    serialized_data = {}
    for field_name, field_value in form.cleaned_data.items():
        serialized_data[field_name] = field_value
    return serialized_data


def send_email(form_data):
    my_email = "mothalindokuhle168@gmail.com"
    my_password = "ebjmkthbnjphixwk"  # Use your App Password

    friend_email = "info@cuspfc.co.za"
    name = form_data['Name']
    email = form_data['Email']
    service = form_data['Service']
    type_of_property = form_data['type_of_property']
    cell = form_data['cell']
    site_address = form_data['Site_Address']

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=friend_email,
            msg=f"Subject: New Quote Request\n\n"
                f"Service: {service}\n"
                f"Type Of Property: {type_of_property}\n"
                f"From: {name}\n"
                f"Email: {email}\n"
                f"Cell: {cell}\n"
                f"Site Address: {site_address}"
        )
    print("Email sent successfully!")
