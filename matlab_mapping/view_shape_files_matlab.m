clf
m_proj('oblique mercator');  % repeated here so cut-n-paste simplified
m_coast('patch',[.1 .7 .5],'edgecolor','none');
m_grid('xlabeldir','end','fontsize',10);
m_line(-129,48.5,'marker','square','markersize',4,'color','r');
m_text(-129,48.5,' M5','vertical','top');