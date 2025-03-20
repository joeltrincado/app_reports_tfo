import flet as ft
from components.TextField import TextField_
from components.AppBar import AppBar_
import pandas as pd
from helpers import print_reports
import datetime


def main(page: ft.Page):
    #vars globals
    global b_q, r_n, b_c, c
    global registers
    global b_q_c
    global printer_name
    b_q = 1
    b_q_c = b_q
    r_n = ""
    b_c = ""
    c = ""
    printer_name = ""
    registers = pd.DataFrame( columns=['Factura', 'Cantidad'])

    #onchanges
    def onChnage_printer(e):
        """
        Updates the global printer_name variable with the selected printer.

        This function is triggered when the printer selection changes in the UI.
        It updates the global `printer_name` variable with the value from the
        control event and refreshes the page.

        Parameters
        ----------
        e : Event
            The event object containing the control with the new printer value.
        """

        global printer_name
        printer_name = e.control.value
        page.update()

    def b_q_change(e):
        """
        Updates the global b_q and b_q_c variables with the selected bin quantity.

        This function is triggered when the bin quantity selection changes in the UI.
        It updates the global `b_q` and `b_q_c` variables with the value from the
        control event and refreshes the page.

        Parameters
        ----------
        e : Event
            The event object containing the control with the new bin quantity value.
        """
        global b_q
        global b_q_c
        b_q = e.control.value
        try:
            b_q = int(b_q)
            b_q_c = b_q
            bin_qty.border_color = ft.Colors.BLACK
            page.update()
        except:
            bin_qty.value = 1
            bin_qty.border_color = "red"
            page.update()
    def r_n_change(e):
        global r_n
        r_n = e.control.value
    def b_c_change(e):
        global b_c
        b_c = e.control.value
    def c_change(e):
        global registers
        global b_q
        global r_n
        global b_c
        global b_q_c
        global printer_name
        position = e.control.value.find("EXPO")
        datee = datetime.datetime.now().strftime('%H:%M:%S')
        if position != -1:
            factura_value = e.control.value[position:]
            filter_inv = registers[registers['Factura'] == factura_value]
            if filter_inv.empty:
               new_row = pd.DataFrame([[factura_value, 1]], columns=["Factura", "Cantidad"])
               registers = pd.concat([registers, new_row], ignore_index=True)
            else:
                registers.loc[registers['Factura'] == factura_value, 'Cantidad'] += 1
            b_q_c -= 1
        if b_q_c == 0:
            print_reports(registers, b_q, r_n, b_c,datee, printer_name)
            bin_count.disabled = False
            ref_num.disabled = False
            btn_print.disabled = True
            btn_save.disabled = False
            bin_qty.disabled = False
            btn_save.bgcolor = ft.Colors.GREEN_900
            btn_print.bgcolor = ft.Colors.GREY_400
            bin_qty.value = 1
            code.disabled = True
            bin_count.value = ""
            ref_num.value = ""
        code.value = ""
        page.update()

     #setting page
    page.title = "SOFTWARE DE CONTROL DE REPORTES"
    page.appbar = AppBar_(onchange=onChnage_printer).create()
        
            
    #alerts
    alert = ft.AlertDialog(
        title=ft.Text("Alerta"),
        content=ft.Text("Complete todos los campos")
    ) 
    alert.open = False

    #functions
    def print_report(e):
        global b_q, r_n, b_c

    def save_data(e):
        global b_q, r_n, b_c
        if r_n != "" and b_c != "":
            btn_print.disabled = False
            code.disabled = False
            btn_save.disabled = True
            bin_qty.disabled = True
            ref_num.disabled = True
            bin_count.disabled = True
            btn_print.bgcolor = ft.Colors.BLUE_900
            btn_save.bgcolor = ft.Colors.GREY_400
            page.update()
        else:
            alert.open = True
            page.update()

   


    # inputs
    bin_qty = TextField_('Bin Qty', 200, b_q_change).create()
    ref_num = TextField_('Ref Num', 200, r_n_change).create()
    bin_count = TextField_('Bin Count', 200, b_c_change).create()
    code = ft.TextField(label="Código de Barras", width=200, on_submit=c_change, border_color=ft.colors.BLACK54,expand=True, shift_enter=True)
    code.disabled = True

    #btns
    btn_print = ft.ElevatedButton("Imprimir", on_click=lambda e: print_report(e), width=250, height=50,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.GREY_400,color=ft.Colors.WHITE, shape=ft.RoundedRectangleBorder(radius=5)))
    btn_print.disabled = True
    btn_save = ft.ElevatedButton("Guardar", on_click=lambda e: save_data(e), width=250, height=50,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_900,color=ft.Colors.WHITE, shape=ft.RoundedRectangleBorder(radius=5)))

    #page front end
    page.add(
        ft.Column(
            [
                ft.Row([bin_qty, ref_num, bin_count, btn_save], expand=True, height=60),
                ft.Row([code, btn_print], expand=True, height=60),
            ]
        ),
        alert
    )

ft.app(main)
