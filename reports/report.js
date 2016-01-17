var json   = JSON.parse(readJSON('data/report.json'));
var levels = ['RED', 'YELLOW', 'ORANGE', 'GRAY', 'GREEN'];
var count  = {RED:'0', YELLOW:'0', ORANGE:'0', GRAY:'0', GREEN:'0'};
var menu   = '';
var body   = '';

sortJsonArrayByProperty(json.report_data, 'json.report_data.category');

for(var l in levels) {
	var bgcolor = getColor(levels[l]);
	
    for(var i in json.report_data) {
        if(levels[l] == json.report_data[i].result.level) {
			count[levels[l]]++;
			
            body += '<div style="margin-left:5px;border-bottom:2px solid ' + bgcolor + ';">' + json.report_data[i].category + ': ' + json.report_data[i].title + '</div>';
            body += '<div style="margin-left:5px;">' + json.report_data[i].description.replace(/(\r\n|\r|\n)/g, "<br/>").replace("<br/>", "") + '</div>';
            body += '<div style="margin-left:25px;"><pre>' + json.report_data[i].result.output + '</pre></div>';
        }
    }   
}

for(var l in levels) {
		bgcolor = getColor(levels[l]);
		menu   += '<a href="javascript:filter(\'' + levels[l] + '\');" style="color: '+ levels[l] + '">' + levels[l] + ' (' + count[levels[l]] + ') </a> &nbsp;';
}

var div       = document.createElement('div');
div.innerHTML = body;

document.getElementById('title').innerHTML = json.title;
document.getElementById('menu').innerHTML  = menu;
document.getElementById('results').appendChild(div);

function filter(level) {
	document.getElementById('results').innerHTML = '';
	var bgcolor                                  = getColor(level);
	var menu_info                                = '';
	
	switch(level) {
		case 'RED':
			menu_info = 'Items needing immediate attention.';
			break;
		case 'YELLOW':
			menu_info = 'Items needing review.';
			break;
		case 'ORANGE':
			menu_info = 'Checks that failed to execute properly. If the explination provided is unclear it may be a bug that should be reported here <a href="https://github.com/foospidy/DbDat/issues" target="_new">https://github.com/foospidy/DbDat/issues</a>.';
			break;
		case 'GRAY':
			menu_info = 'Items that may not be applicable to this version of the database.';
			break;
		case 'GREEN':
			menu_info = 'Items that passed.';
			break;
		default:
			menu_info = '';
			break;
	}
	
	document.getElementById('menu-info').innerHTML = menu_info;
	
	for(var i in json.report_data) {
		if(level == json.report_data[i].result.level) {			
			h  = '<div style="margin-left:5px;border-bottom:2px solid ' + bgcolor + ';">' + json.report_data[i].category + ': ' + json.report_data[i].title + '</div>';
			h += '<div style="margin-left:5px;">' + json.report_data[i].description + '</div>';
			h += '<div style="margin-left:25px;"><pre>' + json.report_data[i].result.output + '</pre></div>';
		
			var div       = document.createElement('div');
			div.innerHTML = h;
			
			document.getElementById('results').appendChild(div);
		}
	}   
}

function getColor(color_text) {
	var color = '';
	
	switch(color_text) {
		case 'YELLOW':
			color = '#ffff66';
			break;
		case 'GREEN':
			color = '#00cc00';
			break;
		default:
			color = color_text;
			break;
	}
	
	return color;
}

function readJSON(file) {
    var json_file = new XMLHttpRequest();
    var json = '';
    json_file.open("GET", file, false);
    json_file.onreadystatechange = function () {
        if(4 === json_file.readyState) {
            if(200 === json_file.status || 0 == json_file.status) {
                json = json_file.responseText;
            }
        }
    }
    json_file.send(null);
    
    return json;
}

// http://stackoverflow.com/questions/4222690/sorting-a-json-object-in-javascript
function sortJsonArrayByProperty(objArray, prop, direction){
    if (arguments.length<2) throw new Error("sortJsonArrayByProp requires 2 arguments");
    var direct = arguments.length>2 ? arguments[2] : 1; //Default to ascending

    if (objArray && objArray.constructor===Array){
        var propPath = (prop.constructor===Array) ? prop : prop.split(".");
        objArray.sort(function(a,b){
            for (var p in propPath){
                if (a[propPath[p]] && b[propPath[p]]){
                    a = a[propPath[p]];
                    b = b[propPath[p]];
                }
            }
            // convert numeric strings to integers
            a = a.match(/^\d+$/) ? +a : a;
            b = b.match(/^\d+$/) ? +b : b;
            return ( (a < b) ? -1*direct : ((a > b) ? 1*direct : 0) );
        });
    }
}
