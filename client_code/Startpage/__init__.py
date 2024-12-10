from ._anvil_designer import StartpageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
import anvil.js
from anvil.tables import app_tables

class Startpage(StartpageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    url = anvil.js.window.location.href
    queryparams = anvil.server.call('get_query_params', url)
    accno = queryparams.get('AccountNo', [None])[0]
    
    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    username = self.textbox_username.text
    passwort = self.textbox_passwort.text
    Resultpage = open_form('Startpage.Resultpage')
    Resultpage.Label_result.text =  anvil.server.call("get_user",username, passwort)
