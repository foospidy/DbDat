var json   = JSON.parse(readJSON('data/report.json'));
var levels = ['RED', 'YELLOW', 'ORANGE', 'GRAY', 'GREEN'];
var menu   = '';

document.getElementById('title').innerHTML = json.title;

sortJsonArrayByProperty(json.report_data, 'json.report_data.category');

for(var l in levels) {
		menu += '<a href="javascript:filter(\'' + levels[l] + '\');">' + levels[l] + '</a> &nbsp;';
}

document.getElementById('menu').innerHTML = menu;

for(var l in levels) {
    for(var i in json.report_data) {
        if(levels[l] == json.report_data[i].result.level) {
            h = '';
            h = json.report_data[i].category + ' ' + json.report_data[i].title + ' (' + json.report_data[i].result.level + ')';
            h = h + '<div style="margin-left:5px;"><pre>' + json.report_data[i].description + '</pre></div>';
            h = h + '<div style="margin-left:25px;"><pre>' + json.report_data[i].result.output + '</pre></div>';
        
            var div       = document.createElement('div');
            div.innerHTML = h;
            
            document.getElementById('results').appendChild(div);
        }
    }   
}

function filter(level) {
	document.getElementById('results').innerHTML = '';
	for(var i in json.report_data) {
		if(level == json.report_data[i].result.level) {
			h = '';
			h = json.report_data[i].category + ' ' + json.report_data[i].title + ' (' + json.report_data[i].result.level + ')';
			h = h + '<div style="margin-left:5px;"><pre>' + json.report_data[i].description + '</pre></div>';
			h = h + '<div style="margin-left:25px;"><pre>' + json.report_data[i].result.output + '</pre></div>';
		
			var div       = document.createElement('div');
			div.innerHTML = h;
			
			document.getElementById('results').appendChild(div);
		}
	}   
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
