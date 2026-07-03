from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Buyer, Report

@login_required(login_url='/login/')
def report(request):
    buyers = Buyer.objects.all()
    return render(request, 'report.html', {
        'buyers': buyers
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("report")

    return render(request, "login.html")    

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def save_report(request):
    if request.method == "POST":
        report_id = request.POST.get('report_id')
        email = request.POST.get('email')
        date = request.POST.get('date')
        ref = request.POST.get('Reference_number')
        itemcode = request.POST.get('Iteam_code')
        pino = request.POST.get('Internal_PI_no')
        buyer_id = request.POST.get('buyer')
        
        buyer_name = ""
        if buyer_id:
            try:
                buyer = Buyer.objects.get(id=buyer_id)
                buyer_name = buyer.name
            except Buyer.DoesNotExist:
                pass

        po_no = request.POST.get('po_no')
        collection = request.POST.get('collection')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        materials = request.POST.get('materials')
        item_size = request.POST.get('item_size')
        carton_size = request.POST.get('carton_size')
        net_weight = request.POST.get('net_weight')
        gross_weight = request.POST.get('gross_weight')
        remarks = request.POST.get('remarks')
        result = request.POST.get('result', 'draft')

        if report_id:
            try:
                report_obj = Report.objects.get(id=report_id)
            except Report.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Report not found"}, status=404)
        else:
            report_obj = Report()

        report_obj.email = email
        report_obj.inspection_date = date if date else None
        report_obj.reference_number = ref
        report_obj.item_code = itemcode
        report_obj.internal_pi_no = pino
        report_obj.buyer = buyer_name
        report_obj.po_no = po_no
        report_obj.collection = collection
        report_obj.description = description
        report_obj.quantity = quantity
        report_obj.materials = materials
        report_obj.item_size = item_size
        report_obj.carton_size = carton_size
        report_obj.net_weight = net_weight
        report_obj.gross_weight = gross_weight
        report_obj.remarks = remarks
        report_obj.status = result
        
        images_data = request.POST.get('images')
        if images_data:
            report_obj.images_data = images_data
        
        report_obj.save()

        return JsonResponse({"status": "success", "report_id": report_obj.id})

    return JsonResponse({"status": "error", "message": "Invalid method"}, status=400)

@login_required(login_url='/login/')
def view_reports(request):
    reports = Report.objects.all().order_by('-created_at')
    return render(request, 'report_list.html', {'reports': reports})

@login_required(login_url='/login/')
def edit_report(request, report_id):
    try:
        report_instance = Report.objects.get(id=report_id)
    except Report.DoesNotExist:
        return redirect('view_reports')
    
    buyers = Buyer.objects.all()
    return render(request, 'report.html', {
        'buyers': buyers,
        'report_instance': report_instance
    })

@login_required(login_url='/login/')
def delete_report(request, report_id):
    try:
        report_instance = Report.objects.get(id=report_id)
        report_instance.delete()
    except Report.DoesNotExist:
        pass
    return redirect('view_reports')