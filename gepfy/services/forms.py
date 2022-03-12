from services.models import Service

class ServiceForm():
    class Meta:
        model =  Service
        fields = [
            'empresa',
            'logo',
            'estado',
            'fecha_emision',
            'fecha_vencimiento',
            'monto_total',
            'fecha_pago',
        ]
        labels = {
            'empresa': 'Empresa:',
            'logo': 'Logo de la empresa:',
            'estado': 'Estado de pago:',
            'fecha_emision': 'Fecha de emision de la factura:',
            'fecha_vencimiento': 'Fecha de vencimiento de la factura:',
            'monto_total': 'Monto Total de la facturacion:',
            'fecha_pago': 'Fecha de Pago de la factura:',
        }