# Modelo de altura das edificações e vegetação de São Paulo a partir do LiDAR 3D

O Modelo de Superfície (MDS) LiDAR 3D contém o levantamento de pontos classificados de toda extensão da cidade de São Paulo. Volumetria e ocupação das edificações são abordagens do MDS LiDAR comum à diversas discilplinas do urbanismo. Trabalhar com o conjunto de dados total da cidade de São Paulo, não é uma tarefa trivial do ponto de vista de capacidade computacional. Uma das estratégias é criar produtos específicos mais simples e com foco em determinado aspecto, por exemplo o Modelo de Altura das edificações (MAE), também chamado de Building Height Model (BHM) ou Modelo de Altura das Copas (MAC) também chamado de Vegetation Height Model (VHM). Neste caso, um formato matricial (raster), com uma grade de 1m ou 50cm contendo a altura máxima em relação ao solo, dos pontos classificados como edificação ou vegetação.

## Objetivo

Este repositório tem o objetivo de documentar o processo de obtenção do Raster das edificações e copas de São Paulo a partir do LiDAR 3D, assim como publicar e disponibilizar os resultados obtidos. Dessa maneira, pretendemos dar autonomia a quem deseja utilizar os dados processados, mas também aos que querem reproduzir, alterar ou melhorar o processamento com outros parâmetros, para diversas finalidades.

## Materiais e métodos

Para obtenção do resultado, foi utilizado Python e a biblioteca Pdal afim de acessar os dados da publicação da nuvem de pontos LiDAR MDS da Cidade de São Paulo. A cidade foi particionada em uma articulação UTM, tomando como limites a caixa delimitadora mínima do município, dividindo-a em 24 quadrículas, sendo 4 horizontais e 6 verticais, nomeadas de 01 à 24 iniciando no canto inferior à sudoeste, de baixo para cima, linha por linha, e suprimidas aquelas que não intersectavam com o limite do município, conforme a imagem abaixo.

![Articulação MA](Articulação-MA.png)

## Resultados

Os resultados processados com resolução espacial de 1m e resolução espectral de altura de 8bits estão disponíveis na pasta `resultados` em arquivos GeoPackage, que podem ser abertos e visualizados no QGis e em diversos softwares de GeoProcessamento.

Os arquivos do Modelo de Altura das Edificações (MAE) tem o prefixo MAE-XX, onde XX é o número da quadrícula, assim como o Modelo de Altura das Copas (vegetação) (MAC) tem o prefixo MAC-XX seguinto a mesma lógica.

### Resultados mais recentes e precisos no Kaggle

Mais recentemente, um processameto com uma resolução espacial de 50cm, ou seja, mais preciso e denso, foi disponibilizado na plataforma Kaggle e deve ser utilizado preferencialmente. Os métodos dos processamentos estão disponíovis aqui neste repositório, no entanto, os dados estão disponibilizados no Kaggle pelo seguinte endereço http://www.kaggle.com/andasampa/height-model

### Limitações dos resultados publicados no GitHub

O resultado obtido e disponibilizado aqui no GitHub é realizado à partir da dimensão `UserData` do levantamento LiDAR ALS publicado, que contem um campo `byte` de numeros inteiros variando de 0 à 255 metros. Dessa forma tem uma precisão de metro em metro nos 3 eixos (X, Y e Z). No entanto, os dados publicados no [Kaggle](http://www.kaggle.com/andasampa/height-model) além de possuir resolução espacial de 50cm estão com precisão de 32bits da altura em relação ao Modelo Digital de Terreno e deve ser utilizado preferencialmente.