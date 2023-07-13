from Excel import usarExcel
from Button import HoverButton
import webbrowser

class btn_listagem():
    def __init__(self, janela):
        #LINHA UM
        HoverButton(janela, text="Programar KIT", coluna=1, linha=1, fg="black", bg="white",font =
                ('calibri', 20, 'bold'), borderwidth = '4', activebackground='#C5C7C4',
                command=lambda: usarExcel.abrirExcel("Q:\GROUPS_BR_SP_SBC\BR_SP_SBC_WM_FABRICACAO\LOGISTICA\PCP\PARTES E PEÇAS E KIT'S\PROGRAMAÇÃO DE KIT AUTOMATIZADO/FERRAMENTA PARA PROGRAMAÇÃO PARTES E PEÇAS_KITS.xlsm"))  

        HoverButton(janela, text="Acompanhar KIT", coluna=2, linha=1, fg="black", bg="white",font =
                    ('calibri', 20, 'bold'), borderwidth = '4', activebackground='#C5C7C4',
                command=lambda: usarExcel.abrirExcel("Q:\GROUPS_BR_SP_SBC\BR_SP_SBC_WM_FABRICACAO\LOGISTICA\PCP\PARTES E PEÇAS E KIT'S\PROGRAMAÇÃO DE KIT AUTOMATIZADO\RELAÇÃO O.V. - Macro.xlsm")) 
        
        HoverButton(janela, text="Atualizar Indicadores", coluna=3, linha=1, fg="black", bg="white",font =
                    ('calibri', 20, 'bold'), borderwidth = '4', activebackground='#C5C7C4',
                command=lambda: usarExcel.abrirExcel("Q:\GROUPS_BR_SP_SBC\BR_SP_SBC_WM_FABRICACAO\LOGISTICA\INDICADORES AUTOMATIZADOS\GR_PROGRAMAÇÃO\IndicadoresWSB.xlsm"))

        #LINHA DOIS
        HoverButton(janela, text="Gerar HU", coluna=1, linha=2, fg="black", bg="white",font =
                    ('calibri', 20, 'bold'), borderwidth = '4', activebackground='#C5C7C4',
                command=lambda: usarExcel.abrirExcel("Q:\GROUPS_BR_SP_SBC\BR_SP_SBC_WM_FABRICACAO\LOGISTICA\CENTRAL DE MACRO PCP\MACROS\GERAR HU - SBC.xlsm"))  
        
        HoverButton(janela, text="Apontar", coluna=2, linha=2, fg="black", bg="white",font =
                    ('calibri', 20, 'bold'), borderwidth = '4', activebackground='#C5C7C4',
                command=lambda: usarExcel.abrirExcel("Q:\GROUPS_BR_SP_SBC\BR_SP_SBC_WM_FABRICACAO\LOGISTICA\CENTRAL DE MACRO PCP\MACROS\Apontamentos.xlsm"))  
        
        HoverButton(janela, text="Ir para Indicador Power BI", coluna=3, linha=2, fg="black", bg="white",font =
                    ('calibri', 20, 'bold'), borderwidth = '4', activebackground='#C5C7C4',
                command=lambda: webbrowser.open_new('https://app.powerbi.com/view?r=eyJrIjoiNThjNGIyZTQtYTBjYi00MGY3LWI2MzYtOGI1ZTA4ZTgzMGE0IiwidCI6Ijg4NjY2NmE2LWE4ZDItNDYwNC1hMDAyLTk1YjYyMmNiN2UxOCIsImMiOjR9'))  
        
        #LINHA TRÊS
        HoverButton(janela, text="Transferir HU", coluna=1, linha=3, fg="black", bg="white",font =
                    ('calibri', 20, 'bold'), borderwidth = '4', activebackground='#C5C7C4',
                command=lambda: usarExcel.abrirExcel("Q:\GROUPS_BR_SP_SBC\BR_SP_SBC_WM_FABRICACAO\LOGISTICA\CENTRAL DE MACRO PCP\MACROS\TRANSFERENCIAS WEX.xlsm"))  
        
