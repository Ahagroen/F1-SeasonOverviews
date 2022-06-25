from . import OutputFileCreation as OFC
from . import Input
from openpyxl import load_workbook
import os

yearlist =[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
for year in yearlist:
    decade = str(year)[:3]+"0s"
    if os.path.exists(decade+".xlsx"):
        workbook = load_workbook(filename = decade+".xlsx")
        sheet = OFC.SheetCreation(year,workbook)
    else:
        workbook = OFC.WorkBookCreation(decade)
        sheet = OFC.SheetCreation(year,workbook)
    workbook.save(filename=decade+".xlsx")

DriverList = Input.DriversList(Input.getDriverStandings(year))
def getOneDriversRaces(driver,team):
    Input.getReleventRaces(team,Input.getRaces(driver,year),driver)