import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import BuiltInCategory

elements = FEC(doc).OfCategory(BuiltInCategory.OST_MEPSpaces)

for element in elements:
    name = element.LookupParameter('Имя').AsString()
    flow = float(element.LookupParameter('Заданный расход приточного воздуха').AsValueString()[:-5])
    volume = float(element.LookupParameter('Объем').AsValueString()[:-3].replace(',', '.'))
    multiplicity = round(flow / volume, 1)
    print name, ' - ', flow, ' - ', volume, ' - ', multiplicity

# bprint(elements)