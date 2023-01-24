clf
figure(100)
%color_att is a 3-column matrix of RGB triplets with length of LenS
%read in shapefile
lonlim=[60, 80];
latlim = [20, 40];
huc = shaperead('pakistan_districts.shp','UseGeoCoords', true, 'BoundingBox', [lonlim',latlim']);
lenS = length(huc);
faceColors = makesymbolspec('Polygon',{'INDEX',[1 lenS],'FaceColor',cmp});
%lenS is the number of polygon

ax = usamap(latlim,lonlim); %plot frame using usamap as template 
axis off; framem on; gridm on; mlabel on; plabel on;
setm(gca,'MLabelLocation',10) %interval for meridians labeling
setm(gca,'PLabelLocation',5)  %interval for parallels labeling

geoshow(ax, huc, 'SymbolSpec', faceColors);
