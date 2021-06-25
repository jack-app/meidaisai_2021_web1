var map = document.getElementById('map');
var style = window.getComputedStyle(map);

var imgWidth  = Number(style.width.split('px')[0])
var imgHeight = Number(style.height.split('px')[0])

let parent = document.body
let element = document.createElement("div")
element = parent.appendChild(element)
// element.style.cssText = `position:fixed; top: 100px; left: 100px; width: 10px; height: 10px; border-radius: 50%; background-color:red;`;


fetch('/get_positions')
  .then(response => response.json())
  .then(data => {
    // console.log(data["positions"])
    data["positions"].forEach(position => {
      let element = document.createElement("div")
			element = parent.appendChild(element)
			// console.log(element)
			var clientRect = map.getBoundingClientRect() ;
			var positionX = clientRect.left + window.pageXOffset ;
			var positionY = clientRect.top + window.pageYOffset ;
      let imgTop = imgHeight*position.position_y + positionY
      let imgLeft = imgWidth*position.position_x + positionX
			// console.log(imgHeight*position.position_x)
			// console.log(imgWidth*position.position_y)
      element.style.cssText = `position:absolute; top: ${imgTop}px; left: ${imgLeft}px; width: 10px; height: 10px; border-radius: 50%; background-color:red;`;
    });
  });

	// var clickX = event.pageX ;
	// var clickY = event.pageY ;

	// // 要素の位置を取得
	// var clientRect = this.getBoundingClientRect() ;
	// var positionX = clientRect.left + window.pageXOffset ;
	// var positionY = clientRect.top + window.pageYOffset ;

	// // 要素内におけるクリック位置を計算 ver X , ver y が画面の座標　マップ要素のwidthを取ってきて割合を出す。それを保存
	// var x = clickX - positionX ;
	// var y = clickY - positionY ;

	// var map = document.getElementById('map');
	// var style = window.getComputedStyle(map);

 	// var imgWidth  = Number(style.width.split('px')[0])
 	// var imgHeight = Number(style.height.split('px')[0])

  // var ratioX = x / imgWidth ;
  // var ratioY = y / imgHeight ;

	// let formElements = document.forms.tweetForm;
	// formElements.positionX.value = ratioX;
	// formElements.positionY.value = ratioY;