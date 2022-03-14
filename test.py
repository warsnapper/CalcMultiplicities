import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import BuiltInCategory, Parameter

elements = FEC(doc).OfCategory(BuiltInCategory.OST_MEPSpaces)

for element in elements:
    multiplicity = element.LookupParameter('Кратность')
    multiplicity.SetValueString('Test2')
    print multiplicity.AsString()