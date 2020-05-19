
var system = require('system');
var webpage = require('webpage');


var args = system.args
console.log(args)

url = args[1] || 'http://taojy123.cn:30416/query/ddc_daily_report/'
width = args[2] || 800
height = args[3] || 1200
delay = args[4] || 3
filename = args[5] || 'report.png'


console.log('url: ' + url)
console.log('width: ' + width)
console.log('height: ' + height)
console.log('delay: ' + delay)
console.log('filename: ' + filename)


var page = webpage.create()
page.viewportSize = {
    width: width,
    height: height
}

console.log('step 1')
page.open(url, function (status) {
	console.log('step 2')
    setTimeout(function(){
		console.log('step 3')
        // page.render('report.png', {quality: 100})
        page.render(filename)
        console.log('ok')
        phantom.exit()
    }, delay * 1000)
})

