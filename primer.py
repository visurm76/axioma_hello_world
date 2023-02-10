from axipy import init_axioma, CoordTransformer, CoordSystem, provider_manager, ExcelDataProvider

os.environ["AXIOMA_LOG_LEVEL"] = "2"
os.environ["AXIOMA_LANGUAGE"] = "ru"
init_axioma()  # инициализация


crs = CoordSystem.from_epsg(4326)
print(crs.name)


crs = CoordSystem.from_string('prj:Earth Projection 12, 62, "m", 0')
print(crs.name)


""" Transform coordinate"""
transformer = CoordTransformer('epsg:4326', 'epsg:26953')
coordinate = (55.76, 37.6)
result = transformer.transform(coordinate)
print(f"Point({result.x}, {result.y})")

"""Dict provide """
#print(provider_manager.loaded_providers())

"""Open file"""

#source = ExcelDataProvider.open('C:\Program Files\Axioma v4\Files\primer.xlsx')
#table = source.open()
table = provider_manager.openfile('C:\Program Files\Axioma v4\Files\primer.xlsx')
print(table)

raster = provider_manager.tms.open('https://maps.axioma-gis.ru/osm/{LEVEL}/{ROW}/{COL}.png')
