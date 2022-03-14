import pdal 
import numpy as np
import json
import geopandas as gpd
import sys
from os.path import exists

dest_folder = sys.argv[1]

quadriculas = gpd.read_file('zip://GIS/SIRGAS_SHP_quadriculamdt.zip!SIRGAS_SHP_quadriculamdt')

pipeline=[
    {
        "type": "readers.las",
        "filename": "https://laz-m3dc-pmsp.s3-sa-east-1.amazonaws.com/MDS_color_3436-442.laz"
    },
    {
        "type":"filters.range",
        "limits":"Classification[5:6]"
    },
    {
        "type":"filters.hag_dem",
        "raster": "/media/feromes/FEROMES/MDT_sampa-ZSTD.tif"
    },
    {
        "filename":"processamentos/BHM-3314-231.tif",
        "gdaldriver":"GTiff",
        "output_type":"max",
        "resolution":"0.5",
        "nodata":"0",
        "data_type": "float32",
        "type": "writers.gdal",
        "where": "(Classification == 6)",
        "override_srs": "EPSG:31983"
    },
    {
        "filename":"processamentos/VHM-3314-231.tif",
        "gdaldriver":"GTiff",
        "output_type":"max",
        "resolution":"0.5",
        "nodata":"0",
        "data_type": "float32",
        "type": "writers.gdal",
        "where": "(Classification == 5)",
        "override_srs": "EPSG:31983"
    }
  ]


for i, row in quadriculas.iterrows():
    scm = row.qmdt_cod
    bhm_file = f'{dest_folder}/BHM/BHM-{scm}.tif'
    vhm_file = f'{dest_folder}/VHM/VHM-{scm}.tif'

    if exists(bhm_file) and exists(vhm_file):
        continue
    else:
        print(f'Processando SMC: {scm} ...')
        pipeline[0]['filename'] = f"https://laz-m3dc-pmsp.s3-sa-east-1.amazonaws.com/MDS_color_{scm}.laz"
        pipeline[3]['filename'] = bhm_file
        pipeline[4]['filename'] = vhm_file

        pdal_pipeline = pdal.Pipeline(json.dumps(pipeline))

        try: 
            pdal_pipeline.execute()
        except: 
            try:
                # print(f'SCM {scm} sem vegetação!')
                pdal_pipeline = pdal.Pipeline(json.dumps(pipeline[0:4]))
                pdal_pipeline.execute()
            except:
                try:
                    print(f'SCM {scm} sem edificação!')
                    pipeline_sv = pipeline.copy()
                    del pipeline_sv[3]
                    pdal_pipeline = pdal.Pipeline(json.dumps(pipeline_sv))
                    pdal_pipeline.execute()
                except:
                    continue
                
        



        