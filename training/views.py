from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import TrainingRecord
from .forms import TrainingRecordForm


def dashboard(request):
    records = TrainingRecord.objects.all()

    context = {
        'total_records': records.count(),
        'completed_records': records.filter(
            training_status='Completed'
        ).count(),
        'ongoing_records': records.filter(
            training_status='Ongoing'
        ).count(),
        'planned_records': records.filter(
            training_status='Planned'
        ).count(),
        'recent_records': records[:5],
    }

    return render(request, 'training/dashboard.html', context)


def training_list(request):
    records = TrainingRecord.objects.all()

    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')

    if search_query:
        records = records.filter(
            Q(training_title__icontains=search_query) |
            Q(employee_name__icontains=search_query)
        )

    if status_filter:
        records = records.filter(training_status=status_filter)

    context = {
        'records': records,
        'search_query': search_query,
        'status_filter': status_filter,
        'status_choices': TrainingRecord.STATUS_CHOICES,
    }

    return render(request, 'training/training_list.html', context)


def training_create(request):
    if request.method == 'POST':
        form = TrainingRecordForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Training record created successfully.'
            )
            return redirect('training_list')
    else:
        form = TrainingRecordForm()

    return render(
        request,
        'training/training_form.html',
        {
            'form': form,
            'page_title': 'Add Training Record',
        }
    )


def training_update(request, pk):
    record = get_object_or_404(TrainingRecord, pk=pk)

    if request.method == 'POST':
        form = TrainingRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Training record updated successfully.'
            )
            return redirect('training_list')
    else:
        form = TrainingRecordForm(instance=record)

    return render(
        request,
        'training/training_form.html',
        {
            'form': form,
            'page_title': 'Edit Training Record',
        }
    )


def training_delete(request, pk):
    record = get_object_or_404(TrainingRecord, pk=pk)

    if request.method == 'POST':
        record.delete()
        messages.success(
            request,
            'Training record deleted successfully.'
        )
        return redirect('training_list')

    return render(
        request,
        'training/training_confirm_delete.html',
        {'record': record}
    )