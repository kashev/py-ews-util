py-ews-util
===========
    py-ews-util
    Kashev Dalmia
    kashev.dalmia@gmail.com

A short python script for displaying EWS Lab Utilization at the University of Illinois at Urbana Champaign. Uses the JSON data URL utilized by the web utilization count on [the EWS website](http://it.engineering.illinois.edu/ews/), and code similar to the Javascript on that website:

```Javascript
$(document).ready(function(){
    $.getJSON("https://my.engr.illinois.edu/labtrack/util_data_json.asp?callback=?",
        function(json_data) {
            var items = [];
            $.each(json_data.data, function(key, val) {
                items.push('<div id="' + val.strlabname.replace(/ /g,"_") + '" class="lab">' + 
                '<div class="name">' + val.strlabname + '</div>' +
                '<div class="graph" style="width: ' + Math.round(((val.inusecount / val.machinecount) * 100) / 2) + 'px; margin-right: ' + 
                Math.round((100 - Math.round(((val.inusecount / val.machinecount) * 100)))/2) + 'px;">&nbsp;</div>' + 
                '<div class="count">' + val.inusecount + ' / ' + val.machinecount + '</div><div class="clear">&nbsp;</div>' + 
                '</div>');
            });

        $('#workstations #data').html(items.join(''));
            
    });
});
```

Use case for this script is to not have to open up a web browser to see if you can get a spot in an EWS Lab. No more, no less.

