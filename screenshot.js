
var system = require('system');
var webpage = require('webpage');


var args = system.args
console.log(args)

width = args[1] || 800
height = args[2] || 1200
delay = args[3] || 3
filename = args[4] || 'report.png'


console.log('width: ' + width)
console.log('height: ' + height)
console.log('delay: ' + delay)
console.log('filename: ' + filename)


var url = 'http://taojy123.cn:30416/query/ddc_daily_report/'
// var url = 'http://prod.tflag.cn:32370/query/ddc_daily_report/'

var page = webpage.create()
page.viewportSize = {
    width: width,
    height: height
}

page.open(url, function (status) {
    setTimeout(function(){
        // page.render('report.png', {quality: 100})
        page.render(filename)
        console.log('ok')
        phantom.exit()
    }, delay * 1000)
})

