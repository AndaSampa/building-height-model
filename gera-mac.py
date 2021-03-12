import pdal
import json
import geopandas as gpd
import os.path
import zipfile

gdf_articulacao = gpd.read_file('resultados/articulacao.gpkg')

pipeline = [
    {
      "type": "readers.ept",
      "filename": "https://ept-m3dc-pmsp.s3-sa-east-1.amazonaws.com/ept.json",
      "bounds": "([336660.93307649984, 337183.60933703714], [7386487.347629301, 7393537.052770114])",
      "threads": 10,
      "resolution": 4,
      "spatialreference":"EPSG:31983"
    },
    {
        "type":"filters.range",
        "limits":"UserData[0:255],Classification[5:5]"
    },
    {
        "type":"filters.ferry",
        "dimensions":"UserData => Z"
    },
    {
        "type":"filters.reprojection",
        "out_srs":"EPSG:31983"
    },
    # {
    #     "type": "writers.las",
    #     "filename": "./resultados/edificacoes.laz",
    # },
    {
        "filename":"./resultados/edificacoes.gpkg",
        "gdaldriver":"GPKG",
        "output_type":"min",
        "resolution":"1.0",
        "nodata":"0",
        "data_type": "uint8",
        "gdalopts":"TABLE='Modelo de Altura de edificação',RASTER_TABLE='Modelo de Altura de edificação',RASTER_IDENTIFIER=altura",
        "type": "writers.gdal"
    },
    {
        "filename":"./resultados/edificacoes.tif",
        "gdaldriver":"GTiff",
        "output_type":"min",
        "resolution":"1.0",
        "nodata":"0",
        "data_type": "uint8",
        "type": "writers.gdal"
    }
]

for index, quadricula in gdf_articulacao.iterrows():
    
    if os.path.isfile(f'./resultados/MAC-{quadricula.nome}.gpkg'):
        print(f'MAC-{quadricula.nome}.gpkg já existe!')
    else:
        xmin, ymin, xmax, ymax = quadricula.geometry.bounds
        pipeline[0]['bounds'] = f'([{xmin}, {xmax}], [{ymin}, {ymax}])'
        pipeline[4]['filename'] = f'./resultados/MAC-{quadricula.nome}.gpkg'
        pipeline[5]['filename'] = f'./resultados/MAC-{quadricula.nome}.tif'
        
        pdal_pipeline = pdal.Pipeline(json.dumps(pipeline))
        pdal_pipeline.validate()
        
        pdal_pipeline.execute()
        
        print(pipeline[0]['bounds'])

    if not os.path.isfile(f'./resultados/MAC-{quadricula.nome}.tif.zip'):
        
        tif_zip = zipfile.ZipFile(f'./resultados/MAC-{quadricula.nome}.tif.zip', 'w')
        tif_zip.write(f'./resultados/MAC-{quadricula.nome}.tif', compress_type=zipfile.ZIP_DEFLATED)
 
        tif_zip.close()