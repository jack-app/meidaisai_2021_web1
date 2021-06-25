document.getElementById( "map" ).addEventListener( "click", function( event ) {
	var clickX = event.pageX ;
	var clickY = event.pageY ;

	var map = document.getElementById('map');
	var style = window.getComputedStyle(map);

	// 要素の位置を取得
	var clientRect = map.getBoundingClientRect() ;
	var positionX = clientRect.left + window.pageXOffset ;
	var positionY = clientRect.top + window.pageYOffset ;

	// 要素内におけるクリック位置を計算 ver X , ver y が画面の座標　マップ要素のwidthを取ってきて割合を出す。それを保存
	var x = clickX - positionX ;
	var y = clickY - positionY ;

 	var imgWidth  = Number(style.width.split('px')[0])
 	var imgHeight = Number(style.height.split('px')[0])

  var ratioX = x / imgWidth ;
  var ratioY = y / imgHeight ;

	let formElements = document.forms.tweetForm;
	formElements.positionX.value = ratioX;
	formElements.positionY.value = ratioY;
} ) ;