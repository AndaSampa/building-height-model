# Raster das edificações de São Paulo a partir do LiDAR 3D

O Modelo de Superfície (MDS) LiDAR 3D contém o levantamento de pontos classificados de toda extensão da cidade de São Paulo. Volumetria e ocupação das edificações é uma abirdagem do MDS LiDAR comum à diversas discilplinas do urbanismo. Trabalhar com o conjunto de dados total da cidade de São Paulo, não é uma tarefa trivial do ponto de vista de capacidade computacional. Uma das estratégias e criar produtos específicos mais simples e com foco em determinado aspecto, por exemplo o Modelo de Altura das edificações (Building Height Model - BHM). Neste caso, um formato matricial (raster), com uma grade de 1 metro contendo a altura máxima em relação ao solo, dos pontos classificados como edificação.

## Objetivo

Este repositório tem o objetivo de documentar o processo de obtenção do Raster das edificações de São Paulo a partir do LiDAR 3D, assim como publicar e disponibilizar os resultados obtidos. Dessa maneira, pretendemos dar autonomia a quem deseja somente utilizar os dados processados, mas também aos que querem reproduzir o processamento com outros parâmetros, para diversas outras finalidades.

## Materiais e métodos

Para obtenção do resultado foi utilizado Python e a biblioteca Pdal para acessar os dados da publicação da nuvem de pontos LiDAR MDS da Cidade de São Paulo. A cidade foi dividida em uma articulação UTM, tomando como limites a caixa delimitadora mínima do município, dividindo-a em 14 quadrículas, sendo 4 horizontais e 6 verticais, nomeadas de 01 à 24 iniciando no canto inferior à sudoeste, de baixo para cima, linha por linha, e suprimidas aquelas que não intersectavam com o limite do município, conforme a imagem abaixo.

![Articulação BHM](articulacao-BHM.png)

## Resultados

Os resultados processados estão disponíveis na pasta `resultados` em arquivos GeoPackage, que podem ser abertos e visualizados no QGis e em diversos softwares de GeoProcessamento.

## Limitações

O resultado obtido é realizado à partir da dimensão `UserData` do levantamento LiDAR ALS publicado, que contem um campo `byte` de numeros inteiros variando de 0 à 255 metros. Dessa forma tem uma precisão de metro em metro nos 3 eixos.