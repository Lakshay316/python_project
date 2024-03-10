from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'title': 'Home'})


def screen1(request):
    response = {
        'title': 'Consolidation & Extrapolation',
        'grids': [
            {
                'title': 'Input / Output Current Path',
                'inputFields': [
                    {
                        'inputName': 'Current T-Zero',
                        'inputType': 'text',
                    },
                    {
                        'inputName': 'Previous T-Zero',
                        'inputType': 'text',
                    },
                    {
                        'inputName': 'NTMR',
                        'inputType': 'text',
                    },
                    {
                        'inputName': 'Saracen',
                        'inputType': 'text',
                    },
                    {
                        'inputName': 'Reference',
                        'inputType': 'text',
                    },
                    {
                        'inputName': 'Output',
                        'inputType': 'text',
                    },
                    # {
                    #     'inputName': 'Gender',
                    #     'inputType': 'dropDown',
                    #     'default': 'Male',
                    #     'dropDownOptions': ['Male', 'Female', 'Others']
                    # }
                ]
            },
            {
                'title': 'NTMR Reconciliation Threshold',
                'inputFields': [
                    {
                        'inputName': 'Absolute',
                        'inputType': 'number',
                    },
                    {
                        'inputName': 'Percentage',
                        'inputType': 'float',
                    }
                ]
            }
        ]
    }
    return render(request, 'screen1.html', response)


def screen2(request):
    return render(request, 'screen2.html', {'title': 'Page 2'})


def screen3(request):
    return render(request, 'screen3.html', {'title': 'Page 3'})


def screen4(request):
    return render(request, 'screen4.html', {'title': 'Page 4'})

