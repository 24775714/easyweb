$(function () {
	var ostitle = $("div#os_tilte");
// init main-layout 
    var tabindex=0;
    $('#layout').w2layout( {
        name: 'layout',
        title:'系统设置',
        padding: 0,
        panels: [
            { type: 'top', size: 85 ,content: ostitle.show() },
            { type: 'left', size: 200, resizable: true, minSize: 120 ,content:'<div id="sidebar" style="width: 100%; height: 100%;"></div>'},
            { type: 'main', overflow: 'hidden',
            	style: 'background-color: white; border: 1px solid silver; border-top: 0px; padding: 10px;',
                tabs: {
                	name: 'tabs',
                    active: 'tab0',
                    tabs: [{ id: 'tab0', caption: 'Maintab' }],
                    onClick: function (event) { 
                    	event.onComplete = function () { 
                    		var tabs = w2ui.layout_main_tabs;	
	                		//w2ui.layout.content('main','');
	               			$().w2destroy('grid'+event.target);
	               			$().w2destroy('form'+event.target);
	               			$().w2destroy('layout'+event.target);
	               			$().w2destroy('popup'+event.target);
	               			this.refresh(); 
	               			w2ui.layout.content('main','');	            				
	                		w2ui.layout.load('main', event.object.route , 'pop-in',function () { tabs.add(evnet);tabs.select(event.target);}); 
                       }
                    },
                    show : {               // indicates what sections are shown
                        tabs    : true,    
                        toolbar : true
                    },
                    onClose: function (event) {
                    	var tabs = w2ui.layout_main_tabs;
						$().w2destroy('grid'+event.target);
	               		$().w2destroy('form'+event.target);	
	               		$().w2destroy('layout'+event.target);
	               		$().w2destroy('popup'+event.target);	
	                    this.remove(event.target);
	                    this.refresh();
	                    w2ui.layout.content('main','');	                    	
	                    w2ui.layout.load('main', "/showTabs/tab0" , 'pop-in', function () { tabs.select('tab0'); });
	                               	                	                    	 	
                    }
                }
            },
            { type: 'bottom', size: 30 ,content: ''},
        ]
    });
 	 
 // sidebar
    $('#sidebar').w2sidebar({
            name: 'sidebar',
            //routeData: { id: 14 },        
            onClick: function (event) {
               var tabs = w2ui.layout_main_tabs;
               w2ui.layout.content('main',''); 
               $().w2destroy('grid'+event.target);
               $().w2destroy('form'+event.target);

               $().w2destroy('layout'+event.target);
               $().w2destroy('popup'+event.target);
               w2ui.layout.refresh('main');
               tabs.refresh(); 
               tabs.add({ id: event.target, caption: event.object.text, route:event.object.route, closable: true });                             
    		   w2ui.layout.load('main', event.object.route , 'pop-in', function () { tabs.select(event.target);});  
            }
    });
    
    w2ui.layout.load('main', "/showTabs/tab0" , 'pop-in', function () { 
    	var tabs = w2ui.layout_main_tabs;
    	tabs.select('tab0'); 
    });   

});