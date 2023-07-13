import win32com.client

class usarExcel():
    def abrirExcel(nome):
        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible = True
        excel.Workbooks.Open(nome)
