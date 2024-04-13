from odoo import api, fields, models
from geopy.geocoders import Nominatim
import werkzeug.urls
class eventInherited(models.Model):
    _inherit = 'event.event'
    mapChoice = fields.Selection([('a', 'Open Street Maps'),('b', 'Google Maps'), ], default='a', required=True, string="Map", tracking=True)
    def _google_map_link(self, zoom=8):
        self.ensure_one()
        if self.address_id:
            if(self.mapChoice=='a'):
                params = {
                'q': '%s, %s %s, %s' % (self.sudo().address_id.street or '', self.sudo().address_id.city or '', self.sudo().address_id.zip or '', self.sudo().address_id.country_id and self.sudo().address_id.country_id.display_name or ''),
                'z': zoom,
                }
                print(werkzeug.urls.url_encode(params))
                return 'https://nominatim.openstreetmap.org/ui/search.html?'+werkzeug.urls.url_encode(params)
            else:
                return self.sudo().address_id.google_map_link(zoom=zoom)

        return None

class osmManager(models.Model):
    _name = "osms.osm"
    _inherit = ["mail.thread"]
    _description = "osms"

