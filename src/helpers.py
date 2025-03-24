import win32print
import subprocess
import platform
import pandas as pd
import datetime


def process_printer(printer_handle, registers,  b_q, r_n, b_c, datee):
        """
        Sends a raw print job to the printer.

        This function sends a raw print job to the printer specified by the printer handle.
        The content of the print job must be a byte string. The function handles the
        printer spooler to send the job to the printer.

        Parameters
        ----------
        printer_handle : int
            The handle of the printer obtained from win32print.OpenPrinter.
        content : bytes
            The content of the print job.

        Returns
        -------
        None
        """
        x = 402
        y=352
        dy = 40
        dx = 208
        x2 = x - dx
        y2 = 352

        content = f"""
	        SIZE 101.10 mm, 51.1 mm
            GAP 3 mm, 0 mm
            CODEPAGE UTF-8
            TEXT 764,363,"0",180,12,12,"Ref Num " + "{r_n}"
            TEXT 761,274,"0",180,10,10,"Bin Qty " + "{b_q}"
            TEXT 761,317,"0",180,10,10,"Bin Count " + "{b_c}"
            TEXT 761,237,"0",180,10,10,"Load Date " + "{datetime.datetime.now().strftime('%m-%d-%Y')}"
            TEXT 761,197,"0",180,10,10,"Start Time " + "{datee}"
            TEXT 761,155,"0",180,10,10,"End Time " + "{datetime.datetime.now().strftime('%H:%M:%S')}"
            
"""
        #sumar cantidades de cada factura
        sum_ = registers['Cantidad'].sum()
        for index, row in registers.iterrows():
            print(row)
            if index <= 6:
                content += f"""
                TEXT {x},{y},"0",180,8,8,"{row['Cantidad']}" + " " + "{row['Factura']}"
            """
                y -= dy
            elif index > 6 and index <= 12:
                content += f"""
                TEXT {x2},{y2},"0",180,8,8,"{row['Cantidad']}" + " " + "{row['Factura']}"
                """
                y2 -= dy
            else:
                content += f"""
                TEXT {x2},{y2},"0",180,8,8,"MÁS..."
                """
                y2 -= dy
                
        content += f"""
            BAR 120,64, 300, 3	
            TEXT 279,54,"0",180,8,8,"{sum_}" + " TOTAL"
            PRINT 1,1
            CLS
            EOJ
            """
        try:

            hJob = win32print.StartDocPrinter(
                printer_handle, 1, ("Etiqueta", None, "RAW")
            )
            win32print.StartPagePrinter(printer_handle)

            win32print.WritePrinter(printer_handle, content.encode("utf-8"))

            win32print.EndPagePrinter(printer_handle)
            win32print.EndDocPrinter(printer_handle)
        finally:

            win32print.ClosePrinter(printer_handle)

            

def list_active_printers():
    """
    Returns a list of active printers on the system.

    This function uses different methods for Windows, Linux, and macOS to
    determine which printers are active. On Windows, it uses the win32print
    module to query the print spooler. On Linux and macOS, it uses the
    lpstat command to get the status of the printers.

    Returns an empty list if no active printers are found or if the
    system is not supported.

    :return: A list of active printer names
    """
    system = platform.system()
    if system == "Windows":
        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
        # Filter only active printers
        active_printers = []
        for printer in printers:
            handle = win32print.OpenPrinter(printer[2])
            status = win32print.GetPrinter(handle, 2)  # Level 2 for detailed info
            if status['Status'] == 0:  # Status 0 usually means active/ready
                active_printers.append(printer[2])
            win32print.ClosePrinter(handle)
        return active_printers
    elif system in ["Linux", "Darwin"]:  # Darwin is macOS
        result = subprocess.run(["lpstat", "-p"], capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.splitlines()
            active_printers = [
                line.split(" ")[1]
                for line in lines
                if "idle" in line.lower() or "printing" in line.lower()
            ]
            return active_printers
        else:
            return []
    else:
        return []
    

def print_reports(registers,  b_q, r_n,b_c,datee, printer_name):
    """
    Sends a raw print job to the printer specified by printer_name.

    The report to be printed is generated from the registers dataframe, which
    contains the report data, and the other parameters.

    Parameters
    ----------
    registers : pandas.DataFrame
        The dataframe containing the report data
    b_q : str
        The bin quantity
    r_n : str
        The ref number
    b_c : str
        The bin count
    datee : str
        The date in the format '%H:%M:%S'
    printer_name : str
        The name of the printer to send the job to

    Returns
    -------
    None
    """
    printer_handle = win32print.OpenPrinter(printer_name)
    process_printer(printer_handle, registers,  b_q, r_n, b_c, datee)