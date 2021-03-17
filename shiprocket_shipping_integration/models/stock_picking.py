from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    shiprocket_order_id = fields.Char(string="Shiprocket Order ID", help="", copy=False)
    shiprocket_shipment_id = fields.Char(string="Shiprocket Shipment ID", help="", copy=False)
    shiprocket_label_url = fields.Char(string="Shiprocket Label URL", help="", copy=False)
    shiprocket_shipping_charge_ids = fields.One2many("shiprocket.shipping.charge", "picking_id", string="Shiprocket Rate Matrix")
    shiprocket_shipping_charge_id = fields.Many2one("shiprocket.shipping.charge", string="Recommended Courier",help="This Method Is Use Full For Generating The Label",copy=False)
    shiprocket_pickup = fields.Boolean(string="Shiprocket Pickup", default=False)

    def get_shiprocket_charges(self):
        if self.delivery_type == "shiprocket" and self.shiprocket_shipment_id:
            res_status, res_message = self.carrier_id and self.carrier_id.get_shiprocket_charges(self)
            if not res_status:
                raise ValidationError(res_message)
            else:
                return {'effect': {
                    'fadeout': 'slow',
                    'message': "Shipping Charges Imported Successfully..",
                    'img_url': '/web/static/src/img/smile.svg',
                    'type': 'rainbow_man'}}

    def generate_shiprocket_pickup_manually(self):
        if self.delivery_type == "shiprocket" and not self.shiprocket_pickup:
            pickup_done , message = self.carrier_id.generate_shiprocket_pickup(self)
            if not pickup_done:
                raise ValidationError(message)

    def generate_shiprocket_awd(self):
        if self.delivery_type == "shiprocket" and self.shiprocket_shipment_id:
            res_status, res_message = self.carrier_id and self.carrier_id.generate_shiprocket_awd(self)
            if not res_status:
                raise ValidationError(res_message)
            else:
                return {'effect': {
                    'fadeout': 'slow',
                    'message': "AWD Imported Successfully..",
                    'img_url': '/web/static/src/img/smile.svg',
                    'type': 'rainbow_man'}}

    def generate_shiprocket_label(self):
        if self.delivery_type == "shiprocket" and self.shiprocket_shipment_id:
            res_status, res_message = self.carrier_id and self.carrier_id.generate_shiprocket_label(self)
            if not res_status:
                raise ValidationError(res_message)
            else:
                return {'effect': {
                    'fadeout': 'slow',
                    'message': "Label Imported Successfully..",
                    'img_url': '/web/static/src/img/smile.svg',
                    'type': 'rainbow_man'}}
