import flet as ft
from helpers import list_active_printers


class AppBar_():
    def __init__(self,page, onchange):
        self.printer = "" 
        self.printers = list_active_printers()
        self.printers_list = [ft.dropdown.Option(i) for i in self.printers]
        self.on_change = onchange  
        self.page = page
        self.alert_help = ft.AlertDialog(
            title=ft.Text("Ayuda"),
        
            content=ft.Container(
            height=400,
            content=ft.Column(
                [ft.Text("""
            Uso de Impresoras en Desarrollo - Requisitos y Configuración  

            Si estás utilizando una impresora en un entorno de desarrollo, es importante seguir estos pasos para garantizar que el software funcione correctamente.  

            Instalar DiagTools 

            El software requiere que DiagTools esté instalado en tu sistema. Puedes descargarlo desde https://tectronic.mx/.  

            Asegúrate de instalar la versión más reciente para evitar problemas de compatibilidad.  

            Ignorar el archivo auto.bas

            Algunas impresoras incluyen el archivo auto.bas en su configuración. Para evitar conflictos, este archivo debe ser ignorado o eliminado de la configuración.  
            Revisa la documentación de tu impresora para conocer el procedimiento correcto.  

            Verificar la Configuración  

            Después de la instalación de DiagTools y la exclusión de auto.bas prueba la conexión.  

            Si la impresora no responde correctamente, revisa que los controladores estén actualizados.  

            Soporte Técnico

            Si encuentras problemas, consulta la documentación del software o contacta al soporte técnico de tu impresora.
            """, selectable=True)],
                scroll=ft.ScrollMode.AUTO 
            )),
          
        )      
    def onClick_help(self, e):
        self.alert_help.open = True
        self.page.update()
    def create(self):

        return ft.AppBar(
            elevation=1,
            leading_width=50,
            toolbar_height=60,
            bgcolor= ft.Colors.GREY_300,
            title=ft.Text(
                spans=[
                    ft.TextSpan(
                        "UNITED FARMS of oasis",
                        ft.TextStyle(
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            foreground=ft.Paint(
                                gradient=ft.PaintLinearGradient(
                                    (0, 200), (400, 200), ["#000000", "#000010"]
                                )
                            ),
                            font_family="times new roman",
                        ),
                    ),
                ],
            ),
            actions=[
                ft.Container(
                    content=ft.Dropdown(
                        options=self.printers_list,
                        on_change=self.on_change,    
                        value=self.printer,
                        label="Selecciona Impresora",
                        width=300,
                    ),padding=ft.padding.only(right=10)
                ),
            
                ft.Container(
                    content=ft.IconButton(
                        ft.Icons.HELP, tooltip="Ayuda", on_click=lambda _: self.onClick_help(_)),padding=ft.padding.only(right=10)
                ), self.alert_help
            ]
        )